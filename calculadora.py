import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculadora') # TITULO DA TELA
        self.configure(background= 'grey') # COR DE FUNDO
        self.geometry("375x575") # DIMENSÃO DA TELA DA CALCULADORA
        self.resizable(0,0) # NÃO DEIXO ELA SER RESPONSIVA 

        self.entrada_var = tk.StringVar() # VARIAVEL PARA O FRAME DO RESULTADO 
        
        self.frame_resultado = tk.Frame(self, bg="#d7d3d3") # CRIANDO O FRAME RESULTADO
        self.frame_resultado.pack(fill=tk.BOTH, expand=True) # COLOCANDO O FRAME RESULTADO NA JANELA

        self.frame_botoes = tk.Frame(self) # CRIANDO O FRAME BOTOES
        self.frame_botoes.pack(fill=tk.BOTH, expand=True) # COLOCANDO O FRAME BOTOES NA JANELA

        self.criar_entrada() # CHAMANDO FUNÇÃO PARA CRIAR A TELA DOS NÚMEROS
        self.criar_botoes() # CHAMANDO A FUNÇÃO PARA PRINTAR OS BOTOES

        self.mainloop()

#------------------------------- FUNÇÕES DAS TECLAS ESPECIAIS -------------------------------------------
    # FUNÇÃO QUE APAGA UM ALGARISMO DA TELA
    def apagar(self):
        entrada_atual = self.entrada_var.get()
        
        if entrada_atual:
            nova_entrada = entrada_atual[:-1]
            self.entrada_var.set(nova_entrada)

    # FUNÇÃO QUE APAGA A TELA INTEIRA
    def apagar_tudo(self):
        entrada_atual = self.entrada_var.get()
        
        if entrada_atual:
            limpo = ''
            self.entrada_var.set(limpo)

    # FUNÇÃO PARA FRAÇÃO
    def fracao(self):
        entrada_atual = self.entrada_var.get()
        
        if entrada_atual:
            valor = str(1/float(entrada_atual))
            self.entrada_var.set(valor)
        else:
            self.entrada_var.set('1/')

    # FUNÇÃO DO QUADRADO DE UM NÚMERO
    def quadrado(self):
        entrada_atual = self.entrada_var.get()
        if entrada_atual:
            valor = str(float(entrada_atual)**2.0)
            self.entrada_var.set(valor)
        else:
            self.entrada_var.set("Erro (digite um número)")

    # FUNÇÃO DA RAIZ DE UM NÚMERO
    def raiz(self):
        entrada_atual = self.entrada_var.get()
        if entrada_atual:
            valor = str(float(entrada_atual)**0.5)
            self.entrada_var.set(valor)
        else:
            self.entrada_var.set("Erro")
    
    # FUNÇÃO DO PARENTESE DA ESQUERDA
    def expressao_esquerda(self):
        entrada_atual = self.entrada_var.get()
        operadores = ['/','*','+','-']
        
        if entrada_atual:
            if entrada_atual[-1].isnumeric and not entrada_atual[-1] in operadores:
                nova_entrada = entrada_atual + '*('
                self.entrada_var.set(nova_entrada)
            else:
                nova_entrada = entrada_atual + '('
                self.entrada_var.set(nova_entrada)  
        else:
            nova_entrada = (entrada_atual + '(')
            self.entrada_var.set(nova_entrada)

    # FUNÇÃO DO PARENTESE DA DIREITA
    def expressao_direita(self):
        entrada_atual = self.entrada_var.get()
        
        if entrada_atual:
            nova_entrada = (entrada_atual + ')')
            self.entrada_var.set(nova_entrada)    
        else:
            self.entrada_var.set("Erro")

    # FUNÇÃO QUE INVERTE O VALOR DO NÚMERO
    def inverte(self):
        entrada_atual = self.entrada_var.get()

        if entrada_atual:
            invertido = str(float(entrada_atual)*(-1))
            self.entrada_var.set(invertido)
        else:
            self.entrada_var.set('Erro')

    # FUNÇÃO PARA DEIXAR O NÚMERO COM VÍRGULA
    def ponto(self):
        entrada_atual = self.entrada_var.get()
        
        if entrada_atual:
            nova_entrada = entrada_atual + '.'
            self.entrada_var.set(nova_entrada)
        else:
            nova_entrada = '0.'
            self.entrada_var.set(nova_entrada)

#------------------------------- FUNÇÕES BÁSICAS --------------------------------------------------------------
    
    # FUNÇÃO QUE CRIA A TELA DO RESULTADOS
    def criar_entrada(self):
        entrada = tk.Entry(self.frame_resultado, textvariable=self.entrada_var, font=("Arial", 24), justify="right")
        entrada.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # FUNÇÃO PARA PRESSIONAR OS NÚMEROS
    def pressionar_botao(self, valor):
        entrada_atual = self.entrada_var.get()
        self.entrada_var.set(entrada_atual + valor)

    # FUNÇÃO QUE CALCULA A EXPRESSÃO
    def calcular(self):
        try:
            resultado = str(eval(self.entrada_var.get()))
            self.entrada_var.set(resultado)
        except Exception as e:
            self.entrada_var.set("Erro")

    # FUNÇÃO DA INTERFACE DOS BOTOES
    def criar_botoes(self):
        botoes = [
            '(', ')', 'C', '<-',
            '1/X', 'X²', '√X', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '!', '0', '.', '='
        ]

        row, col = 1, 0

        for botao in botoes:
            if botao == '=':
                tk.Button(self.frame_botoes, text='=', command=self.calcular, width=12, height=5).grid(row=row, column=col)
            
            elif botao =='<-':
                tk.Button(self.frame_botoes, text=botao, command=self.apagar, width=12, height=5).grid(row=row, column=col)
            
            elif botao =='C':
                tk.Button(self.frame_botoes, text=botao, command=self.apagar_tudo, width=12, height=5).grid(row=row, column=col)
                
            elif botao =='(':
                tk.Button(self.frame_botoes, text=botao, command=self.expressao_esquerda, width=12, height=5).grid(row=row, column=col)
            
            elif botao == '1/X':
                tk.Button(self.frame_botoes, text=botao, command=self.fracao, width=12, height=5).grid(row=row, column=col)

            elif botao == 'X²':
                tk.Button(self.frame_botoes, text=botao, command=self.quadrado, width=12, height=5).grid(row=row, column=col)
            
            elif botao == '√X':
                tk.Button(self.frame_botoes, text=botao, command=self.raiz, width=12, height=5).grid(row=row, column=col)

            elif botao == ')':
                tk.Button(self.frame_botoes, text=botao, command=self.expressao_direita, width=12, height=5).grid(row=row, column=col)
            
            elif botao == '!':
                tk.Button(self.frame_botoes, text=botao, command=self.inverte, width=12, height=5).grid(row=row, column=col)

            elif botao == '.':
                tk.Button(self.frame_botoes, text=botao, command=self.ponto, width=12, height=5).grid(row=row, column=col)

            else:
                tk.Button(self.frame_botoes, text=botao, command=lambda b=botao: self.pressionar_botao(b), width=12, height=5).grid(row=row, column=col)
            
            col += 1
            if col > 3:
                col = 0
                row += 1

#-------------------------------------------------------------------------------------------------------------------

Application()