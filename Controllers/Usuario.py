from tkinter import messagebox
from Models.conexionBD import conexionBD

class Usuario():
    def __init__(self,  nombrebreusuario, password):
        self.NombreUsuario =  nombrebreusuario
        self.password = password
        self.rol = ""

    def iniciarSesion(self,  nombrebreusuario, password):
        miConexion =  conexionBD()
        miConexion.crearConexion()
        conn = miConexion.getConnection()
        cursor =  conn.cursor()
        cursor.execute("select * from usuario")
        listaUsuarios = cursor.fetchall()

        for usuario in listaUsuarios:
            if(usuario[1] == nombrebreusuario and usuario[2] == password):
                self.rol = usuario[3]
                if(self.rol == "admin"):
                    messagebox.showinfo("informacion","Acceso correcto Administrador")
                    #crear objeto Administrador y abrir menu Administrador 
                else:
                    messagebox.showinfo("informacion", "Acceso correcto Digitador")
                miConexion.cerrarConexion
                return
        messagebox.showwarning("Advertencia", "El nombre de  usuario y/o contraseña no existe, verifique e intente nuevamente")
