import subprocess

# Comando para obtener la memoria disponible en Windows
comando_memoria = "wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value"
resultado_memoria = subprocess.run(comando_memoria, shell=True, capture_output=True, text=True)

# Obtener el resultado del comando para la memoria disponible
memoria_info = resultado_memoria.stdout.strip().splitlines()

memoria_total = 0
memoria_disponible = 0

for line in memoria_info:
    if "TotalVisibleMemorySize" in line:
        memoria_total = int(line.split('=')[1]) // (1024**2)  # Convertir bytes a MB
    elif "FreePhysicalMemory" in line:
        memoria_disponible = int(line.split('=')[1]) // (1024**2)  # Convertir bytes a MB

# Calcular el porcentaje de uso de la memoria
memoria_usada = memoria_total - memoria_disponible
porcentaje_uso_memoria = (memoria_usada / memoria_total) * 100 if memoria_total > 0 else 0

# Comando para obtener el rendimiento de red en Windows
comando_rendimiento_red = "wmic NIC get BytesSentPersec /Value"
resultado_rendimiento_red = subprocess.run(comando_rendimiento_red, shell=True, capture_output=True, text=True)

# Obtener el resultado del comando para el rendimiento de red
lineas = resultado_rendimiento_red.stdout.strip().splitlines()
rendimiento_red = 0

for line in lineas:
    if "BytesSentPersec" in line:
        rendimiento_red = int(line.split('=')[1]) // (1024**2)  # Convertir bytes a MB
        break

# Comando para obtener la temperatura del CPU en Windows
comando_temperatura_cpu = "wmic /namespace:\\\\root\\cimv2 PATH Win32_PerfFormattedData_Counters_ThermalZoneInformation get Temperature /Value"
resultado_temperatura_cpu = subprocess.run(comando_temperatura_cpu, shell=True, capture_output=True, text=True)

# Obtener el resultado del comando para la temperatura del CPU
lineas_temperatura = resultado_temperatura_cpu.stdout.splitlines()
temperatura_cpu = "No disponible en esta plataforma"

for linea in lineas_temperatura:
    if "Temperature" in linea:
        temperatura_cpu = linea.split('=')[1].strip()
        break

# Imprimir los resultados obtenidos
print(f"Memoria disponible: {memoria_disponible} MB")
print(f"Porcentaje de uso de la memoria: {porcentaje_uso_memoria:.2f}%")
print(f"Rendimiento de la red: {rendimiento_red:.2f} MB")
print(f"Temperatura del CPU: {temperatura_cpu}")



