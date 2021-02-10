from tkinter import *

def iniciar_sesion():
    ventana2 = Tk()
    ventana2.geometry("500x200")
    ventana2.resizable(0, False)
    ventana2.mainloop()


)
boton = Button(ventana1, text="Iniciar sesion", command=iniciar_sesion).grid(
    row=2, column=0
)
Label(ventana1, text="Usted no esta registrado?").grid(row=3, column=0)
boton = Button(ventana1, text="Registrarse", command=iniciar_sesion).grid(
    row=4, column=0
)
ventana1.mainloop()
