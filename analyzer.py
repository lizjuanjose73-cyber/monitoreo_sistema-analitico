import re

LOG_FILE = "system.log"


def leer_datos():
    try:
        with open(LOG_FILE, "r") as f:
            contenido = f.read()

        # Extraer últimos valores registrados
        cpu = re.findall(r"CPU: (\d+\.?\d*)", contenido)
        ram = re.findall(r"RAM: (\d+\.?\d*)", contenido)
        disk = re.findall(r"DISK: (\d+)", contenido)

        if not cpu or not ram or not disk:
            print("No hay datos suficientes en el log.")
            return None

        return float(cpu[-1]), float(ram[-1]), int(disk[-1])

    except FileNotFoundError:
        print("Error: No se encontró el archivo system.log")
        return None


def analizar(cpu, ram, disk):
    print("\n===== ANÁLISIS DEL SISTEMA =====")
    print(f"CPU: {cpu}%")
    print(f"RAM: {ram}%")
    print(f"DISCO: {disk}%")
    print("--------------------------------")

    if cpu > 80:
        print("⚠️ ALERTA: Uso de CPU alto")

    if ram > 75:
        print("⚠️ ALERTA: Uso de RAM alto")

    if disk > 80:
        print("⚠️ ALERTA: Disco casi lleno")


def main():
    datos = leer_datos()

    if datos:
        analizar(*datos)
    else:
        print("No se pudo realizar el análisis.")


# 🔴 IMPORTANTE: ESTA ES LA LÍNEA CORRECTA
if __name__ == "__main__":
    main()
