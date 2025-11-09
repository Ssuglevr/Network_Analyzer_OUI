# Network Analyzer (Analizador de Red)

Un sencillo script de Python para escanear la red local, descubrir dispositivos conectados y mostrar su dirección IP, dirección MAC y fabricante.

## Características (Features)

* **Detección Automática de Red:** Detecta automáticamente tu subred local (ej. `192.168.1.0/24`) usando `psutil`.
* **Entrada Manual:** Permite al usuario especificar una red diferente para escanear.
* **Escaneo ARP:** Utiliza `scapy` para enviar peticiones ARP a la red y descubrir hosts activos.
* **Identificación de Fabricante:** Consulta la API de [macvendors.com](https://macvendors.com/) para identificar al fabricante del hardware basándose en los primeros 6 dígitos de la dirección MAC (OUI).
* **Menú Interactivo:** Una interfaz de línea de comandos simple para operar el escáner.

## Tecnologías Utilizadas

* Python 3
* [Scapy](https://scapy.net/): Para enviar y recibir paquetes de red (ARP).
* [Psutil](https://github.com/giampaolo/psutil): Para obtener información de las interfaces de red del sistema.
* [Requests](https://docs.python-requests.org/en/latest/): Para realizar consultas a la API de `macvendors.com`.

## Instalación y Uso

Este script debe ejecutarse con privilegios de administrador (sudo) para poder enviar paquetes ARP.

### 1. Prerrequisitos

* Python 3
* `pip` (o `pip3`)

### 2. Clonar el Repositorio

```bash
git clone [https://github.com/tu-usuario/nombre-del-repositorio.git](https://github.com/tu-usuario/nombre-del-repositorio.git)
cd nombre-del-repositorio
