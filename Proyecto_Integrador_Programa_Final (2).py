#Proyecto Integrador
#Programa de la tienda
#Equipo:
#Francisco Javier Olea Gándara-A00227807
#Jesús Ramón Zazueta Ubiarco-A00227809
#Alán Tapia Parada-A000227840
print("¡Bienvenido a la tienda RAF!")
while True:
    myfile=open("Inventario.txt","r")
    inv=myfile.readlines()
    
    #Separa la lista de inventario con comas para tener muchos elementos en lugar de uno solo.
    invent=[]
    for v in inv:
        reg=v.split(",")
        invent.append(reg)

    inventari=invent[0]
    
    #Función para crear el inventario total
    def crear_inventario(x):
        s=[]
        for i in range (0,len(inventari),4):
            s.append(inventari[i:i+4])
        return(s)
    iniciar=0
    inventario=crear_inventario(iniciar)
    myfile.close()
    
    #Lista de artículos por departamento
    casa=[inventario[0:5]]
    electronica=[inventario[5:10]]
    farmacia=[inventario[10:15]]
    alcohol=[inventario[15:20]]
    
    ventas=open("Ventas.txt","r")
    v=ventas.readlines()

    ven=[]
    for v in v:
        reg=v.split(",")
        ven.append(reg)

    venta=ven[0]

    #Función para lista de ventas totales por Vendedor, Artículo y Cantidad.
    def crear_ventas(x):
        h=[]
        for i in range (0,len(venta),3):
            h.append(venta[i:i+3])
        return(h)
    comenzar=0
    lista_ventas=crear_ventas(comenzar)
    ventas.close()

    #Lista de artículos por departamento
    ventas_jose=lista_ventas[0:5]
    ventas_alan=lista_ventas[5:10]
    ventas_salvador=lista_ventas[10:15]
    ventas_venustiano=lista_ventas[15:20]
    
    #Variables de Cantidad de cada Artículo
    cant_nueva_camarosa=int(casa[0][0][3])
    cant_nueva_nutribullet=int(casa[0][1][3])
    cant_nueva_estante=int(casa[0][2][3])
    cant_nueva_buro=int(casa[0][3][3])
    cant_nueva_lampara=int(casa[0][4][3])
    cant_nueva_xbox=int(electronica[0][0][3])
    cant_nueva_ps4=int(electronica[0][1][3])
    cant_nueva_iphone=int(electronica[0][2][3])
    cant_nueva_camara=int(electronica[0][3][3])
    cant_nueva_switch=int(electronica[0][4][3])
    cant_nueva_paracetamol=int(farmacia[0][0][3])
    cant_nueva_peptobismol=int(farmacia[0][1][3])
    cant_nueva_treda=int(farmacia[0][2][3])
    cant_nueva_vick=int(farmacia[0][3][3])
    cant_nueva_condones=int(farmacia[0][4][3])
    cant_nueva_smirnoff=int(alcohol[0][0][3])
    cant_nueva_josecuervo=int(alcohol[0][1][3])
    cant_nueva_tecate=int(alcohol[0][2][3])
    cant_nueva_merlot=int(alcohol[0][3][3])
    cant_nueva_moet=int(alcohol[0][4][3])
    
    #Variables de cantidad de ventas por vendedor.
    ventas_jose_camarosa=int(ventas_jose[0][2])
    ventas_jose_nutribullet=int(ventas_jose[1][2])
    ventas_jose_estante=int(ventas_jose[2][2])
    ventas_jose_buro=int(ventas_jose[3][2])
    ventas_jose_lampara=int(ventas_jose[4][2])
    ventas_alan_xbox=int(ventas_alan[0][2])
    ventas_alan_ps4=int(ventas_alan[1][2])
    ventas_alan_iphone=int(ventas_alan[2][2])
    ventas_alan_camara=int(ventas_alan[3][2])
    ventas_alan_switch=int(ventas_alan[4][2])
    ventas_salvador_paracetamol=int(ventas_salvador[0][2])
    ventas_salvador_peptobismol=int(ventas_salvador[1][2])
    ventas_salvador_treda=int(ventas_salvador[2][2])
    ventas_salvador_vick=int(ventas_salvador[3][2])
    ventas_salvador_condones=int(ventas_salvador[4][2])
    ventas_venustiano_smirnoff=int(ventas_venustiano[0][2])
    ventas_venustiano_josecuervo=int(ventas_venustiano[1][2])
    ventas_venustiano_tecate=int(ventas_venustiano[2][2])
    ventas_venustiano_merlot=int(ventas_venustiano[3][2])
    ventas_venustiano_moet=int(ventas_venustiano[4][2])
    
    #Se le dan las opciones al usuario de qué quiere hacer.
    print("Escribe 'comprar' para comprar un artículo")
    print("Escribe 'registrar' para registrar llegada de artículo")
    print("Escribe 'inventario' para consultar el inventario")
    print("Escribe 'ventas' para consultar las ventas")
    print("Escribe 'ventas vendedor' para reporte de ventas por vendedor")
    print("Escribe 'ventas articulo' para reporte de ventas por artículo")
    n=input("¿Qué quieres hacer? ")
    #Según la opción que elija el usuario, se le lleva a la opción mediante un if.
    if n.lower()=="comprar":
        print("Hola, ¿a qué departamento quiere ir?")
        print("Casa, Electrónica, Farmacia o Alcohol")
        dep=input("Departamento: ")
        #En esta función se recibe  el dato de la cantidad del artículo antes de la venta y la cantidad que se quiere comprar.
        #Después toma ambos datos y los resta, para obtener la cantidad que queda de ese artículo.
        def venta(cantidad_articulo,cant_nueva):
                cant_nueva=cant_nueva-cantidad_articulo
                return cant_nueva
        #Dependiendo de que escriba el usuario, lo lleva a dicho departamento.
        #Por ejemplo al escribir 'casa', va al departamento de casa.
        if dep.lower()=="casa":
            print("Buen día, soy José, encargado del departamento de casa")
            print("nuestros artículos son: ")
            for articulo in casa:
                #Imprime los artículos disponibles en el departamento y su cantidad.
                print(articulo[0][3],articulo[0][2]+" disponibles.")
                print(articulo[1][3],articulo[1][2]+" disponibles.")
                print(articulo[2][3],articulo[2][2]+" disponibles.")
                print(articulo[3][3],articulo[3][2]+" disponibles.")
                print(articulo[4][3],articulo[4][2]+" disponibles.")
            #Se le pregunta al usuario qué comprará, y se hace lower en los if para que todo sea minúscula y evitar errores en el código.
            articulo_comprar=input("¿Qué quiere comprar? ")
            cantidad_articulo=int(input("¿Cuántas quiere? "))
            if articulo_comprar.lower()=="cama rosa":
                #Si no quedan artículos, envia un mensaje de que se acabaron.
                if int(cant_nueva_camarosa)==0:
                    print("Lo siento, se nos acabaron.")
                #Si quedan suficientes artículos en la tienda, se ejecuta la venta.
                #Por medio de la función (venta) se resta la cantidad comprada a la total.
                #Al hacerse la compra, se le suma la cantidad que se compro a las ventas del vendedor de el departamento.
                elif cantidad_articulo<=cant_nueva_camarosa:
                    cant_nueva_camarosa=venta(cantidad_articulo,cant_nueva_camarosa)
                    ventas_jose_camarosa=ventas_jose_camarosa+cantidad_articulo
                    print("Está bien, gracias por su compra")
                #Si la cantidad que pide el usuario es mayor a la disponible, se le notifica que no alcanzan, y se le dice la cantidad en existencia.
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_camarosa:
                    print("Lo siento, sólo nos quedan",cant_nueva_camarosa)
            elif articulo_comprar.lower()=="nutribullet":
                if int(cant_nueva_nutribullet)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_nutribullet:
                    cant_nueva_nutribullet=venta(cantidad_articulo,cant_nueva_nutribullet)
                    ventas_jose_nutribullet=ventas_jose_nutribullet+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_nutribullet:
                    print("Lo siento, sólo nos quedan",cant_nueva_nutribullet)
            elif articulo_comprar.lower()=="estante":
                if int(cant_nueva_estante)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_estante:
                    cant_nueva_estante=venta(cantidad_articulo,cant_nueva_estante)
                    ventas_jose_estante=ventas_jose_estante+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_estante:
                    print("Lo siento, sólo nos quedan",cant_nueva_estante)        
            elif articulo_comprar.lower()=="buro":
                if int(cant_nueva_buro)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_buro:
                    cant_nueva_buro=venta(cantidad_articulo,cant_nueva_buro)
                    ventas_jose_buro=ventas_jose_buro+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_buro:
                    print("Lo siento, sólo nos quedan",cant_nueva_buro)
            elif articulo_comprar.lower()=="lampara":
                if int(cant_nueva_lampara)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_lampara:
                    cant_nueva_lampara=venta(cantidad_articulo,cant_nueva_lampara)
                    ventas_jose_lampara=ventas_jose_lampara+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_lampara:
                    print("Lo siento, sólo nos quedan",cant_nueva_lampara)
            else:
                print("No tenemos ese artículo.")
                
        #Departamento de Electrónica:
        if dep.lower()=="electronica":
            print("Buen día, soy Alan, encargado del departamento de electrónica")
            print("nuestros artículos son: ")
            for articulo in electronica:
                print(articulo[0][3],articulo[0][2]+" disponibles.")
                print(articulo[1][3],articulo[1][2]+" disponibles.")
                print(articulo[2][3],articulo[2][2]+" disponibles.")
                print(articulo[3][3],articulo[3][2]+" disponibles.")
                print(articulo[4][3],articulo[4][2]+" disponibles.")
            articulo_comprar=input("¿Qué quiere comprar? ")
            cantidad_articulo=int(input("¿Cuántas quiere? "))
            if articulo_comprar.lower()=="xbox one x":
                if int(cant_nueva_xbox)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_xbox:
                    cant_nueva_xbox=venta(cantidad_articulo,cant_nueva_xbox)
                    ventas_alan_xbox=ventas_alan_xbox+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_xbox:
                    print("Lo siento, sólo nos quedan",cant_nueva_xbox)   
            elif articulo_comprar.lower()=="play station 4":
                if int(cant_nueva_ps4)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_ps4:
                    cant_nueva_ps4=venta(cantidad_articulo,cant_nueva_ps4)
                    ventas_alan_ps4=ventas_alan_ps4+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_ps4:
                    print("Lo siento, sólo nos quedan",cant_nueva_ps4)
            elif articulo_comprar.lower()=="iphone 12":
                if int(cant_nueva_iphone)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_iphone:
                    cant_nueva_iphone=venta(cantidad_articulo,cant_nueva_iphone)
                    ventas_alan_iphone=ventas_alan_iphone+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_iphone:
                    print("Lo siento, sólo nos quedan",cant_nueva_iphone)
            elif articulo_comprar.lower()=="camara":
                if int(cant_nueva_camara)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_camara:
                    cant_nueva_camara=venta(cantidad_articulo,cant_nueva_camara)
                    ventas_alan_camara=ventas_alan_camara+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_camara:
                    print("Lo siento, sólo nos quedan",cant_nueva_camara)
            elif articulo_comprar.lower()=="nintendo switch":
                if int(cant_nueva_switch)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_switch:
                    cant_nueva_switch=venta(cantidad_articulo,cant_nueva_switch)
                    ventas_alan_switch=ventas_alan_switch+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_switch:
                    print("Lo siento, sólo nos quedan",cant_nueva_switch)
            else:
                print("No tenemos ese artículo.")
                    
        #Departamento de Farmacia:
        if dep.lower()=="farmacia":
            print("Buen día, soy Salvador, encargado del departamento de farmacia")
            print("nuestros artículos son: ")
            for articulo in farmacia:
                print(articulo[0][3],articulo[0][2]+" disponibles.")
                print(articulo[1][3],articulo[1][2]+" disponibles.")
                print(articulo[2][3],articulo[2][2]+" disponibles.")
                print(articulo[3][3],articulo[3][2]+" disponibles.")
                print(articulo[4][3],articulo[4][2]+" disponibles.")
            articulo_comprar=input("¿Qué quiere comprar? ")
            cantidad_articulo=int(input("¿Cuántas quiere? "))
            if articulo_comprar.lower()=="paracetamol":
                if int(cant_nueva_paracetamol)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_paracetamol:
                    cant_nueva_paracetamol=venta(cantidad_articulo,cant_nueva_paracetamol)
                    ventas_salvador_paracetamol=ventas_salvador_paracetamol+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_paracetamol:
                    print("Lo siento, sólo nos quedan",cant_nueva_paracetamol)
            elif articulo_comprar.lower()=="peptobismol":
                if int(cant_nueva_peptobismol)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_peptobismol:
                    cant_nueva_peptobismol=venta(cantidad_articulo,cant_nueva_peptobismol)
                    ventas_salvador_peptobismol=ventas_salvador_peptobismol+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_peptobismol:
                    print("Lo siento, sólo nos quedan",cant_nueva_peptobismol)
            elif articulo_comprar.lower()=="treda":
                if int(cant_nueva_treda)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_treda:
                    cant_nueva_treda=venta(cantidad_articulo,cant_nueva_treda)
                    ventas_salvador_treda=ventas_salvador_treda+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_treda:
                    print("Lo siento, sólo nos quedan",cant_nueva_treda)
            elif articulo_comprar.lower()=="vick vaporub":
                if int(cant_nueva_vick)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_vick:
                    cant_nueva_vick=venta(cantidad_articulo,cant_nueva_vick)
                    ventas_salvador_vick=ventas_salvador_vick+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_vick:
                    print("Lo siento, sólo nos quedan",cant_nueva_vick)
            elif articulo_comprar.lower()=="condones":
                if int(cant_nueva_condones)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_condones:
                    cant_nueva_condones=venta(cantidad_articulo,cant_nueva_condones)
                    ventas_salvador_condones=ventas_salvador_condones+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_condones:
                    print("Lo siento, sólo nos quedan",cant_nueva_condones)
            else:
                print("No tenemos ese artículo.")

        #Departamento de Alcohol:
        if dep.lower()=="alcohol":
            print("Buen día, soy Venustiano, encargado del departamento de alcohol")
            print("nuestros artículos son: ")
            for articulo in alcohol:
                print(articulo[0][3],articulo[0][2]+" disponibles.")
                print(articulo[1][3],articulo[1][2]+" disponibles.")
                print(articulo[2][3],articulo[2][2]+" disponibles.")
                print(articulo[3][3],articulo[3][2]+" disponibles.")
                print(articulo[4][3],articulo[4][2]+" disponibles.")
            articulo_comprar=input("¿Qué quiere comprar? ")
            cantidad_articulo=int(input("¿Cuántas quiere? "))
            if articulo_comprar.lower()=="smirnoff tamarindo":
                if int(cant_nueva_smirnoff)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_smirnoff:
                    cant_nueva_smirnoff=venta(cantidad_articulo,cant_nueva_smirnoff)
                    ventas_venustiano_smirnoff=ventas_venustiano_smirnoff+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_smirnoff:
                    print("Lo siento, sólo nos quedan",cant_nueva_smirnoff)
            elif articulo_comprar.lower()=="jose cuervo":
                if int(cant_nueva_josecuervo)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_josecuervo:
                    cant_nueva_josecuervo=venta(cantidad_articulo,cant_nueva_josecuervo)
                    ventas_venustiano_josecuervo=ventas_venustiano_josecuervo+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_josecuervo:
                    print("Lo siento, sólo nos quedan",cant_nueva_josecuervo)
            elif articulo_comprar.lower()=="tecate":
                if int(cant_nueva_tecate)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_tecate:
                    cant_nueva_tecate=venta(cantidad_articulo,cant_nueva_tecate)
                    ventas_venustiano_tecate=ventas_venustiano_tecate+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_tecate:
                    print("Lo siento, sólo nos quedan",cant_nueva_tecate)
            elif articulo_comprar.lower()=="merlot":
                if int(cant_nueva_merlot)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_merlot:
                    cant_nueva_merlot=venta(cantidad_articulo,cant_nueva_merlot)
                    ventas_venustiano_merlot=ventas_venustiano_merlot+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_merlot:
                    print("Lo siento, sólo nos quedan",cant_nueva_merlot)
            elif articulo_comprar.lower()=="moet":
                if int(cant_nueva_moet)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_moet:
                    cant_nueva_moet=venta(cantidad_articulo,cant_nueva_moet)
                    ventas_venustiano_moet=ventas_venustiano_moet+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_moet:
                    print("Lo siento, sólo nos quedan",cant_nueva_moet)
            else:
                print("No tenemos ese artículo.")

    #Registro de artículos nuevos que llegan a la tienda.
    if n.lower()=="registrar":
        print("¿De qué departamento es su artículo?")
        print("Casa, Electrónica, Farmacia o Alcohol")
        dep=input("Departamento: ")
        #Función donde recibe la cantidad del artículo inicial y la que se quiere agregar
        #Se suman las dos y luego regresa la cantidad total a una cadena de if, para ver
        #a que variable se le debe de agregar (artículo que se agregó).
        def registrar(cant_llegada,cant_nueva):
                cant_nueva=cant_nueva+cant_llegada
                return cant_nueva
        #Se lleva al departamento que corresponda dependiendo de que escribe el usuario.
        if dep.lower()=="casa":
            print("Buen día, soy José, encargado del departamento de casa")
            art_llegada=input("¿Qué artículo trae para nosotros? ")
            cant_llegada=int(input("¿Cuántos trae? "))
            #Por medio de la función (registrar) se suma la cantidad de artículos que trajo el repartidor,
            #más la cantidad de artículos que ya hay en el inventario.
            if art_llegada.lower()=="cama rosa":
                cant_nueva_camarosa=registrar(cant_llegada,cant_nueva_camarosa)
            if art_llegada.lower()=="nutribullet":
                cant_nueva_nutribullet=registrar(cant_llegada,cant_nueva_nutribullet)
            if art_llegada.lower()=="estante":
                cant_nueva_estante=registrar(cant_llegada,cant_nueva_estante)
            if art_llegada.lower()=="buro":
                cant_nueva_buro=registrar(cant_llegada,cant_nueva_buro)
            if art_llegada.lower()=="lampara":
                cant_nueva_lampara=registrar(cant_llegada,cant_nueva_lampara)
        elif dep.lower()=="electronica":
            print("Buen día, soy Alan, encargado del departamento de casa")
            art_llegada=input("¿Qué artículo trae para nosotros? ")
            cant_llegada=int(input("¿Cuántos trae? "))
            if art_llegada.lower()=="xbox one x":
                cant_nueva_xbox=registrar(cant_llegada,cant_nueva_xbox)
            if art_llegada.lower()=="play station 4":
                cant_nueva_ps4=registrar(cant_llegada,cant_nueva_ps4)
            if art_llegada.lower()=="iphone 12":
                cant_nueva_iphone=registrar(cant_llegada,cant_nueva_iphone)
            if art_llegada.lower()=="camara":
                cant_nueva_camara=registrar(cant_llegada,cant_nueva_camara)
            if art_llegada.lower()=="nintendo switch":
                cant_nueva_switch=registrar(cant_llegada,cant_nueva_switch) 
        elif dep.lower()=="farmacia":
            print("Buen día, soy Salvador, encargado del departamento de casa")
            art_llegada=input("¿Qué artículo trae para nosotros? ")
            cant_llegada=int(input("¿Cuántos trae? "))
            if art_llegada.lower()=="paracetamol":
                cant_nueva_paracetamol=registrar(cant_llegada,cant_nueva_paracetamol)
            if art_llegada.lower()=="peptobismol":
                cant_nueva_peptobismol=registrar(cant_llegada,cant_nueva_peptobismol)
            if art_llegada.lower()=="treda":
                cant_nueva_treda=registrar(cant_llegada,cant_nueva_treda)
            if art_llegada.lower()=="vick vaporub":
                cant_nueva_vick=registrar(cant_llegada,cant_nueva_vick)
            if art_llegada.lower()=="condones":
                cant_nueva_condones=registrar(cant_llegada,cant_nueva_condones)
        elif dep.lower()=="alcohol":
            print("Buen día, soy Venustiano, encargado del departamento de casa")
            art_llegada=input("¿Qué artículo trae para nosotros? ")
            cant_llegada=int(input("¿Cuántos trae? "))
            if art_llegada.lower()=="smirnoff tamarindo":
                cant_nueva_smirnoff=registrar(cant_llegada,cant_nueva_smirnoff)
            if art_llegada.lower()=="jose cuervo":
                cant_nueva_josecuervo=registrar(cant_llegada,cant_nueva_josecuervo)
            if art_llegada.lower()=="tecate":
                cant_nueva_tecate=registrar(cant_llegada,cant_nueva_tecate)
            if art_llegada.lower()=="merlot":
                cant_nueva_merlot=registrar(cant_llegada,cant_nueva_merlot)
            if art_llegada.lower()=="moet":
                cant_nueva_moet=registrar(cant_llegada,cant_nueva_moet)
        print("Gracias, la entrega quedó registrada.")
        
    #Consulta el inventario
    if n.lower()=="inventario":
        #Se imprimen las posiciones de cada artículo en la lista de cada departamento
        print("            INVENTARIO        ")
        print("Dpto."+"    "+"Modelo"+"    "+"Artículo"+"    "+"Cantidad")
        print(casa[0][0])
        print(casa[0][1])
        print(casa[0][2])
        print(casa[0][3])
        print(casa[0][4])
        print(electronica[0][0])
        print(electronica[0][1])
        print(electronica[0][2])
        print(electronica[0][3])
        print(electronica[0][4])
        print(farmacia[0][0])
        print(farmacia[0][1])
        print(farmacia[0][2])
        print(farmacia[0][3])
        print(farmacia[0][4])
        print(alcohol[0][0])
        print(alcohol[0][1])
        print(alcohol[0][2])
        print(alcohol[0][3])
        print(alcohol[0][4])
        
        
    if n.lower()=="ventas":
        print("            VENTAS        ")
        print("Vendedor"+"    "+"Artículo"+"    "+"Ventas")
        #Se imprimen las listas de cada vendedor por elemento,
        #Estas sublistas contienen el nombre del vendedor, el artículo, y la cantidad de ventas de ese artículo.
        print(ventas_jose[0])
        print(ventas_jose[1])
        print(ventas_jose[2])
        print(ventas_jose[3])
        print(ventas_jose[4])
        print(ventas_alan[0])
        print(ventas_alan[1])
        print(ventas_alan[2])
        print(ventas_alan[3])
        print(ventas_alan[4])
        print(ventas_salvador[0])
        print(ventas_salvador[1])
        print(ventas_salvador[2])
        print(ventas_salvador[3])
        print(ventas_salvador[4])
        print(ventas_venustiano[0])
        print(ventas_venustiano[1])
        print(ventas_venustiano[2])
        print(ventas_venustiano[3])
        print(ventas_venustiano[4])
        
    if n.lower()=="ventas vendedor":
        #Función que toma las variables de ventas para cada producto de un departamento y las suma.
        #Con esto, se pueden ver las ventas totales que ha hecho cada vendedor.
        def ventas_vendedor(ventas_prod_1,ventas_prod_2,ventas_prod_3,ventas_prod_4,ventas_prod_5):
            ventas_vendedor_totales=ventas_prod_1+ventas_prod_2+ventas_prod_3+ventas_prod_4+ventas_prod_5
            return ventas_vendedor_totales
        print("      VENTAS POR VENDEDOR       ")
        #Se corre la función (ventas_vendedor) dando los valores de ventas de cada producto de un departamento y se asigna el resultado a su encargado.
        totales_jose=ventas_vendedor(ventas_jose_camarosa,ventas_jose_nutribullet,ventas_jose_estante,ventas_jose_buro,ventas_jose_lampara)
        print("José ha vendido "+str(totales_jose)+" artículos en total.")
        totales_alan=ventas_vendedor(ventas_alan_xbox,ventas_alan_ps4,ventas_alan_iphone,ventas_alan_camara,ventas_alan_switch)
        print("Alan ha vendido "+str(totales_alan)+" artículos en total.")
        totales_salvador=ventas_vendedor(ventas_salvador_paracetamol,ventas_salvador_peptobismol,ventas_salvador_treda,ventas_salvador_vick,ventas_salvador_condones)
        print("Salvador ha vendido "+str(totales_salvador)+" artículos en total.")
        totales_venustiano=ventas_vendedor(ventas_venustiano_smirnoff,ventas_venustiano_josecuervo,ventas_venustiano_tecate,ventas_venustiano_merlot,ventas_venustiano_moet)
        print("Venustiano ha vendido "+str(totales_venustiano)+" artículos en total.")
        
    if n.lower()=="ventas articulo":
        print("    VENTAS POR ARTÍCULO       ")
        #Se imprime una cadena de strings en la que el valor de en medio es igual a las ventas
        #que ha habido por cada artículo.
        print("Se han vendido "+str(ventas_jose_camarosa)+" camas rosas.")
        print("Se han vendido "+str(ventas_jose_nutribullet)+" nutribullets.")
        print("Se han vendido "+str(ventas_jose_estante)+" estantes.")
        print("Se han vendido "+str(ventas_jose_buro)+" burós.")
        print("Se han vendido "+str(ventas_jose_lampara)+" lámparas.")
        print("Se han vendido "+str(ventas_alan_xbox)+" Xbox One X.")
        print("Se han vendido "+str(ventas_alan_ps4)+" Play Station 4.")
        print("Se han vendido "+str(ventas_alan_iphone)+" Iphone 12.")
        print("Se han vendido "+str(ventas_alan_camara)+" cámaras.")
        print("Se han vendido "+str(ventas_alan_switch)+" Nintendo Switch.")
        print("Se han vendido "+str(ventas_salvador_paracetamol)+" Paracetamol.")
        print("Se han vendido "+str(ventas_salvador_peptobismol)+" Peptobismol.")
        print("Se han vendido "+str(ventas_salvador_treda)+" Treda.")
        print("Se han vendido "+str(ventas_salvador_vick)+" Vick Vaporub.")
        print("Se han vendido "+str(ventas_salvador_condones)+" condones.")
        print("Se han vendido "+str(ventas_venustiano_smirnoff)+" Smirnoff Tamarindo.")
        print("Se han vendido "+str(ventas_venustiano_josecuervo)+" José Cuervo.")
        print("Se han vendido "+str(ventas_venustiano_tecate)+" Tecates.")
        print("Se han vendido "+str(ventas_venustiano_merlot)+" Merlot.")
        print("Se han vendido "+str(ventas_venustiano_moet)+" Moet.")
        
    #Aquí se escribe el archivo de inventario otra vez, pero ahora teniendo la variable de cantidad que corresponda
    #tras haber corrido todo el programa.
    myfile=open("Inventario.txt","w")
    #Inventario Casa
    myfile.write("Casa"+","+"0023"+","+"Cama Rosa"+","+str(cant_nueva_camarosa)+",")
    myfile.write("Casa"+","+"0192"+","+"Nutribullet"+","+str(cant_nueva_nutribullet)+",")
    myfile.write("Casa"+","+"1093"+","+"Estante"+","+str(cant_nueva_estante)+",")
    myfile.write("Casa"+","+"0456"+","+"Buró"+","+str(cant_nueva_buro)+",")
    myfile.write("Casa"+","+"1230"+","+"Lámpara"+","+str(cant_nueva_lampara)+",")
    #Inventario Electrónica
    myfile.write("Electrónica"+","+"1234"+","+"Xbox One X"+","+str(cant_nueva_xbox)+",")
    myfile.write("Electrónica"+","+"9203"+","+"Play Station 4"+","+str(cant_nueva_ps4)+",")
    myfile.write("Electrónica"+","+"0012"+","+"Iphone 12"+","+str(cant_nueva_iphone)+",")
    myfile.write("Electrónica"+","+"1833"+","+"Cámara"+","+str(cant_nueva_camara)+",")
    myfile.write("Electrónica"+","+"3432"+","+"Nintendo Switch"+","+str(cant_nueva_switch)+",")
    #Inventario Farmacia
    myfile.write("Farmacia"+","+"9239"+","+"Paracetamol"+","+str(cant_nueva_paracetamol)+",")
    myfile.write("Farmacia"+","+"1254"+","+"Peptobismol"+","+str(cant_nueva_peptobismol)+",")
    myfile.write("Farmacia"+","+"9223"+","+"Treda"+","+str(cant_nueva_treda)+",")
    myfile.write("Farmacia"+","+"1238"+","+"Vick Vaporub"+","+str(cant_nueva_vick)+",")
    myfile.write("Farmacia"+","+"4352"+","+"Condones Trojan"+","+str(cant_nueva_condones)+",")
    #Inventario alcohol
    myfile.write("Alcohol"+","+"4321"+","+"Smirnoff Tamarindo"+","+str(cant_nueva_smirnoff)+",")
    myfile.write("Alcohol"+","+"3452"+","+"José Cuervo"+","+str(cant_nueva_josecuervo)+",")
    myfile.write("Alcohol"+","+"6582"+","+"Tecate"+","+str(cant_nueva_tecate)+",")
    myfile.write("Alcohol"+","+"8924"+","+"Merlot"+","+str(cant_nueva_merlot)+",")
    myfile.write("Alcohol"+","+"2323"+","+"Moet"+","+str(cant_nueva_moet))
    myfile.close()
    
    #Aquí se escribe el archivo de ventas otra vez, pero ahora teniendo la variable de cantidad que corresponda
    #tras haber corrido todo el programa.
    ventas=open("Ventas.txt", "w")
    #Ventas de José, encargado de departamento de casa.
    ventas.write("José"+","+"Cama Rosa"+","+str(ventas_jose_camarosa)+",")
    ventas.write("José"+","+"Nutribullet"+","+str(ventas_jose_nutribullet)+",")
    ventas.write("José"+","+"Estante"+","+str(ventas_jose_estante)+",")
    ventas.write("José"+","+"Buró"+","+str(ventas_jose_buro)+",")
    ventas.write("José"+","+"Lámpara"+","+str(ventas_jose_lampara)+",")
    #Ventas de Alan, encargado de departamento de electrónica.
    ventas.write("Alan"+","+"Xbox One X"+","+str(ventas_alan_xbox)+",")
    ventas.write("Alan"+","+"Play Station 4"+","+str(ventas_alan_ps4)+",")
    ventas.write("Alan"+","+"Iphone 12"+","+str(ventas_alan_iphone)+",")
    ventas.write("Alan"+","+"Cámara"+","+str(ventas_alan_camara)+",")
    ventas.write("Alan"+","+"Nintendo Switch"+","+str(ventas_alan_switch)+",")
    #Ventas de Salvador, encargado de departamento de farmacia.
    ventas.write("Salvador"+","+"Paracetamol"+","+str(ventas_salvador_paracetamol)+",")
    ventas.write("Salvador"+","+"Peptobismol"+","+str(ventas_salvador_peptobismol)+",")
    ventas.write("Salvador"+","+"Treda"+","+str(ventas_salvador_treda)+",")
    ventas.write("Salvador"+","+"Vick Vaporub"+","+str(ventas_salvador_vick)+",")
    ventas.write("Salvador"+","+"Condones"+","+str(ventas_salvador_condones)+",")
    #Ventas de Venustiano, encargado de departamento de alcohol.
    ventas.write("Venustiano"+","+"Smirnoff Tamarindo"+","+str(ventas_venustiano_smirnoff)+",")
    ventas.write("Venustiano"+","+"José Cuervo"+","+str(ventas_venustiano_josecuervo)+",")
    ventas.write("Venustiano"+","+"Tecate"+","+str(ventas_venustiano_tecate)+",")
    ventas.write("Venustiano"+","+"Merlot"+","+str(ventas_venustiano_merlot)+",")
    ventas.write("Venustiano"+","+"Moet"+","+str(ventas_venustiano_moet))
    ventas.close()
    
    #esta parte es para terminar el programa, si escribe s (que representa 'salir'), se usa quit() para terminar
    #sin embargo, si esto no se cumple, el while true del inicio vuelve a comenzar, por lo que se repite todo el programa.
    n=input("\n"+"Escribe s para terminar y cont para continuar: ")
    if n=="s":
        print("\n"+"Gracias por visitarnos, vuelva pronto")
        quit()


    
    
    
    

