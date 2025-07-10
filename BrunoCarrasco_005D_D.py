import os

class Modelo:
    def __init__(self, modelo, marca, pantalla, RAM, disco, GB, procesador, video, precio, stock):
        self.modelo = modelo
        self.marca = marca
        self.pantalla = pantalla
        self.RAM = RAM
        self.disco = disco
        self.GB = GB
        self.procesador = procesador
        self.video = video
        self.precio = precio
        self.stock = stock

productos = [
    Modelo('8475HD','HP', 15.6, 8, 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050', 387990, 10),
    Modelo('2175HD','Acer', 14, 4, 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050', 327990, 4),
    Modelo('JjfFHD','Asus', 14, 16, 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti', 424990, 1),
    Modelo('fgdxFHD','HP', 15.6, 8, 'DD', '1T', 'Intel Core i3', 'integrada', 664990, 21),
    Modelo('GF75HD','Asus', 15.6, 8, 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050', 749990, 2),
    Modelo('123FHD','Acer', 14, 6, 'DD', '1T', 'AMD Ryzen 5', 'integrada', 290890, 32),
    Modelo('342FHD','Acer', 15.6, 8, 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050', 444990, 7),
    Modelo('UWU131HD','Dell', 15.6, 8, 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050', 349990, 1) 
    ]

marcas = []
marcasLower = []
for pc in productos:
    if pc.marca not in marcas:
        marcas.append(pc.marca)

for marca in marcas:
    marcasLower.append(marca.lower())


def clear():
    os.system('cls')

def menuPrincipal():
    global productos
    global marcas
    clear()
    print(
        '***MENU PRINCIPAL***\n\n'
        '1. Stock marca\n'
        '2. Busqueda por RAM y precio\n'
        '3. Eliminar producto\n'
        '4. Salir\n'
    )
    r = input()
    match r:
        case '1':
            while True:
                clear()
                print('Ingrese marca a consultar\nMarcas Encontradas: ')
                for marca in marcas:
                    print(f'- {marca}')
                r = input()
                if r.lower() in marcasLower:
                    stock_marca(r.lower())
                    break
        case '2':
            while True:
                clear()
                mn = input('Ingrese RAM minima: ')
                mx = input('Ingrese RAM máxima: ')
                presupuesto = input('Ingrese precio: ')

                if not mn.isdigit() or not mx.isdigit() or not presupuesto.isdigit():
                    print('Debe ingresar valores enteros!!')
                    print("presione 'enter' para reintentar")
                    input()
                else:
                    busqueda_ram_precio(int(mn), int(mx), int(presupuesto))
                    break
        case '3':
            tmp()

        case '4':
            clear()
            print('Programa finalizado')
            quit()
        case _:
            menuPrincipal()

def stock_marca(marca):
    global productos
    print(f"Productos marca '{marca}':\n")
    for pc in productos:
        if pc.marca.lower() == marca:
            print(f'PC modelo: {pc.modelo}\nPrecio: {pc.precio}\n{pc.stock} en stock\n')

    print("\nPresione 'enter' para volver")
    input()
    menuPrincipal()

def busqueda_ram_precio(ram_min, ram_max, precio):
    global productos
    i = 0
    for pc in productos:
        if pc.RAM >= ram_min and pc.RAM <= ram_max and pc.precio <= precio:
            print(f'{pc.modelo}, {pc.marca}, {pc.pantalla}, {pc.RAM}GB, {pc.disco}, {pc.GB}, {pc.procesador}, {pc.video}')
            i += 1
    if i == 0:
        print('No hay productos encontrados :(')
    print("presione 'enter' para volver")
    input()
    menuPrincipal

def tmp():
    global productos
    lista = []
    clear()
    print('Ingrese modelo del producto a eliminar')
    print('Productos encontrados')
    for pc in productos:
        print(f'- {pc.modelo}')
        lista.append(pc.modelo.lower())
    r = input()
    eliminar_producto(r)

def eliminar_producto(modelo):
    clear()
    global productos
    lista = []
    for pc in productos:
        lista.append(pc.modelo.lower())
    if modelo not in lista:
        print('El modelo no existe!!!')
        print("\npresione 'enter' para volver")
        tmp()
    else:
        i = 0
        for pc in productos:
            if modelo.lower() == pc.modelo.lower():
                productos.remove(i)
                print('Producto eliminado!!')
            i += 1
            input()
            menuPrincipal()


menuPrincipal()

