#!/usr/bin/env python3
# mi programa de hardware - PC builder
# autor: kevin

import re
from abc import ABC, abstractmethod

# colores para la terminal
RESET  = '\x1b[0m'
BOLD   = '\x1b[1m'
DIM    = '\x1b[2m'
GRIS   = '\x1b[90m'
ROJO   = '\x1b[91m'
VERDE  = '\x1b[92m'
AMARI  = '\x1b[93m'
CYAN   = '\x1b[96m'
BLANCO = '\x1b[97m'
NEGRO  = '\x1b[30m'
BG_AM  = '\x1b[43m'
BG_CY  = '\x1b[46m'
BG_GR  = '\x1b[100m'

# colores segun la gama que el usuario elija
COLOR_GAMA = {
    'Alta':  {'borde': AMARI, 'tag': BG_AM + NEGRO,  'precio': BOLD + AMARI, 'entrada': AMARI},
    'Media': {'borde': CYAN,  'tag': BG_CY + NEGRO,  'precio': BOLD + CYAN,  'entrada': CYAN},
    'Baja':  {'borde': BLANCO,'tag': BG_GR + BLANCO, 'precio': BOLD + BLANCO,'entrada': BLANCO},
}

# para quitar los codigos de color al contar caracteres
def quitar_ansi(texto):
    return re.sub(r'\x1b\[[0-9;]*m', '', texto)

def longitud_visible(texto):
    return len(quitar_ansi(texto))

def rellenar(texto, n):
    faltan = n - longitud_visible(texto)
    if faltan > 0:
        return texto + ' ' * faltan
    return texto

# ====================
# CATALOGO DE PRODUCTOS
# ====================
CATALOGO = {
    'Alta': {
        'CPU': [
            ('Intel Core i9-14900K',       '24 nucleos / 6.0 GHz Turbo',   580),
            ('AMD Ryzen 9 7950X',           '16 nucleos / 5.7 GHz Turbo',   650),
            ('Intel Core i9-14900KS',      '24 nucleos / 6.2 GHz Turbo',   720),
        ],
        'GPU': [
            ('NVIDIA RTX 4080 Super',      '16 GB GDDR6X / DLSS 3.5',     1000),
            ('NVIDIA RTX 4090 24 GB',      '24 GB GDDR6X / Ray Tracing',  1700),
            ('AMD Radeon RX 7900 XTX',     '24 GB GDDR6 / FSR 3',         1050),
        ],
        'Motherboard': [
            ('ASUS ROG Maximus Z790',      'Z790 / WiFi 7 / DDR5',         550),
            ('MSI MEG Z790 ACE',           'Z790 / Thunderbolt 4 / DDR5',  500),
            ('Gigabyte Z790 Aorus Master', 'Z790 / WiFi 6E / DDR5',        480),
        ],
        'RAM': [
            ('64 GB DDR5 G.Skill Trident', '6000 MHz / 2x32 GB / CL30',   220),
            ('64 GB DDR5 Corsair Dominator','6400 MHz / 2x32 GB / RGB',    260),
            ('128 GB DDR5 Kingston Fury',  '5600 MHz / 4x32 GB',           420),
        ],
        'SSD': [
            ('Samsung 990 Pro 2 TB',       'PCIe 5.0 NVMe / 7450 MB/s',   180),
            ('WD Black SN850X 2 TB',       'PCIe 4.0 NVMe / 7300 MB/s',   160),
            ('Seagate FireCuda 530 2 TB',  'PCIe 4.0 NVMe / 7300 MB/s',   155),
        ],
        'HDD': [
            ('Seagate IronWolf Pro 8 TB',  '7200 RPM / NAS Grade',         220),
            ('WD Gold 8 TB',               '7200 RPM / Enterprise',        240),
            ('Seagate Exos X18 16 TB',     '7200 RPM / Enterprise',        380),
        ],
        'PSU': [
            ('Corsair AX1000',             '1000 W / 80+ Titanium',        280),
            ('Corsair AX1600i',            '1600 W / 80+ Titanium',        600),
            ('Seasonic PRIME TX-1000',     '1000 W / 80+ Titanium',        300),
        ],
        'Cooler': [
            ('NZXT Kraken Elite 360',      'Refrigeracion Liquida / LCD',  280),
            ('Corsair iCUE H150i Elite',   'Ref. Liquida / 360mm',         260),
            ('Arctic Liquid Freezer III',  'Ref. Liquida / 420mm',         120),
        ],
        'Chasis': [
            ('Lian Li O11 Dynamic EVO',    'E-ATX / Cristal Templado',     200),
            ('Corsair 7000D Airflow',      'Full Tower / Mesh',            250),
            ('Fractal Design Torrent XL',  'Full Tower / Airflow',         230),
        ],
        'Monitor': [
            ('Samsung Odyssey G9 49"',     'DQHD / 240 Hz / VA Curvo',   1100),
            ('LG UltraGear 32" 4K',        '4K / 144 Hz / Nano IPS',      800),
            ('ASUS ROG Swift PG42UQ 42"',  '4K / 138 Hz / OLED',         1300),
        ],
        'Teclado': [
            ('Razer Huntsman V3 Pro',      'Optico Analogico / RGB',       250),
            ('SteelSeries Apex Pro TKL',   'OLED / Switch Ajustable',      200),
            ('Corsair K100 RGB',           'OPX Optico / iCUE',            230),
        ],
        'Mouse': [
            ('Logitech G Pro X Superlight','Inalambrico / HERO 25K / 60g', 150),
            ('Razer DeathAdder V3 Hyper',  'Inalambrico / Focus Pro',      100),
            ('SteelSeries Prime Wireless', 'Inalambrico / TrueMove Air',   130),
        ],
    },

    'Media': {
        'CPU': [
            ('AMD Ryzen 5 7600X',          '6 nucleos / 5.3 GHz Turbo',   240),
            ('AMD Ryzen 7 7700X',          '8 nucleos / 5.4 GHz Turbo',   290),
            ('AMD Ryzen 7 7800X3D',        '8 nucleos / V-Cache 3D',      350),
        ],
        'GPU': [
            ('NVIDIA RTX 4060 Ti 8 GB',    '8 GB GDDR6 / DLSS 3',         380),
            ('NVIDIA RTX 4070 Super',      '12 GB GDDR6X / DLSS 3',       590),
            ('AMD Radeon RX 7800 XT',      '16 GB GDDR6 / FSR 3',         480),
        ],
        'Motherboard': [
            ('MSI MAG B650 Tomahawk',      'AM5 / DDR5 / WiFi 6E',        200),
            ('ASUS TUF Gaming B650-Plus',  'AM5 / DDR5 / WiFi 6',         210),
            ('Gigabyte B650 Aorus Elite',  'AM5 / DDR5 / 2.5G LAN',       220),
        ],
        'RAM': [
            ('32 GB DDR5 Kingston Fury',   '5200 MHz / 2x16 GB',          100),
            ('32 GB DDR5 G.Skill Flare X', '6000 MHz / 2x16 GB / CL36',  130),
            ('32 GB DDR5 Corsair Vengeance','5600 MHz / 2x16 GB / RGB',   120),
        ],
        'SSD': [
            ('Crucial P3 Plus 1 TB',       'PCIe Gen4 / 5000 MB/s',        60),
            ('Samsung 980 Pro 1 TB',       'PCIe Gen4 / 7000 MB/s',       100),
            ('WD Black SN770 1 TB',        'PCIe Gen4 / 5150 MB/s',        70),
        ],
        'HDD': [
            ('WD Blue 2 TB',               '5400 RPM / SATA',              55),
            ('Seagate Barracuda 4 TB',     '5400 RPM / SATA',              85),
            ('Toshiba P300 4 TB',          '7200 RPM / SATA',              80),
        ],
        'PSU': [
            ('EVGA SuperNOVA 650W G6',     '650 W / 80+ Gold',             85),
            ('Corsair RM750e',             '750 W / 80+ Gold',             95),
            ('Seasonic Focus GX-750',      '750 W / 80+ Gold / Modular',  120),
        ],
        'Cooler': [
            ('DeepCool AK620',             'Doble Torre / 260W TDP',        55),
            ('be quiet! Dark Rock 4',      'Torre Simple / 200W TDP',       65),
            ('Cooler Master Hyper 212',    'Torre Simple / RGB',            45),
        ],
        'Chasis': [
            ('NZXT H5 Flow',               'ATX / Mesh / Airflow',          85),
            ('Fractal Design Pop Air',     'ATX / Mesh / Positivo',         90),
            ('be quiet! Pure Base 500DX',  'ATX / Mesh / 3 Fans',         100),
        ],
        'Monitor': [
            ('LG UltraGear 27GN800 27"',   'QHD / 144 Hz / IPS',          230),
            ('Samsung Odyssey G5 27"',     'QHD / 165 Hz / VA Curvo',     220),
            ('MSI G274QPF-QD 27"',         'QHD / 170 Hz / IPS',          240),
        ],
        'Teclado': [
            ('HyperX Alloy Origins Core',  'Mecanico / TKL / RGB',         75),
            ('Logitech G413 SE',           'Mecanico / Tactil / Aluminio', 55),
            ('Razer BlackWidow V3 TKL',    'Mecanico / RGB / TKL',         90),
        ],
        'Mouse': [
            ('Logitech G502 Hero',         'Cableado / HERO 25K',          45),
            ('Razer DeathAdder V2',        'Cableado / Focus+ / 20K DPI',  50),
            ('SteelSeries Rival 3',        'Cableado / TrueMove Core',     35),
        ],
    },

    'Baja': {
        'CPU': [
            ('Intel Core i3-12100F',       '4 nucleos / 4.3 GHz',          90),
            ('AMD Ryzen 5 5500',           '6 nucleos / 4.2 GHz Turbo',    90),
            ('Intel Core i5-12400F',       '6 nucleos / 4.4 GHz',         130),
        ],
        'GPU': [
            ('NVIDIA GTX 1650 4 GB',       '4 GB GDDR6 / 1080p',          140),
            ('AMD Radeon RX 6500 XT',      '4 GB GDDR6 / PCIe 4.0',       120),
            ('NVIDIA RTX 3050 8 GB',       '8 GB GDDR6 / DLSS 2',         220),
        ],
        'Motherboard': [
            ('Gigabyte H610M S2H',         'LGA1700 / Micro-ATX / DDR4',   75),
            ('MSI PRO H610M-G',            'LGA1700 / Micro-ATX / DDR4',   80),
            ('ASRock B660M-HDV',           'LGA1700 / Micro-ATX / DDR4',   85),
        ],
        'RAM': [
            ('8 GB DDR4 Kingston',         '3200 MHz / 1x8 GB',            22),
            ('16 GB DDR4 Kingston Fury',   '3200 MHz / 2x8 GB',            38),
            ('16 GB DDR4 Corsair Vengeance','3600 MHz / 2x8 GB',           42),
        ],
        'SSD': [
            ('Kingston NV2 256 GB',        'PCIe Gen3 / 3000 MB/s',        22),
            ('Crucial BX500 480 GB',       'SATA III / 540 MB/s',          30),
            ('WD Green 480 GB',            'SATA III / 545 MB/s',          32),
        ],
        'HDD': [
            ('Seagate Barracuda 1 TB',     '7200 RPM / SATA III',          38),
            ('WD Blue 1 TB',               '7200 RPM / SATA III',          40),
            ('Toshiba DT02ABA200 2 TB',    '5400 RPM / SATA III',          50),
        ],
        'PSU': [
            ('EVGA 450W BR',               '450 W / 80+ Bronze',           38),
            ('Thermaltake Smart 500W',     '500 W / 80+ White',            35),
            ('Cooler Master MWE 550W',     '550 W / 80+ White',            45),
        ],
        'Cooler': [
            ('Cooler Stock Intel',         'Ventilador de fabrica',          0),
            ('Cooler Master Hyper 212',    'Torre Simple / 150W TDP',      30),
            ('DeepCool AG300',             'Torre Simple / 150W TDP',      22),
        ],
        'Chasis': [
            ('Thermaltake V100',           'ATX / Torre Mid / Acrilico',   35),
            ('Cougar MX330-G Air',         'ATX / Mesh Frontal',           45),
            ('Aerocool PGS-A Glam',        'ATX / Panel Acrilico',         40),
        ],
        'Monitor': [
            ('Acer KA222Q 21.5"',          'FHD / 75 Hz / VA',             75),
            ('AOC 22B2AM 21.5"',           'FHD / 75 Hz / VA',             70),
            ('HP V22e G5 21.5"',           'FHD / 75 Hz / IPS',            80),
        ],
        'Teclado': [
            ('Logitech K120',              'Membrana / USB / 104 teclas',  12),
            ('Redragon K503',              'Membrana / RGB / USB',         20),
            ('HyperX Alloy Core RGB',      'Membrana / RGB / USB',         30),
        ],
        'Mouse': [
            ('Logitech B100',              'Cableado / Optico / 800 DPI',   8),
            ('Redragon M602',              'Cableado / RGB / 7200 DPI',    15),
            ('Logitech G203 Lightsync',    'Cableado / 8K DPI',            25),
        ],
    },
}

ORDEN = ['CPU', 'GPU', 'Motherboard', 'RAM', 'SSD', 'HDD',
         'PSU', 'Cooler', 'Chasis', 'Monitor', 'Teclado', 'Mouse']

ETIQUETAS = {
    'CPU': 'CPU ', 'GPU': 'GPU ', 'Motherboard': 'MOBO',
    'RAM': 'RAM ', 'SSD': 'SSD ', 'HDD': 'HDD ',
    'PSU': 'PSU ', 'Cooler': 'COOL', 'Chasis': 'CASE',
    'Monitor': 'MON ', 'Teclado': 'KEYB', 'Mouse': 'MOUS',
}

# anchos de cada columna en la tabla
W_TIPO   = 6
W_NOMBRE = 26
W_DESC   = 28
W_PRECIO = 11

# ====================
# PATRON COMPOSITE
# ====================
class ComponenteHardware(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def obtener_precio(self):
        pass

    @abstractmethod
    def mostrar_detalles(self):
        pass


# hoja del composite - un solo producto
class Producto(ComponenteHardware):
    def __init__(self, nombre, descripcion, precio, tipo, gama):
        super().__init__(nombre)
        self.descripcion = descripcion
        self.precio = precio
        self.tipo = tipo
        self.gama = gama

    def obtener_precio(self):
        return self.precio

    def mostrar_detalles(self):
        # esto lo hace la computadora, no el producto solo
        pass


# contenedor del composite - agrupa todos los productos
class Computadora(ComponenteHardware):
    def __init__(self, nombre, gama):
        super().__init__(nombre)
        self.gama = gama
        self.componentes = []   # lista de productos agregados

    def agregar(self, comp):
        self.componentes.append(comp)
        return self

    def obtener_precio(self):
        total = 0
        for c in self.componentes:
            total += c.obtener_precio()
        return total

    def mostrar_detalles(self):
        col = COLOR_GAMA[self.gama]
        borde = col['borde']
        ancho_total = W_TIPO + W_NOMBRE + W_DESC + W_PRECIO + 11  # 11 = separadores

        # linea de separacion horizontal
        def linea(izq, med, der):
            seg1 = borde + izq + '═' * (W_TIPO   + 2) + RESET
            seg2 = borde + med + '═' * (W_NOMBRE + 2) + RESET
            seg3 = borde + med + '═' * (W_DESC   + 2) + RESET
            seg4 = borde + med + '═' * (W_PRECIO + 2) + der + RESET
            return seg1 + seg2 + seg3 + seg4

        def celda(texto, ancho, color=''):
            contenido = color + rellenar(texto, ancho) + (RESET if color else '')
            return borde + '║' + RESET + ' ' + contenido + ' '

        def fila(tipo, nombre, desc, precio, ct='', cn='', cd='', cp=''):
            return (celda(tipo,   W_TIPO,   ct)
                  + celda(nombre, W_NOMBRE, cn)
                  + celda(desc,   W_DESC,   cd)
                  + celda(precio, W_PRECIO, cp)
                  + borde + '║' + RESET)

        # borde de arriba
        print()
        print(borde + '╔' + '═' * (ancho_total) + '╗' + RESET)

        # titulo con la gama y nombre del build
        etiqueta = col['tag'] + ' ' + self.gama.upper() + ' ' + RESET
        titulo   = BOLD + borde + '  ' + self.nombre + '  ' + RESET
        espacio  = ancho_total - longitud_visible(' ' + self.gama.upper() + ' ') - longitud_visible('  ' + self.nombre + '  ') - 2
        print(borde + '║' + RESET + ' ' + etiqueta + ' ' * max(espacio, 1) + titulo + borde + '║' + RESET)

        # encabezados
        print(linea('╠', '╬', '╣'))
        print(fila('TIPO', 'COMPONENTE', 'ESPECIFICACION', 'PRECIO',
                   BOLD + GRIS, BOLD + GRIS, BOLD + GRIS, BOLD + GRIS))
        print(linea('╠', '╬', '╣'))

        # filas de productos
        for i, prod in enumerate(self.componentes):
            color_fila = BLANCO if i % 2 == 0 else GRIS
            etiq = ETIQUETAS.get(prod.tipo, prod.tipo[:4])

            if prod.precio == 0:
                precio_str = 'INCL.'
                color_p = DIM + GRIS
            else:
                precio_str = f'${prod.precio:>7,.0f}'
                color_p = col['precio']

            print(fila(etiq, prod.nombre, prod.descripcion, precio_str,
                       BOLD + borde, color_fila, DIM + GRIS, color_p))

        # total
        print(linea('╠', '╬', '╣'))
        total_str = f'${self.obtener_precio():,.0f} USD'
        etiq_total = 'TOTAL CONFIGURACION:'
        espacio_total = ancho_total - len(total_str) - 3
        linea_total = BOLD + f' {etiq_total}'.ljust(espacio_total) + RESET + col['tag'] + BOLD + f' {total_str} ' + RESET
        print(borde + '║' + RESET + linea_total + borde + '║' + RESET)

        # borde de abajo
        print(borde + '╚' + '═' * (ancho_total) + '╝' + RESET)


# ====================
# FUNCIONES DEL MENU
# ====================

def pedir_gama():
    print(f'\n{BOLD}{BLANCO}  Elige la gama:{RESET}')
    print(f'{GRIS}  {"─" * 46}{RESET}')
    print(f'  {AMARI}{BOLD}[1]{RESET}  {AMARI}{BOLD}Alta{RESET}   {DIM}Workstation / Gaming extremo{RESET}')
    print(f'  {CYAN}{BOLD}[2]{RESET}  {CYAN}{BOLD}Media{RESET}  {DIM}Gaming / Productividad{RESET}')
    print(f'  {BLANCO}{BOLD}[3]{RESET}  {BLANCO}{BOLD}Baja{RESET}   {DIM}Ofimática / Uso basico{RESET}')
    print(f'{GRIS}  {"─" * 46}{RESET}')

    while True:
        try:
            op = input(f'{BOLD}{VERDE}  Opcion: {RESET}').strip()
        except (EOFError, KeyboardInterrupt):
            return ''
        if op == '1': return 'Alta'
        if op == '2': return 'Media'
        if op == '3': return 'Baja'
        print(f'{ROJO}  Solo 1, 2 o 3.{RESET}')


def elegir_componentes(gama):
    col = COLOR_GAMA[gama]
    productos_elegidos = []
    total_cats = len(ORDEN)

    for num, cat in enumerate(ORDEN, 1):
        opciones = CATALOGO[gama][cat]

        print(f'\n  {col["borde"]}{BOLD}[{num}/{total_cats}]  {cat}{RESET}')
        print(f'{GRIS}  {"─" * 56}{RESET}')

        for i, (nombre, desc, precio) in enumerate(opciones, 1):
            p = 'Incluido' if precio == 0 else f'${precio:,.0f}'
            print(f'  {col["borde"]}{BOLD}[{i}]{RESET}  {BLANCO}{nombre:<28}{RESET}  {DIM}{desc:<30}{RESET}  {col["precio"]}{p}{RESET}')

        print(f'{GRIS}  {"─" * 56}{RESET}')

        # pedir la eleccion del usuario
        while True:
            try:
                op = input(f'{col["entrada"]}{BOLD}  Eleccion [1/2/3]: {RESET}').strip()
            except (EOFError, KeyboardInterrupt):
                print(f'\n{ROJO}  Cancelado.{RESET}')
                return []

            if op in ('1', '2', '3'):
                nombre, desc, precio = opciones[int(op) - 1]
                nuevo = Producto(nombre, desc, precio, cat, gama)
                productos_elegidos.append(nuevo)
                p = 'Incluido' if precio == 0 else f'${precio:,.0f}'
                print(f'{VERDE}  > {nombre}  {DIM}{p}{RESET}')
                break
            print(f'{ROJO}  Escribe 1, 2 o 3.{RESET}')

    return productos_elegidos


def armar_pc():
    gama = pedir_gama()
    if not gama:
        return

    col = COLOR_GAMA[gama]
    print(f'\n  {col["tag"]} {gama.upper()} {RESET}  {DIM}Elige un componente por cada categoria.{RESET}')

    elegidos = elegir_componentes(gama)
    if not elegidos:
        return

    try:
        nombre = input(f'\n{BOLD}{VERDE}  Nombre de tu build (ENTER = "MI PC"): {RESET}').strip()
    except (EOFError, KeyboardInterrupt):
        nombre = ''

    if not nombre:
        nombre = 'MI PC'

    # crear el objeto computadora y agregarle los productos
    mi_pc = Computadora(nombre, gama)
    for prod in elegidos:
        mi_pc.agregar(prod)

    mi_pc.mostrar_detalles()


# ====================
# INICIO DEL PROGRAMA
# ====================
def main():
    # banner de bienvenida
    print(BOLD + CYAN)
    print('  ╔══════════════════════════════════════════════════╗')
    print('  ║  SERNA HARDWARE  --  PC BUILDER                 ║')
    print('  ╚══════════════════════════════════════════════════╝')
    print(RESET)

    while True:
        print(f'  {BOLD}{BLANCO}[1]{RESET}  Armar una PC')
        print(f'  {BOLD}{BLANCO}[0]{RESET}  {DIM}Salir{RESET}')

        try:
            op = input(f'\n{BOLD}{VERDE}  Opcion: {RESET}').strip()
        except (EOFError, KeyboardInterrupt):
            op = '0'

        if op == '0':
            print(f'\n{DIM}  Hasta luego.\n{RESET}')
            break
        elif op == '1':
            armar_pc()
        else:
            print(f'{ROJO}  Esa opcion no existe.{RESET}')


if __name__ == '__main__':
    main()
