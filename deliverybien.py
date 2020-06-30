class persona:
    def __init__(self):
        self.nombre = []
        self.apellido = []
        self.telefono = []
        self.carnet = []
        self.estado = []

    def validar(self, eleccion):
        if eleccion.isdigit():
            return True
        else:
            return False

    def menuPersona(self):
        opciones = """
     *** 📂  Modificar datos personales 📂  ***

              1.- Nombre 
              2.- apellido
              3.- telefono
              4.- carnet
              5.- tipo licencia
              6.- volver al menu principal

                  """
        print(opciones)
        eleccion1 = input("Digite una opción: \n")
        if self.validar(eleccion1):
            eleccion = int(eleccion1)
        else:
            print("¡¡¡¡Digite solo números!!!")
            self.menuPersona()
        self.opciones(eleccion)

    def opciones(self, eleccion):
        if eleccion == 1:
            nombre2 = input("Digite el nro de carnet: \n")
            for i in range(len(self.nombre)):
                if self.carnet[i] == nombre2:
                    nombre2_1 = input("Digite el nuevo nombre: \n")
                    self.nombre[i] = nombre2_1
                    print("La modificacion del nombre se realizo con exito!!!")
            else:
                return "No se encontraron coincidencias"
        elif eleccion == 2:
            apellido2 = input("Digite el nro de carnet: \n")
            for i in range(len(self.apellido)):
                if self.carnet[i] == apellido2:
                    apellido2_1 = input("Digite el nuevo apellido: \n")
                    self.apellido[i] = apellido2_1
                    print("La modificacion se realizo correctamente!!!")
            else:
                return "No se encontraron coincidencias"
        elif eleccion == 3:
            telefono2 = input("Digite el nro de carnet: \n")
            for i in range(len(self.nombre)):
                if self.carnet[i] == telefono2:
                    telefono2_1 = int(input("Digite el nuevo numero: \n"))
                    self.telefono[i] = telefono2_1
                    print("La modificacion se realizo correctamente!!!")
            else:
                return "No se encontraron coincidencias"
        elif eleccion == 4:
            carnet2 = input("Digite el nro de carnet: \n")
            for i in range(len(self.nombre)):
                if self.carnet[i] == carnet2:
                    carnet2_1 = input("Digite el nuevo carnet: \n")
                    self.carnet[i] = carnet2_1
                    print("La modificacion se realizo correctamente!!!")
            else:
                return "No se encontraron coincidencias"
        elif eleccion == 5:
            self.modificar_licencia()
        elif eleccion == 6:
            self.menu()
        else:
            print("Digite una opcion valida")
            return (self.menuPersona())
        pass

    def guardarPersona(self, nombre, apellido, telefono, carnet):
        self.nombre.append(nombre)
        self.apellido.append(apellido)
        self.telefono.append(telefono)
        self.carnet.append(carnet)
        return "Datos actualizados correctamente!!!"

    def detallePersona(self, posicion):
        print("--------------------")
        print("Nombre : {}".format(self.nombre[posicion]))
        print("Apellido : {}".format(self.apellido[posicion]))
        print("telefono: {}".format(self.telefono[posicion]))
        print("carnet : {}".format(self.carnet[posicion]))
        pass

    def mostrarPersona(self):
        if (self.nombre):
            for i in range(len(self.nombre)):
                self.detallePersona(i)
        else:
            return "Aun no hay datos!!!"
        return "--------------------"


class usuario(persona):
    def __init__(self):
        persona.__init__(self)
        self.email = []
        self.contra = []


class conductor(usuario):
    def __init__(self):
        usuario.__init__(self)
        self.tipoLicencia = []
        self.vehiculo = []
        self.estado = []

    def modificar_licencia(self):
        propietario = input("digite el nro de carnet: \n")
        for i in range(len(self.nombre)):
            if self.carnet[i] == propietario:
                propietario2 = input("Digite el nuevo tipo de licencia: \n")
                self.tipoLicencia[i] = propietario2
                print("La modificacion se realizo correctamente!!!")
        else:
            return "No se encontraron coincidencias"


class vehiculo(conductor):
    def __init__(self):
        conductor.__init__(self)
        self.placa = []
        self.cilindrada = []

    def menuAuto(self):
        opciones = """
        *** 🔩 Modificar datos del vehiculo 🔩 ***

              1.- vehiculo 
              2.- marca
              3.- placa
              4.- cilindrada
              5.- volver al menu principal

                  """
        print(opciones)
        eleccion1 = input("Digite una opción: \n")
        if self.validar(eleccion1):
            eleccion = int(eleccion1)
        else:
            print("¡¡¡¡Digite solo números!!!")
            self.menuAuto()
        self.opciones2(eleccion)

    def opciones2(self, eleccion):
        if eleccion == 1:
            propietario = input("Digite el nro de carnet: \n")
            for i in range(len(self.nombre)):
                if self.carnet[i] == propietario:
                    propietario2 = input("Digite el nuevo vehiculo asignado: \n")
                    self.vehiculo[i] = propietario2
                    print("La modificacion se realizo correctamente!!!")
            else:
                return "No se encontraron coincidencias"
        elif eleccion == 2:
            self.modificar_marca()
        elif eleccion == 3:
            propietario = input("Digite el nro de carnet: \n")
            for i in range(len(self.nombre)):
                if self.carnet[i] == propietario:
                    propietario2 = int(input("Digite nueva placa: \n"))
                    self.placa[i] = propietario2
                    print("La modificacion se realizo correctamente!!!")
            else:
                return "No se encontraron coincidencias"
        elif eleccion == 4:
            propietario = input("Digite el nro de carnet: \n")
            for i in range(len(self.nombre)):
                if self.carnet[i] == propietario:
                    propietario2 = input("Digite cilindrada: \n")
                    self.cilindrada[i] = propietario2
                    print("La modificacion se realizo correctamente!!!")
            else:
                return "No se encontraron coincidencias"
        elif eleccion == 5:
            self.menu()
        else:
            print("Digite una opcion valida")
            return self.menuAuto()

    def guardarAuto(self, vehiculo, tipoLicencia, placa, cilindrada):
        self.vehiculo.append(vehiculo)
        self.tipoLicencia.append(tipoLicencia)
        self.placa.append(placa)
        self.cilindrada.append(cilindrada)
        return "Datos actualizados correctamente!!!"

    def detalleAuto(self, posicion):
        print("---------------------")
        print("Nombre : {}".format(self.nombre[posicion]))
        print("Carnet: {}".format(self.carnet[posicion]))
        print("vehiculo : {}".format(self.vehiculo[posicion]))
        print("marca : {}".format(self.marca[posicion]))
        print("tipoLicencia :{} ".format(self.tipoLicencia[posicion]))
        print("placa : {}".format(self.placa[posicion]))
        print("cilindrada :{} ".format(self.cilindrada[posicion]))
        pass

    def mostrarAuto(self):
        if (self.nombre):
            for i in range(len(self.nombre)):
                self.detalleAuto(i)
        else:
            return "Aun no hay datos!!!"


class tipoVehiculo(vehiculo):
    def __init__(self):
        vehiculo.__init__(self)
        self.tipoVehiculo = []


class marca(tipoVehiculo):
    def __init__(self):
        tipoVehiculo.__init__(self)
        self.marca = []
        self.procedencia = []

    def menu(self):
        opciones = """
    ***  🚚 DeliverY Los SolFaMiDas  🚚 ***

           1.- Registrar
           2.- Mostrar habilitados
           3.- Mostrar no habilitados
           4.- Modificar
           5.- Salir
    **************************************

               """
        print(opciones)
        eleccion1 = input("Digite una opción: \n")
        if self.validar(eleccion1):
            eleccion = int(eleccion1)
        else:
            print("¡¡¡¡Digite solo números!!!")
            self.menu()
        self.opciones3(eleccion)

    def opciones3(self, eleccion):
        if eleccion == 1:
            print(self.registrar())
            self.menu()
        elif eleccion == 2:
            print(self.mostrarSi())
            self.menu()
        elif eleccion == 3:
            print(self.mostrarNo())
            self.menu()
        elif eleccion == 4:
            print(self.menuModificar())
            self.menu()
        elif eleccion == 5:
            print("Gracias por utilizar el sistema")
        else:
            print("Digite una opcion valida")
            return self.menu()
        pass

    def menuModificar(self):
        opciones = """
          *** 🔧 Menu Modificaciones 🔧 ***

              1.- Datos Pesonales
              2.- Datos del auto
              3.- Habilitar 
              4.- Deshabilitar
              5.- volver al menu principal

                  """
        print(opciones)
        eleccion1 = input("Digite una opción: \n")
        if self.validar(eleccion1):
            eleccion = int(eleccion1)
        else:
            print("¡¡¡¡Digite solo números!!!")
            self.menuModificar()
        self.opciones4(eleccion)

    def opciones4(self, eleccion):
        if eleccion == 1:
            print(self.mostrarSi2())
            print(self.menuPersona())
            print(self.menuModificar())
        elif eleccion == 2:
            print(self.mostrarSi3())
            print(self.menuAuto())
            print(self.menuModificar())
        elif eleccion == 3:
            print(self.habilitar())
            print(self.menuModificar())
        elif eleccion == 4:
            print(self.deshabilitar())
            print(self.menuModificar())
        elif eleccion == 5:
            self.menu()
        else:
            print("Digite una opcion valida")
            return self.menu()
        pass

    def registrar(self):
        nombre = input("Ingrese nombre: \n")
        apellido = input("Ingrese  el apellido: \n")
        telefono = int(input("Numero de telefono: \n"))
        carnet = input("Numero de carnet: \n")
        email = self.generar_usuario(nombre, apellido)
        contra = self.generar_password(carnet)
        tipoLicencia = input("Tipo de licencia:\n")
        vehiculo = input("Vehiculo: \n")
        tipoVehiculo = input("Tipo de vehiculo: \n")
        placa = input("Numero de placa:\n")
        cilindrada = input("Cilindrada:\n")
        marca = input("Marca:\n")
        procedencia = input("Procedencia:\n")
        print(
            self.guardar(nombre, apellido, telefono, carnet, email, contra, tipoLicencia, vehiculo, tipoVehiculo, placa,
                         cilindrada, marca, procedencia))
        otro = input("Desea registrar otro: s/n \n")
        if (otro == "s" or otro == "s"):
            self.registrar()
        return "--------------------"

    def guardar(self, nombre, apellido, telefono, carnet, email, contra, tipoLicencia, vehiculo, tipoVehiculo, placa,
                cilindrada, marca, procedencia):
        self.nombre.append(nombre)
        self.apellido.append(apellido)
        self.telefono.append(telefono)
        self.carnet.append(carnet)
        self.email.append(email)
        self.contra.append(contra)
        self.tipoLicencia.append(tipoLicencia)
        self.vehiculo.append(vehiculo)
        self.tipoVehiculo.append(tipoVehiculo)
        self.placa.append(placa)
        self.cilindrada.append(cilindrada)
        self.marca.append(marca)
        self.procedencia.append(procedencia)
        self.estado.append(1)
        return "** {} fue registrado correctamente **".format(nombre)

    def detalle(self, posicion):
        print("--------------------")
        print("Nombre: {} {}".format(self.nombre[posicion], self.apellido[posicion]))
        print("Telefono: {}".format(self.telefono[posicion]))
        print("Carnet: {}".format(self.carnet[posicion]))
        print("Email: {}".format(self.email[posicion]))
        print("Contraceña:{} ".format(self.contra[posicion]))
        print("TipoLicencia:{} ".format(self.tipoLicencia[posicion]))
        print("Vehiculo: {}".format(self.vehiculo[posicion]))
        if (self.estado[posicion] == 1):
            print("habilitado: si")
        elif (self.estado[posicion] == 0):
            print("habilitado: No")
        print("TipoVehiculo:{} ".format(self.tipoVehiculo[posicion]))
        print("Placa: {}".format(self.placa[posicion]))
        print("Cilindrada:{} ".format(self.cilindrada[posicion]))
        print("Marca:{} ".format(self.marca[posicion]))
        print("Procedencia:{} ".format(self.procedencia[posicion]))
        pass

    def mostrar(self):
        if (self.nombre):
            for i in range(len(self.nombre)):
                self.detalle(i)
            return "--------------------"
        else:
            return "Aun no hay datos!!!"

    def deshabilitar(self):
        self.mostrar()
        pregunta = input("Nro de carnet de la persona a deshabilitar: \n")
        posicion = self.carnet.index(pregunta)
        self.estado[posicion] = 0
        return "{} fue dado de baja".format(self.nombre[posicion])

    def habilitar(self):
        self.mostrar()
        pregunta = input("Nro de carnet de la persona a habilitar: \n")
        posicion = self.carnet.index(pregunta)
        self.estado[posicion] = 1
        return "{} fue dado de Alta".format(self.nombre[posicion])

    def mostrarSi(self):
        habi = False
        for i in range(len(self.nombre)):
            if (self.estado[i] == 1):
                self.detalle(i)
                habi = True
        if (habi == False):
            return "No hay datos en la base de habilitados!!"
        return "--------------------"

    def mostrarSi2(self):
        habi = False
        for i in range(len(self.nombre)):
            if (self.estado[i] == 1):
                self.detallePersona(i)
                habi = True
        if (habi == False):
            return "No hay datos en la base de habilitados!!"
        return "--------------------"

    def mostrarSi3(self):
        habi = False
        for i in range(len(self.nombre)):
            if (self.estado[i] == 1):
                self.detalleAuto(i)
                habi = True
        if (habi == False):
            return "No hay datos en la base de habilitados!!"
        pass

    def mostrarNo(self):
        habi = False
        for i in range(len(self.nombre)):
            if (self.estado[i] == 0):
                self.detalle(i)
                habi = True
        if (habi == False):
            return "no hay datos en la base de deshabilitados!!"
        pass

    def generar_password(self, carnet):
        contra = str(carnet) + "001"
        return contra

    def generar_usuario(self, nombre, apellido):
        usuario = str(apellido) + str(nombre[0]) + "@delivery.com"
        return usuario

    def modificar_marca(self):
        propietario = input("Digite el nro de carnet: \n")
        for i in range(len(self.nombre)):
            if self.carnet[i] == propietario:
                propietario2 = input("Digite la marca: \n")
                self.marca[i] = propietario2
                print("La modificacion se realizo correctamente!!!")
        else:
            return "No se encontraron coincidencias"


delivery = marca()
delivery.menu()