import PySimpleGUI as sg

# criando janela principal
def main_win():
    sg.theme('DarkBlack1')
    linha = [
        [sg.Checkbox(''),sg.Input('')] ]
    
    layout = [
        [sg.Frame("Task's",linha,key='container')],
        [sg.Button('New Task'),sg.Button('Reset')] ]
    

    return sg.Window('To do List by Ero',layout,finalize=True)
# criar a janela
janela = main_win()
# criar as regras dessa janela
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'New Task':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Reset':
        janela.close()
        janela = main_win()