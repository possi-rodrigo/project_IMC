import tkinter as tk

def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())

        imc = (peso / (altura * altura))

        if imc < 18.5:
            resultado_label.config(text=f"\n Seu IMC é {imc:.2f}" + "\n \n Considerado segundo a OMS (Organização Mundial da Saúde) \n como MAGREZA.")
        elif imc >= 18.5 and imc <=24.999:
            resultado_label.config(text=f"\n Seu IMC é {imc:.2f}" + "\n \n Considerado segundo a OMS (Organização Mundial da Saúde) \ncomo PESO NORMAL.")
        elif imc >= 25 and imc <= 29.999:
            resultado_label.config(text=f"\n Seu IMC é {imc:.2f}" + "\n \n Considerado segundo a OMS (Organização Mundial da Saúde) \n como SOBREPESO.")
        elif imc >= 30 and imc <= 34.999:
            resultado_label.config(text=f"\n Seu IMC é {imc:.2f}" + "\n \n Considerado segundo a OMS (Organização Mundial da Saúde) \n como OBESIDADE GRAU I.")
        elif imc >= 35 and imc <= 39.999:
            resultado_label.config(text=f"\n Seu IMC é {imc:.2f}" + "\n \n Considerado segundo a OMS (Organização Mundial da Saúde) \n como OBESIDADE GRAU I.")
        else:
            resultado_label.config(text=f"\n Seu IMC é {imc:.2f}" + "\n \n Considerado segundo a OMS (Organização Mundial da Saúde) \n como OBESIDADE GRAU III.")
    except ZeroDivisionError:
        resultado_label.config(text="Impossível dividir por zero, digite valores válidos.")
    except ValueError:
        resultado_label.config(text="Digite valores válidos para altura e peso conforme exemplificado.")
    

janela = tk.Tk()
janela.title("                                                         Calcule seu IMC") #Os vários espaços é para o título ficar "centralizado", ao invés de alinhado a esquerda.
janela.geometry("480x250")
janela.resizable(False, False)

label_peso = tk.Label(janela, text="Digite seu peso em quilos (Ex.: 12.34)")
label_peso.pack()
entrada_peso = tk.Entry(janela)
entrada_peso.pack()

label_altura = tk.Label(janela, text="\n Digite sua altura em metros (Ex.: 1.23)")
label_altura.pack()
entrada_altura = tk.Entry(janela)
entrada_altura.pack()

botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

janela.mainloop()