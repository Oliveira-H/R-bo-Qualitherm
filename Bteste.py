import pyautogui
import webbrowser
from time import sleep
import time
import clipboard
import os

# definir quantidade de arquivos
initial_count = 0
dir = "C:/Users/Bruno Neves/Desktop/Teste/Coletas processadas/Obsoletos/Tabelas"
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        initial_count += 1
# laço de repetição enquanto houver arquivos
num_ciclos = 0
while num_ciclos < initial_count:
    # Abrir pasta onde estão as tabelas
    path = 'C:/Users/Bruno Neves/Desktop/Teste/Coletas processadas/Obsoletos/Tabelas'
    webbrowser.open('file:///' + path)
    time.sleep(2)
    pyautogui.keyDown('f11')
    pyautogui.keyUp('f11')

    # selecionar, arrastar e converter o arquvio
    pyautogui.moveTo(258,69, duration=3)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.keyDown('f11')
    pyautogui.keyUp('f11')
    time.sleep(1)
    pyautogui.moveTo(652,744, 1)
    time.sleep(1)
    pyautogui.moveTo(710,368, 1)
    pyautogui.mouseUp(button='left')
    time.sleep(1)
    pyautogui.click(1178,618, 2)
    time.sleep(4)
    # abrir arquivo seleionar e copiar dados

    path = 'C:/Users/Bruno Neves/Downloads/Coletas a Editar'

    webbrowser.open('file:///' + path)
    time.sleep(4)
    pyautogui.keyDown('f11')
    pyautogui.keyUp('f11')
    time.sleep(7)
    pyautogui.doubleClick(258,69,)
    time.sleep(6)
    pyautogui.click(1164,37, 2)
    # adiquirir número de páginas e tempo do processo
    time.sleep(5)
    pyautogui.doubleClick(923, 193, duration=2)
    pyautogui.click(1283, 715, duration=2)
    pyautogui.click(1315, 696, duration=2)
    pyautogui.click(1315, 696, duration=2)
    pyautogui.moveTo(1160,200)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.moveTo(1129,198)
    pyautogui.mouseUp(button='left')
    pyautogui.hotkey('ctrl', 'c')
    Numero_Pag = clipboard.paste()
    clipboard.copy("")  # caso queira deixar vazia após settar a variavel.
    Numero_pag_int = int(Numero_Pag)
    # abrir TXT e pegar Horario do Processo
    path = 'C:/Users/Bruno Neves/Desktop/Teste/Processo.txt'
    webbrowser.open('file:///' + path)
    # deixar em tela cheia
    pyautogui.click(1147, 94, duration=1)
    # selecionar copiar e guardar inicio do processo
    pyautogui.moveTo(156,53)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.moveTo(6,53, 1)
    pyautogui.mouseUp(button='left')
    pyautogui.hotkey('ctrl', 'c')
    Inicio_processo = clipboard.paste()
    clipboard.copy("")
    # selecionar e copiar fim do processo
    pyautogui.moveTo(350,53)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.moveTo(196,53, 1)
    pyautogui.mouseUp(button='left')
    pyautogui.hotkey('ctrl', 'c')
    Fim_processo = clipboard.paste()
    clipboard.copy("")
    # selecionar e copiar adição ou subtrção de valores
    pyautogui.moveTo(373,53)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.moveTo(357,53, 1)
    pyautogui.mouseUp(button='left')
    pyautogui.hotkey('ctrl', 'c')
    Val = clipboard.paste()
    clipboard.copy("")
    # apagar tempo de processo deixando pronto para o próximo ciclo
    pyautogui.click(7,70, duration=1)
    apag = 0
    while apag <= 47:
        pyautogui.press('backspace')
        apag += 1
        # salvar arquivo
    pyautogui.hotkey('ctrl', 's')
    # fechar TXT e voltar ao estado 100% do word para continuar
    pyautogui.click(1354,7, duration=1)
    pyautogui.doubleClick(1243,544, duration=1)
    pyautogui.click(1248,715, duration=1)
    pyautogui.click(1317,717, duration=1)
    pyautogui.click(1362,148, duration=1)
    pyautogui.click(1362,148, duration=1)
    pyautogui.click(1362,148, duration=1)
    # de volta ao andamento normal
    pyautogui.click(1234,102, duration=2)
    pyautogui.click(1034, 132, duration=2)
    time.sleep(1)
    pyautogui.hotkey('Ctrl', 'c')
    # abrir modelo de edição, colar e copiar dados de volta ao word
    path = 'C:/Users/Bruno Neves/Desktop/Teste/Modelo Edição Números Aleatórios.xlsx'
    webbrowser.open('file:///' + path)
    time.sleep(3)
    pyautogui.click(119,217, duration=2)
    time.sleep(1)
    pyautogui.hotkey('Ctrl', 'v')
    # arrumando as bordas para sair igual
    pyautogui.click(224,101, duration=1)
    pyautogui.click(261,247, duration=1)
    pyautogui.click(224,101, duration=1)
    pyautogui.click(258,271, duration=1)
    # trocar de ponto para virgula no excel
    pyautogui.click(1300,97, duration=2)
    pyautogui.click(1236,158, duration=2)
    pyautogui.click(563,369, duration=2)
    pyautogui.write('.')
    pyautogui.click(539,392, duration=2)
    pyautogui.write(',')
    pyautogui.click(484,461, duration=2)
    pyautogui.click(685, 420, duration=2)
    pyautogui.click(913,299, duration=2)
    # mudança de função caso existam mais paginas
    time.sleep(2)
    if Numero_pag_int < 2:
        # excluir apenas as 4 linhas erradas
        pyautogui.moveTo(11, 216, duration=1)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.moveTo(13, 339, duration=1)
        pyautogui.mouseUp(button='left')
        pyautogui.rightClick(13, 339)
        pyautogui.click(72, 499, duration=1)
        # selecionar colunas para arrumar casas
        pyautogui.moveTo(184, 199, duration=1)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.moveTo(903, 196, duration=1)
        pyautogui.mouseUp(button='left')
        pyautogui.click(754, 102, duration=1)
        pyautogui.click(778, 102, duration=1)
        # selecionar e colar valores editados na tabela do Excel
        time.sleep(2)
        # mover de volta ao inicio para colar os valores copiados
        pyautogui.moveTo(1337, 690, duration=1)
        b = 0
        while b < 9:
            pyautogui.click()
            b += 1
        # Editar valor na função para subir ou diminuir a temperatura
        pyautogui.click(515, 219, duration=1)
        pyautogui.click(319, 164, duration=1)
        pyautogui.typewrite(Val)
        pyautogui.press('Enter')
        pyautogui.click(515, 219, duration=1)
        # arrastar para valer em todas as colunas
        pyautogui.moveTo(536, 228, duration=1)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(1240, 228, duration=1)
        pyautogui.mouseUp(button='left')
        pyautogui.doubleClick(1240, 228)
        # selecionar Valores editados para colar
        pyautogui.moveTo(502, 202, duration=1)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.moveTo(1211, 201, duration=1)
        pyautogui.mouseUp(button='left')
        pyautogui.hotkey('Ctrl', 'c')
        pyautogui.moveTo(842, 691, duration=1)
        b = 0
        while b < 9:
            pyautogui.click()
            b += 1
        pyautogui.click(187, 217, duration=1)
        pyautogui.rightClick(187, 217)
        time.sleep(1)
        pyautogui.click(256, 302)
        # editando celulas do filtro para reconhecer 30 S
        pyautogui.click(128, 205, duration=1)
        pyautogui.rightClick(128, 205, duration=1)
        pyautogui.click(205, 417, duration=1)
        time.sleep(3)
        # novo formato das células
        pyautogui.click(52, 404, duration=1)
        pyautogui.click(209, 323, duration=1)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.typewrite('dd/mm/aaaa hh:mm:ss,000')
        pyautogui.click(431, 611, duration=1)
        # clicando no filtro e selecionando o intervalo
        pyautogui.click(163, 218, duration=1)
        pyautogui.moveTo(181,361, duration=1)
        pyautogui.moveTo(364, 363, duration=1)
        pyautogui.click(368, 260)
        pyautogui.click(822, 318, duration=1)
        pyautogui.click(780, 334, duration=1)
        pyautogui.click(822, 363, duration=1)
        pyautogui.moveTo(823, 397, duration=1)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(822, 426, duration=1)
        pyautogui.mouseUp(button='left')
        pyautogui.click(746, 446, duration=1)
        pyautogui.click(741, 438, duration=1)
    else:
        # excluir apenas as 2 linhas erradas
        pyautogui.moveTo(11,216, duration=1)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.moveTo(11,239, duration=1)
        pyautogui.mouseUp(button='left')
        pyautogui.rightClick(11,239)
        pyautogui.click(70, 402, duration=1)
        # selecionar colunas para arrumar casas
        pyautogui.moveTo(184, 199, duration=1)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.moveTo(903, 196, duration=1)
        pyautogui.mouseUp(button='left')
        pyautogui.click(754, 102, duration=1)
        pyautogui.click(778, 102, duration=1)
        # selecionar e colar valores editados na tabela do Excel
        time.sleep(2)
        # mover de volta ao inicio para colar os valores copiados
        pyautogui.moveTo(1337, 690, duration=1)
        b = 0
        while b < 9:
            pyautogui.click()
            b += 1
        # Editar valor na função para subir ou diminuir a temperatura
        pyautogui.click(515, 219, duration=1)
        pyautogui.click(319, 164, duration=1)
        pyautogui.typewrite(Val)
        pyautogui.press('Enter')
        pyautogui.click(515, 219, duration=1)
        # arrastar para valer em todas as colunas
        pyautogui.moveTo(536, 228, duration=1)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(1240, 228, duration=1)
        pyautogui.mouseUp(button='left')
        pyautogui.doubleClick(1240, 228)
        # selecionar Valores editados para colar
        pyautogui.moveTo(502, 202, duration=1)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.moveTo(1211, 201, duration=1)
        pyautogui.mouseUp(button='left')
        pyautogui.hotkey('Ctrl', 'c')
        pyautogui.moveTo(842, 691, duration=1)
        b = 0
        while b < 9:
            pyautogui.click()
            b += 1
        pyautogui.click(187, 217, duration=1)
        pyautogui.rightClick(187, 217)
        time.sleep(1)
        pyautogui.click(256, 302)
        #adicionar o Filtro Corretamente
        pyautogui.click(130,201, duration=1)
        pyautogui.click(1230,83, duration=1)
        pyautogui.click(1128, 208, duration=1)
        pyautogui.click(1230,83, duration=1)
        pyautogui.click(1128, 208, duration=1)
        # editando celulas do filtro para reconhecer 30 S
        pyautogui.click(128, 205, duration=1)
        pyautogui.rightClick(128, 205, duration=1)
        pyautogui.click(205, 417, duration=1)
        time.sleep(3)
        # novo formato das células
        pyautogui.click(52, 404, duration=1)
        pyautogui.click(209, 323, duration=1)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.typewrite('dd/mm/aaaa hh:mm:ss,000')
        pyautogui.click(431, 611, duration=1)
        # clicando no filtro e selecionando o intervalo
        pyautogui.click(163, 218, duration=1)
        pyautogui.moveTo(181,361, duration=1)
        pyautogui.moveTo(364, 363, duration=1)
        pyautogui.click(368, 260)
        pyautogui.click(822, 318, duration=1)
        pyautogui.click(780, 334, duration=1)
        pyautogui.click(822, 363, duration=1)
        pyautogui.moveTo(823, 397, duration=1)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(822, 425, duration=1)
        pyautogui.mouseUp(button='left')
        pyautogui.click(717, 430, duration=1)
        pyautogui.click(741, 438, duration=1)

    # selecionar o espaço de uma página, copiar no word enquanto houver página
    time.sleep(1)
   # se o arquivo tiver apenas uma página, colar e formatar uma vez só
    if Numero_pag_int < 2:
        pyautogui.click(46, 217)
        pyautogui.moveTo(1219, 715, duration=1)
        pyautogui.click()
        pyautogui.moveTo(94, 200, duration=1)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.moveTo(363, 635, duration=1)
        pyautogui.mouseUp(button='left')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.moveTo(704, 746, duration=1)
        pyautogui.click()
        pyautogui.moveTo(303, 272, duration=1)
        pyautogui.click()
        pyautogui.rightClick()
        pyautogui.moveTo(435,357, duration=1)
        pyautogui.click()
        pyautogui.click(276,289)
        #formatar tabela
        pyautogui.moveTo(295,274, duration=1)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.moveTo(1023, 320, duration=1)
        pyautogui.mouseUp(button='left')
        pyautogui.click(967, 36, duration=1)
        pyautogui.click(707, 57, duration=1)
        pyautogui.click(130, 37, duration=1)
        # inserir Números no cabecalho
        pyautogui.click(305,247, duration=1)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write('001')
        pyautogui.click(369,248, duration=1)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write('002')
        pyautogui.click(432,247, duration=1)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write('003')
        pyautogui.click(498,247)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write('004')
        pyautogui.click(562,246)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write('005')
        pyautogui.click(625,245, duration=1)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write('006')
        pyautogui.click(690,246)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write('007')
        pyautogui.click(753,246)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write('008')
        pyautogui.click(817,245)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write('009')
        pyautogui.click(880,246)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write('010')
        pyautogui.click(945,246)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write('011')
        pyautogui.click(1010,245)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write('012')
    else:  # se tiver mais páginas repetir o processo de colar e formatar as páginas em quanto houver Páginas
        pyautogui.click(46, 217)
        pyautogui.moveTo(1219, 715, duration=1)
        pyautogui.click()
        rep_copia_pag = 0
        Parar_Copia = 1
        time.sleep(2)
        while rep_copia_pag < Numero_pag_int:
            pyautogui.moveTo(94, 200, duration=1)
            pyautogui.mouseDown(button='left')
            time.sleep(1)
            pyautogui.moveTo(363, 635, duration=1)
            pyautogui.mouseUp(button='left')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.moveTo(704, 746, duration=1)
            pyautogui.click()
            pyautogui.moveTo(303, 272, duration=1)
            pyautogui.click()
            pyautogui.rightClick()
            pyautogui.moveTo(435,357, duration=1)
            pyautogui.click()
            pyautogui.click(276,289)
            #formatar tabela
            pyautogui.moveTo(295,274, duration=1)
            pyautogui.mouseDown(button='left')
            time.sleep(1)
            pyautogui.moveTo(1023, 320, duration=1)
            pyautogui.mouseUp(button='left')
            pyautogui.click(967, 36, duration=1)
            pyautogui.click(707, 57, duration=1)
            pyautogui.click(130, 37, duration=1)
            # inserir Números no cabecalho
            pyautogui.click(305,247, duration=1)
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.write('001')
            pyautogui.click(369,248, duration=1)
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.write('002')
            pyautogui.click(432,247, duration=1)
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.write('003')
            pyautogui.click(498,247)
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.write('004')
            pyautogui.click(562,246)
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.write('005')
            pyautogui.click(625,245, duration=1)
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.write('006')
            pyautogui.click(690,246)
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.write('007')
            pyautogui.click(753,246)
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.write('008')
            pyautogui.click(817,245)
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.write('009')
            pyautogui.click(880,246)
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.write('010')
            pyautogui.click(945,246)
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.write('011')
            pyautogui.click(1010,245)
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.write('012')
        # descer para a proxima tabela word
            if Parar_Copia < Numero_pag_int:
                time.sleep(1)
                pyautogui.press('pgdn')
                pyautogui.press('pgdn')
                # descer para a proxima tabela Excel
                pyautogui.click(385, 749, duration=1)
                pyautogui.press('pgdn')
                # posicionar a tabela para copiar novamente
                pyautogui.click(1354,197, duration=1)
                pyautogui.click(1354,197, duration=1)
                pyautogui.click(1354,197, duration=1)
                pyautogui.click(1354,197, duration=1)
                pyautogui.click(1354,197, duration=1)
                Parar_Copia += 1
            rep_copia_pag += 1
    # substituir Virgula por ponto no Word Tabela
    pyautogui.click(1268,88, duration=1)
    pyautogui.click(130,566, duration=1)
    pyautogui.write(',')
    pyautogui.click(116,623, duration=1)
    pyautogui.write('.')
    pyautogui.click(302,683, duration=1)
    time.sleep(5)
    pyautogui.click(686,426, duration=1)
    pyautogui.click(545,496, duration=1)
    # imprimir pdf da Tabela
    pyautogui.click(30,35, duration=1)
    pyautogui.click(47,272, duration=1)
    pyautogui.click(243,414, duration=1)
    pyautogui.typewrite('1')
    pyautogui.typewrite('-')
    pyautogui.typewrite(Numero_Pag)
    pyautogui.click(212,171, duration=1)
    time.sleep(20)
    pyautogui.click(854,638, duration=1)
    time.sleep(5)
    # fechar PDF gerado e voltar a pagina inicial do site
    pyautogui.click(471,15, duration=1)
    pyautogui.click(20,50, duration=1)
    # voltar e fechar o word
    pyautogui.click(703,748, duration=1)
    pyautogui.click(1354,8, duration=1)
    pyautogui.click(682,410, duration=1)
    # subir para o inicio do Excel e editar filtro
    pyautogui.click(390,744, duration=1)
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    # clicando no Filtro e definindo horario do inicio do processo
    pyautogui.click(68,200, duration=1)
    pyautogui.moveTo(94, 337, duration=1)
    pyautogui.moveTo(364, 363, duration=1)
    pyautogui.click(363, 258)
    pyautogui.click(822,320, duration=1)
    pyautogui.click(758, 336, duration=1)
    time.sleep(1)
    pyautogui.click(782,320, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.typewrite(Inicio_processo)
    # definindo o horario do fim do processo
    pyautogui.click(822,363, duration=1)
    pyautogui.click(782,379, duration=1)
    time.sleep(1)
    pyautogui.click(783,363, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.typewrite(Fim_processo)
    pyautogui.click(743,439, duration=1)
    # abrir e Excluir arquivos nos dowloads e fechar pagina de downloads
    pyautogui.moveTo(454,744)
    time.sleep(1)
    pyautogui.click(512,651)
    pyautogui.click(296,70, duration=1)
    pyautogui.press('Del')
    pyautogui.press('f11')
    pyautogui.click(1343,7, duration=1)
    # abrir e excluir Tabela Obsoleta
    pyautogui.click(451,746, duration=1)
    time.sleep(2)
    pyautogui.click(291,216, duration=1)
    pyautogui.press('Del')
    pyautogui.click(1338,8, duration=1)
    # Abrir pasta onde estão od Gráficos
    path = 'C:/Users/Bruno Neves/Desktop/Teste/Coletas processadas/Obsoletos/Gráficos'
    webbrowser.open('file:///' + path)
    time.sleep(2)
    pyautogui.keyDown('f11')
    pyautogui.keyUp('f11')
    # selecionar, arrastar e converter o arquvio
    pyautogui.moveTo(286,70, duration=3)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.keyDown('f11')
    pyautogui.keyUp('f11')
    time.sleep(1)
    pyautogui.moveTo(663, 743, 1)
    time.sleep(1)
    pyautogui.moveTo(518, 414, 1)
    pyautogui.mouseUp(button='left')
    time.sleep(1)
    pyautogui.click(1178, 618, 2)
    time.sleep(4)
    # abrir arquivo seleionar e copiar dados
    path = 'C:/Users/Bruno Neves/Downloads/Coletas a Editar'
    webbrowser.open('file:///' + path)
    time.sleep(4)
    pyautogui.keyDown('f11')
    pyautogui.keyUp('f11')
    time.sleep(4)
    pyautogui.doubleClick(285, 71,)
    time.sleep(6)
    pyautogui.click(1170, 37, 2)
    # selecionar e mudar os sensores na tabelinha
    pyautogui.click(226, 273, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('001')
    pyautogui.click(227, 285, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('002')
    pyautogui.click(227, 296, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('003')
    pyautogui.click(227, 310, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('004')
    pyautogui.click(227, 320, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('005')
    pyautogui.click(226, 330, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('006')
    pyautogui.click(226, 342, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('007')
    pyautogui.click(227, 353, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('008')
    pyautogui.click(227, 365, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('009')
    pyautogui.click(227, 376, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('010')
    pyautogui.click(227, 388, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('011')
    pyautogui.click(226, 399, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('012')
    # mudar sensores no canto da página
    pyautogui.click(1183, 449, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('001')
    pyautogui.click(1183, 457, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('002')
    pyautogui.click(1183, 466, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('003')
    pyautogui.click(1183, 475, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('004')
    pyautogui.click(1183, 482, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('005')
    pyautogui.click(1183, 493, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('006')
    pyautogui.click(1183, 501, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('007')
    pyautogui.click(1183, 509, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('008')
    pyautogui.click(1183, 517, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('009')
    pyautogui.click(1183, 524, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('010')
    pyautogui.click(1183, 534, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('011')
    pyautogui.click(1183, 543, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('012')
    # abrir excel e ir na planilha com os dados das Tabelas
    pyautogui.click(392,747, duration=1)
    pyautogui.click(188,689, duration=1)
    # substituir C por C2 na formula
    pyautogui.click(1298,91, duration=2)
    pyautogui.click(1272, 154, duration=2)
    pyautogui.click(539,395, duration=2)
    pyautogui.press('backspace')
    pyautogui.write('1:')
    pyautogui.moveTo(540,421)
    pyautogui.click(540,421, duration=2)
    pyautogui.press('backspace')
    pyautogui.write('2:')
    pyautogui.click(480,490, duration=2)
    pyautogui.click(684,421, duration=2)
    pyautogui.click(914,327, duration=2)
    # Copiar tabela do Excel
    pyautogui.moveTo(601,244, duration=1)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.moveTo(903,497, duration=1)
    pyautogui.mouseUp(button='left')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    # abrir word Gráfico e Colar Tabela
    pyautogui.click(706, 745, duration=1)
    pyautogui.moveTo(310,275, duration=1)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.moveTo(539,400, duration=1)
    pyautogui.mouseUp(button='left')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(1020,86, duration=1)
    pyautogui.click(311,73, duration=1)
    pyautogui.write('5')
    pyautogui.press('Enter')
    # substituir Virgula por ponto no Word Tabela
    pyautogui.click(125, 33, duration=1)
    pyautogui.click(1266, 83, duration=1)
    pyautogui.write(',')
    pyautogui.click(113, 623, duration=1)
    pyautogui.write('.')
    pyautogui.click(297, 684, duration=1)
    time.sleep(2)
    pyautogui.click(733,430, duration=1)
    pyautogui.click(544, 495, duration=1)
    # imprimir pdf do Gráfico
    pyautogui.click(26, 33, duration=1)
    pyautogui.click(43, 270, duration=1)
    pyautogui.click(208, 156, duration=1)
    time.sleep(3)
    pyautogui.click(851, 638, duration=1)
    time.sleep(3)
    # fechar PDF gerado e voltar a pagina inicial do site
    pyautogui.click(469, 14, duration=1)
    pyautogui.click(19, 48, duration=1)
    # voltar e fechar o word
    pyautogui.click(697, 748, duration=1)
    pyautogui.click(1351, 8, duration=1)
    pyautogui.click(681, 408, duration=1)
    # abrir e Excluir arquivos nos dowloads e fechar pagina de downloads
    pyautogui.moveTo(454,744)
    time.sleep(1)
    pyautogui.click(512,651)
    pyautogui.click(296,70, duration=1)
    pyautogui.press('Del')
    pyautogui.press('f11')
    pyautogui.click(1343,7, duration=1)
    # abrir e excluir Gráfico Obsoleta
    pyautogui.click(451,746, duration=1)
    time.sleep(2)
    pyautogui.click(291,216, duration=1)
    pyautogui.press('Del')
    pyautogui.click(1338,8, duration=1)
    # fechar Excel
    pyautogui.click(390,747, duration=1)
    pyautogui.click(1349,8, duration=1)
    pyautogui.click(681,410, duration=1)
    num_ciclos += 1