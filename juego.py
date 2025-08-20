from tkinter import *
from tkinter import messagebox as MessageBox
import random

ventana = Tk()
ventana.geometry("400x400")
ventana.title("Piedra, Papel o Tijeras")

# Encabezado
encabezado = Label(
    ventana,
    text="Tu vs la computadora",
    fg="White",
    bg="lightBlue",
    font=("Open Sans", 18),
    padx=5,
    pady=5
)
encabezado.pack(anchor=N)
Label(ventana, text="").pack()

# Opciones
opciones = ["piedra", "papel", "tijeras"]
opcion_usuario = StringVar()

# Función para jugar
def jugar(eleccion):
    opcion_usuario.set(eleccion)
    computadora = random.choice(opciones)

    if eleccion == computadora:
        MessageBox.showinfo("Resultado", f"Empate! Ambos eligieron {eleccion}")
    elif (eleccion == "piedra" and computadora == "tijeras") or \
         (eleccion == "papel" and computadora == "piedra") or \
         (eleccion == "tijeras" and computadora == "papel"):
        MessageBox.showinfo("Resultado", f"Ganaste! Computadora eligió {computadora}")
    else:
        MessageBox.showinfo("Resultado", f"Perdiste! Computadora eligió {computadora}")

# Botones
Button(ventana, text="Piedra", command=lambda: jugar("piedra")).pack(pady=5)
Button(ventana, text="Papel", command=lambda: jugar("papel")).pack(pady=5)
Button(ventana, text="Tijeras", command=lambda: jugar("tijeras")).pack(pady=5)

ventana.mainloop()