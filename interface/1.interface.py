from tkinter import *;
from tkinter import messagebox;

janela = Tk()#iniciar tela

janela.title("Olá mundo")#titulo
janela.geometry('500x500+700+250')#tamanho e  posição da janela
#minimo e maximo da tela
janela.minsize(200,200)
janela.maxsize(600,600)

janela.resizable(False,False)#não funcionar o btn quadrado q max o tamanho

# janela.state("zoomed")#inicia ela maximada no tamanho inicial
# janela.state("iconic")#inicia com ela minimizada
 
janela['bg'] = 'white' #cor de fundo

#adicionando a label
nome = Label(janela, text = "Nome", font = "Arial 30 bold" , fg = "black",bg = 'white')
nome.pack()

#input
txtNome = Entry(janela, font = 'Arial 30', bg = 'red')
txtNome.pack()

#funcionalidades btns
def mensagemInformação():
    messagebox.showinfo("Informação", "Mensagem de informação")
    
def mensagemAtenção():
    messagebox.showwarning("Atenção", "mensagem de atenção")
    
def mensagemErro():
    messagebox.showerror("Erro", "messagem de erro")
    
def pegar():
    texto = txtNome.get()
    print(texto)

#btns
btn1 = Button(janela, text = "INFORMAÇÃO", font = 'Arial 15 bold' , bg = 'white', fg = 'black', width = '15', height= '1', command = mensagemInformação)
btn1.pack()

btn2 = Button(janela, text = "ATENÇÃO", bg = 'red', fg = 'white', font = "Arial 15 bold", width='15', height = '1', command = mensagemAtenção)
btn2.pack()

btn3 = Button(janela, text = "ERRO", font = 'Arial 15 bold' , bg = 'white', fg = 'black', width = '15', height= '1', command =  mensagemErro)
btn3.pack()

btn4 = Button(janela, text = "ENVIAR PRO PROMPT", font = 'Arial 15 bold' , bg = 'white', fg = 'black', width = '15', height= '1', command =  pegar)
btn4.pack()

janela.mainloop()

#Crie uma janela de cadastro, utilizando linguagem python, com a interface gráfica tkinter, para um cadastro de produtos, a interface deve ser intuitiva e elegante. Adicione os campos descrição, validade, segmento, lote, armazenamento, fornecedor e quantidade. Adicione 4 botões alinhados horizontalmente, sendo eles: inserir, pesquisar, alterar e excluir,  cada botão deverá chamar uma função especifica, para dizer qual botão foi clicado, onde se colocara funções futuras. Os campos não podem ficar sem informações, caso o usuário não adicione uma informação em um campo, mostre uma mensagem de aviso indicando que o campo deverá ser preenchido, e retorne o foco ao campo que necessita ser digitado. A janela não poderá ser redimensionada.
