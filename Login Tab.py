import PySimpleGUI as sg

# Layout
sg.theme("Reddit")
layout = [
    [sg.Text("Login  "),sg.Input(key="user",size=(20,1))],
    [sg.Text("Senha"),sg.Input(key="password",password_char="*",size=(20,1))],
    [sg.Checkbox("Salvar login?")],
    [sg.Button("Entrar")]
]
#Janela
janela = sg.Window("Tela de Login", layout)
#Ler os eventos
while True:
   evento, valores = janela.read()
   if evento == sg.WINDOW_CLOSED:
       break
   if evento == "Entrar":
       if valores["user"] == "Felipe" and valores["password"] == "1243":
           print("Bem-Vindo ao jogo!")
