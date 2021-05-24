from tkinter import *

def somar():
    global resultado
    texto = entrada_de_texto.get()
    numero = int(texto)
    resultado += numero
    print("Resultado: %i"%resultado)

janela = Tk()
resultado = 0

entrada_de_texto = Entry(janela,width=10,bg="white",font=("Arial",15))
entrada_de_texto.pack()

Button(janela,text="Somar",command=somar).pack()
janela.mainloop()