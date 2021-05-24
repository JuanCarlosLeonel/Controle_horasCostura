## INTERFACE GRÁFICA EM ANDAMENTO


from tkinter import *
class Calculadora(object):
    def __init__(self, instancia):
        # Colocar entrada de texto
        self.form = Entry(instancia)
        self.form.pack()
        # botão calcular
        self.calc = Button(instancia, text="Calcule", fg = 'blue', command = self.Calcular)
        self.calc.pack()
        # texto das fórmulas:
        self.resultado = Label(instancia, text="Resultado", fg="red")
        self.resultado.pack()

        botoes = ('Média do func.', 'Valor período p/ hora', 'Produção total mais horas')
        for b in botoes:
            a = Button(instancia, text =b , )
            a.pack()
    def Calcular(self):
        self.resultado['text'] = self.form.get()
        self.resultado['fg'] = 'red'

# Criar a tela
instancia = Tk()
#Cria uma instancia da calculadora
Calculadora(instancia)
# título a tela
instancia.title('Fechamento horas-FINALIZAÇÃO')

# dá um tamanho a tela
instancia.geometry("800x600")
#Dá um ícone ao aplicativo
#instancia.wm_iconbitmap('icone.ico')

# inicia o programa
instancia.mainloop()

continuar = 'S'
while True:
    dia = 8.50
    dias = float(input('Quantidade de dias produtivos do mês:'))
    horasmes = dias * dia
    producao = float(input('Produção acumulada: R$'))
    print('Digite agora a quantidade de horas e minutos do funcionario:')
    horas = int(input('Horas:'))
    minutos = int(input('Minutos:'))
    horasproducao = (horasmes) - (horas + (minutos / 60))
    print(f'O funcionário produziu {horasproducao:.2f} horas.')
    media = ((producao / horasproducao))
    print(f'Média: R${media:.2f}')
    horasocioso = (horasmes - horasproducao)
    print(f'Período que ficou por hora: {horasocioso:.2f} horas')
    valorganhohora = ((media * horasocioso))
    print(f'Valor do período que ficou por hora: R$ {valorganhohora:.2f}')
    valorfinal = producao + valorganhohora
    print(f'Produção total mais horas :\033[1;31m R${valorfinal:.2f}\033[m')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N]')).upper()
    if continuar == 'N':
        break
print('FIM DE PROGRAMA...')
