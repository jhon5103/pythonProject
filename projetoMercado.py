
import tkinter as tk
import crud as crud
from tkinter import ttk
from tkinter import messagebox


class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()
        
        # componentes
        #Joubert Lima Correa de Oliveira - 202102283388, 
        #Jhonata Goncalves Antunes - 202102212812
        self.lblCodigo = tk.Label(win, text='Código do Produto:', font=fonte)
        self.lblNome = tk.Label(win, text='Nome do Produto', font=fonte)
        self.lblPreco = tk.Label(win, text='Preço', font=fonte)
        self.lblPrecoAdd = tk.Label(win, text="Preço c/ 10% ", font=fonte)

        self.txtCodigo = tk.Entry(bd=4, font=fonte)
        self.txtNome = tk.Entry(font=fonte)
        self.txtPreco = tk.Entry(font=fonte)
        self.txtPrecoAdd = ttk.Entry(font=fonte)

        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto, font=fonte)
        self.btnAtualizar = tk.Button(win, text='Atualizar', command=self.fAtualizarProduto, font=fonte)
        self.btnExcluir = tk.Button(win, text='Excluir', command=self.fExcluirProduto, font=fonte)
        self.btnLimpar = tk.Button(win, text='Limpar', command=self.fLimparTela, font=fonte)
        #Componente TreeView
        
        self.dadosColunas = ("Código", "Nome", "Preço", "Preco c/ acrescimo")

        self.treeProdutos = ttk.Treeview(win,
                                         columns=self.dadosColunas,
                                         selectmode='browse')

        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeProdutos.yview)
        self.verscrlbar.pack(side='right', fill='x')

        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)

        self.treeProdutos.heading("Código", text="Código")
        self.treeProdutos.heading("Nome", text="Nome")
        self.treeProdutos.heading("Preço", text="Preço")
        self.treeProdutos.heading("Preco c/ acrescimo", text="Preco c/ acrescimo")

        self.treeProdutos.column("Código", minwidth=0, width=100)
        self.treeProdutos.column("Nome", minwidth=0, width=100)
        self.treeProdutos.column("Preço", minwidth=0, width=100)
        self.treeProdutos.column("Preco c/ acrescimo", minwidth=0, width=100)

        self.treeProdutos.pack(padx=10, pady=10)

        self.treeProdutos.bind("<<TreeviewSelect>>",
                               self.apresentarRegistrosSelecionados)

        #Joubert Lima Correa de Oliveira - 202102283388,
        #Jhonata Goncalves Antunes - 202102212812                       
        
        self.lblCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)

        self.lblNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)

        self.lblPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)

        self.lblPrecoAdd.place(x=100, y=200)
        self.txtPrecoAdd.place(x=250, y=200)

        self.btnCadastrar.place(x=100, y=250)
        self.btnAtualizar.place(x=200, y=250)
        self.btnExcluir.place(x=300, y=250)
        self.btnLimpar.place(x=400, y=250)

        self.treeProdutos.place(x=100, y=350)
        self.verscrlbar.place(x=805, y=350, height=800)
        self.carregarDadosIniciais()

    # Apresentar registros selecionados
    #Joubert Lima Correa de Oliveira - 202102283388,
    #Jhonata Goncalves Antunes - 202102212812   

    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeProdutos.selection():
            item = self.treeProdutos.item(selection)
            codigo, nome, preco, precoAdd = item["values"][0:4]
            self.txtCodigo.insert(0, codigo)
            self.txtNome.insert(0, nome)
            self.txtPreco.insert(0, preco)
            self.txtPrecoAdd.insert(0, precoAdd)

    # carregar dados iniciais
    #Joubert Lima Correa de Oliveira - 202102283388,
    #Jhonata Goncalves Antunes - 202102212812
    def carregarDadosIniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registros = self.objBD.selecionarDados()
            print("************ dados dsponíveis no BD ***********")
            for item in registros:
                codigo = item[0]
                nome = item[1]
                preco = item[2]
                precoAdd = item[3]
                print("Código = ", codigo)
                print("Nome = ", nome)
                print("Preço  = ", preco)
                print("Preco c/ acrescimo: ", precoAdd, "\n")

                self.treeProdutos.insert('', 'end',
                                         iid=self.iid,
                                         values=(codigo,
                                                 nome,
                                                 preco,
                                                 precoAdd))
                self.iid = self.iid + 1
                self.id = self.id + 1
            print('Dados da Base')
        except:
            print('Ainda não existem dados para carregar')

        # Ler dados
        #Joubert Lima Correa de Oliveira - 202102283388,
        #Jhonata Goncalves Antunes - 202102212812
        
    def fLerCampos(self):
        try:

            print("************ dados dsponíveis ***********")
            codigo = int(self.txtCodigo.get())
            nome = self.txtNome.get()
            preco = float(self.txtPreco.get())
            precoAdd = preco + (preco*0.10)
            print('Leitura dos Dados com Sucesso!')
        except:
            print('Não foi possível ler os dados.')
        return codigo, nome, preco, precoAdd


    # Cadastrar Produto
    #Joubert Lima Correa de Oliveira - 202102283388,
    #Jhonata Goncalves Antunes - 202102212812
    def fCadastrarProduto(self):
        try:
            print("************ dados dsponíveis ***********")
            codigo, nome, preco, precoAdd = self.fLerCampos()
            self.objBD.inserirDados(codigo, nome, preco, precoAdd)
            self.treeProdutos.insert('', 'end',
                     iid=self.iid,
                     values=(codigo,
                             nome,
                             preco,
                             precoAdd))
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.fLimparTela()
            print('Produto Cadastrado com Sucesso!')
        except:
            print('Não foi possível fazer o cadastro.')
            


        # Atualizar Produtos
        #Joubert Lima Correa de Oliveira - 202102283388,
        #Jhonata Goncalves Antunes - 202102212812
    def fAtualizarProduto(self):
        try:
            codigo, nome, preco, precoAdd = self.fLerCampos()
            self.objBD.atualizarDados(codigo, nome, preco, precoAdd)
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print("Produto atualizado com sucesso")
        except:
            print("Nao foi possivel fazer a atualização")


        # Excluir Produtos
        #Joubert Lima Correa de Oliveira - 202102283388,
        #Jhonata Goncalves Antunes - 202102212812

    def fExcluirProduto(self):
        try:
            codigo, nome, preco, precoAdd = self.fLerCampos()
            self.objBD.excluirDados(codigo)
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print("Produto excluído com sucesso")
        except:
            print("Não foi possível fazer a exclusão")
            messagebox.showwarning("Alerta", "Não foi possível fazer a exclusão")

    
    #Limpa tela
    #Joubert Lima Correa de Oliveira - 202102283388,
    #Jhonata Goncalves Antunes - 202102212812
    def fLimparTela(self):
        try:
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            self.txtPrecoAdd.delete(0, tk.END)
            print('Campos limpos!')
        except:
            print('Não foi possível limpar os campos')



#principal
#Joubert Lima Correa de Oliveira - 202102283388,
#Jhonata Goncalves Antunes - 202102212812
fonte = ('verdana','10', 'bold')
messagebox.showinfo("Alerta", "Bem vindo")
janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title("Bem vindo a Tela de Cadastro")
ttk.Label(janela, text="Dados do Produto", font=fonte, style="BW.TLabel").place(x= 250, y= 0)
janela.geometry("820x700+10+10")
janela.mainloop()
