
class Calculos:

    def menu (self):
        opc = 0
        while opc!=5:
            print("MENU")
            print("[1] Registrar contacto")
            print("[2] Listar contactos")
            print("[3] Modificar un contacto")
            print("[4] Eliminar un contacto")
            print("[5] Salir")

            opc = int(input(">> "))
            if opc==1:
                self.registrar()
            elif opc==2:
                self.listar()
            elif opc==3:
                self.modificar()
            elif opc==4:
                self.eliminar()
            
    def registrar(self):
        
        import mysql.connector
        
        mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="tienda"
        )

        mycursor=mydb.cursor()
        
        nombres = input("Nombres: ")
        telefono = int(input("Telefono: "))
        direccion = input("Direccion: ")

        sql = "insert into contacto (nombres, telefono, direccion) values (%s, %s, %s)"
        val = (nombres, telefono, direccion)
        mycursor.execute(sql, val)
        mydb.commit()
        print("")
        print (mycursor.rowcount,"Cliente registrado correctamente")
        print("")

    def listar(self):
        
        import mysql.connector
        
        mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="tienda"
        )

        mycursor=mydb.cursor()

        sql="select * from contacto"
        mycursor.execute(sql)

        myresult = mycursor.fetchall()
        print("")
        for x in myresult:
            print(x)
        print("")

c = Calculos()
c.menu()












