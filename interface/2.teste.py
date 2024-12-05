import tkinter as tk
from tkinter import messagebox

# Funções para os botões
def inserir():
    messagebox.showinfo("Botão Clicado", "Botão Inserir foi clicado!")

def pesquisar():
    messagebox.showinfo("Botão Clicado", "Botão Pesquisar foi clicado!")

def alterar():
    messagebox.showinfo("Botão Clicado", "Botão Alterar foi clicado!")

def excluir():
    messagebox.showinfo("Botão Clicado", "Botão Excluir foi clicado!")

# Função para validar campos
def validar_campos():
    # Obtendo os valores dos campos
    descricao = entry_descricao.get()
    validade = entry_validade.get()
    segmento = entry_segmento.get()
    lote = entry_lote.get()
    armazenamento = entry_armazenamento.get()
    fornecedor = entry_fornecedor.get()
    quantidade = entry_quantidade.get()

    # Checando se algum campo está vazio
    if not descricao:
        messagebox.showwarning("Aviso", "O campo Descrição deve ser preenchido!")
        entry_descricao.focus()
        return False
    if not validade:
        messagebox.showwarning("Aviso", "O campo Validade deve ser preenchido!")
        entry_validade.focus()
        return False
    if not segmento:
        messagebox.showwarning("Aviso", "O campo Segmento deve ser preenchido!")
        entry_segmento.focus()
        return False
    if not lote:
        messagebox.showwarning("Aviso", "O campo Lote deve ser preenchido!")
        entry_lote.focus()
        return False
    if not armazenamento:
        messagebox.showwarning("Aviso", "O campo Armazenamento deve ser preenchido!")
        entry_armazenamento.focus()
        return False
    if not fornecedor:
        messagebox.showwarning("Aviso", "O campo Fornecedor deve ser preenchido!")
        entry_fornecedor.focus()
        return False
    if not quantidade:
        messagebox.showwarning("Aviso", "O campo Quantidade deve ser preenchido!")
        entry_quantidade.focus()
        return False

    # Se todos os campos forem preenchidos
    return True

# Criando a janela principal
janela = tk.Tk()
janela.title("Cadastro de Produtos")
janela.geometry("600x400")
janela.resizable(False, False)  # Desabilita o redimensionamento da janela

# Título
titulo = tk.Label(janela, text="Cadastro de Produtos", font=("Arial", 18))
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Campo Descrição
label_descricao = tk.Label(janela, text="Descrição:", font=("Arial", 12))
label_descricao.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_descricao = tk.Entry(janela, font=("Arial", 12), width=40)
entry_descricao.grid(row=1, column=1, padx=10, pady=5)

# Campo Validade
label_validade = tk.Label(janela, text="Validade:", font=("Arial", 12))
label_validade.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_validade = tk.Entry(janela, font=("Arial", 12), width=40)
entry_validade.grid(row=2, column=1, padx=10, pady=5)

# Campo Segmento
label_segmento = tk.Label(janela, text="Segmento:", font=("Arial", 12))
label_segmento.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_segmento = tk.Entry(janela, font=("Arial", 12), width=40)
entry_segmento.grid(row=3, column=1, padx=10, pady=5)

# Campo Lote
label_lote = tk.Label(janela, text="Lote:", font=("Arial", 12))
label_lote.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_lote = tk.Entry(janela, font=("Arial", 12), width=40)
entry_lote.grid(row=4, column=1, padx=10, pady=5)

# Campo Armazenamento
label_armazenamento = tk.Label(janela, text="Armazenamento:", font=("Arial", 12))
label_armazenamento.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_armazenamento = tk.Entry(janela, font=("Arial", 12), width=40)
entry_armazenamento.grid(row=5, column=1, padx=10, pady=5)

# Campo Fornecedor
label_fornecedor = tk.Label(janela, text="Fornecedor:", font=("Arial", 12))
label_fornecedor.grid(row=6, column=0, padx=10, pady=5, sticky="w")
entry_fornecedor = tk.Entry(janela, font=("Arial", 12), width=40)
entry_fornecedor.grid(row=6, column=1, padx=10, pady=5)

# Campo Quantidade
label_quantidade = tk.Label(janela, text="Quantidade:", font=("Arial", 12))
label_quantidade.grid(row=7, column=0, padx=10, pady=5, sticky="w")
entry_quantidade = tk.Entry(janela, font=("Arial", 12), width=40)
entry_quantidade.grid(row=7, column=1, padx=10, pady=5)

# Botões
botao_inserir = tk.Button(janela, text="Inserir", font=("Arial", 12), command=inserir)
botao_inserir.grid(row=8, column=0, padx=10, pady=20, sticky="w")

botao_pesquisar = tk.Button(janela, text="Pesquisar", font=("Arial", 12), command=pesquisar)
botao_pesquisar.grid(row=8, column=1, padx=10, pady=20, sticky="w")

botao_alterar = tk.Button(janela, text="Alterar", font=("Arial", 12), command=alterar)
botao_alterar.grid(row=8, column=2, padx=10, pady=20, sticky="w")

botao_excluir = tk.Button(janela, text="Excluir", font=("Arial", 12), command=excluir)
botao_excluir.grid(row=8, column=3, padx=10, pady=20, sticky="w")

# Botão de Verificação e Validação
validar_botao = tk.Button(janela, text="Validar", font=("Arial", 12), command=validar_campos)
validar_botao.grid(row=9, column=0, columnspan=4, pady=20)

# Iniciar a interface
janela.mainloop()
