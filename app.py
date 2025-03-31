# Importa biblioteca Tkinter.
import tkinter as tk

# cria um objeto tkinter.
janela = tk.Tk()
# Define título da janela.
janela.title("Calculadora Python")
# Define tamanho da janela, Largura x Altura.
janela.geometry("300x400")
# Define uma janela de tamanho fixo.
janela.resizable(False,False)

# Variável que armazena expressão.
expressao_numerica = tk.StringVar()

# Função que atualiza expressão.
def clicar(botao):
    atual = expressao_numerica.get()
    expressao_numerica.set(atual + botao)

# Função que calcula resultado.
def calcular():
    try:
        resultado = eval(expressao_numerica.get())
        expressao_numerica.set(resultado)
    except:
        expressao_numerica.set("Erro")

# Função que limpa tela.
def limpar():
    expressao_numerica.set("")

# Define campo para entrada de dados.
entrada = tk.Entry(janela, textvariable=expressao_numerica, font=("Arial", 20, "bold"), bd=2, relief="ridge", justify="right")
entrada.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.15)


# Define teclas para a calculadora.
tecla9 = tk.Button(janela, text = ' 9 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('9'))
tecla9.place(relx = 0.45, rely = 0.25, relheight = 0.15, relwidth = 0.15)

tecla8 = tk.Button(janela, text = ' 8 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('8'))
tecla8.place(relx = 0.25, rely = 0.25,relheight = 0.15, relwidth = 0.15)

tecla7 = tk.Button(janela, text = ' 7 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('7'))
tecla7.place(relx = 0.05, rely = 0.25, relheight = 0.15, relwidth = 0.15)



tecla6 = tk.Button(janela, text = ' 6 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('6'))
tecla6.place(relx = 0.45, rely = 0.45, relheight = 0.15, relwidth = 0.15)

tecla5 = tk.Button(janela, text = ' 5 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('5'))
tecla5.place(relx = 0.25, rely = 0.45, relheight = 0.15, relwidth = 0.15)

tecla4 = tk.Button(janela, text = ' 4 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('4'))
tecla4.place(relx = 0.05, rely = 0.45, relheight = 0.15, relwidth = 0.15)



tecla3 = tk.Button(janela, text = ' 3 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('3'))
tecla3.place(relx = 0.45, rely = 0.65, relheight = 0.15, relwidth = 0.15)

tecla2 = tk.Button(janela, text = ' 2 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('2'))
tecla2.place(relx = 0.25, rely = 0.65, relheight = 0.15, relwidth = 0.15)

tecla1 = tk.Button(janela, text = ' 1 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('1'))
tecla1.place(relx = 0.05, rely = 0.65, relheight = 0.15, relwidth = 0.15)



tecla0 = tk.Button(janela, text = ' 0 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('0'))
tecla0.place(relx = 0.25, rely = 0.85, relheight = 0.1, relwidth = 0.15)

tecla_ponto = tk.Button(janela, text = '.', fg = 'white', font=("Arial", 20, "bold"), bg = 'gray', command = lambda: clicar('.'))
tecla_ponto.place(relx = 0.05, rely = 0.85, relheight = 0.1, relwidth = 0.15)

tecla_limpar = tk.Button(janela, text=' C ', fg='white', font=("Arial", 20, "bold"), bg = 'orange', bd = 3, command = limpar)
tecla_limpar.place(relx = 0.45, rely = 0.85, relheight = 0.1, relwidth = 0.15)



tecla_soma = tk.Button(janela, text = ' + ', fg = 'white', font=("Arial", 20, "bold"), bg = 'gray', command = lambda: clicar("+"))
tecla_soma.place(relx = 0.65, rely = 0.25, relheight = 0.15, relwidth = 0.15)

tecla_sub = tk.Button(janela, text = '-', fg = 'white', font=("Arial", 20, "bold"), bg = 'gray', command = lambda: clicar("-"))
tecla_sub.place(relx = 0.65, rely = 0.45, relheight = 0.15, relwidth = 0.15)

tecla_div = tk.Button(janela, text = '/', fg = 'white', font=("Arial", 20, "bold"), bg = 'gray', command = lambda: clicar("/"))
tecla_div.place(relx = 0.65, rely = 0.65, relheight = 0.15, relwidth = 0.15)

tecla_mult = tk.Button(janela, text = '*', fg = 'white', font=("Arial", 20, "bold"), bg = 'gray', command = lambda: clicar("*"))
tecla_mult.place(relx = 0.65, rely = 0.85, relheight = 0.1, relwidth = 0.15)



tecla_igual = tk.Button(janela, text = ' = ', fg = 'white', font=("Arial", 20, "bold"), bg = 'gray', command = calcular)
tecla_igual.place(relx = 0.86, rely = 0.25, relheight = 0.7, relwidth = 0.1)


# Iniciar a calculadora.
janela.mainloop()