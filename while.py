personas = int(input("Introduzca la cantidad de personas: "))
n = 0
while personas >= n :
    n += 1
    SSD = int(input("SSD (TB): 1|2|5 "))
    RAM = int(input("RAM (GB): 12|32|64 "))
    GRAPHIC_CARD = int(input("Graphic Card (GTX): 3090|5090|9090 "))
    PROCESADOR = int(input("PROCESADOR (i): 5|7|9 "))
    MOTHERBOARD = input("MOTHERBOARD (ATX): MICRO|MACRO|BIG ")
    print ("Persona ",n)(":")
    print ("SSD: ",SSD)("RAM: ",RAM)("Tarjeta gráfica: ",GRAPHIC_CARD)("Procesador: ",PROCESADOR)("Placa madre: ",MOTHERBOARD)
    print("RAM: ",RAM)
    print("Tarjeta gráfica: ",GRAPHIC_CARD)
    print("Procesador: ",PROCESADOR)
    print("Placa madre: ",MOTHERBOARD)
    
