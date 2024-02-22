print('Calculadora de Notas')
print('--------------------------')


def estruturaDeDados():
    print('Nota em Estrutura de Dados')

    p1 = float(input("Nota da primeira prova: "))
    p2 = float(input("Nota da segunda prova: "))
    api = float(input("Nota do trabalho prático: "))
   
    notaProvas = int(p1 + (p2*2))/ 3
    
    if notaProvas >= 6:
        print('Aprovada nas provas')
        notaFinal = (api + (notaProvas*2))/ 3
        print(f'Nota final {notaFinal:.1f}')
    else: 
        print('Reprovada')
        print(f'Nota final {notaFinal:.1f}')

estruturaDeDados()


""" def sistemasOperacionais():
    print('Nota em Sistemas Operacionais')
    p1 = float(input("Nota da primeira prova: "))
    p2 = float(input("Nota da segunda prova: "))
    atv =  float(input("Nota das atividades avaliativas: ")) #verificar quanto vale cada atividade
    api = float(input("Nota do trabalho prático: "))

    porcentagemProvas = (p1 + p2)*0.5
    porcentagemAPI = api*0.25
    porcentagemAtividades = atv*0.25
    notaFinal = porcentagemProvas + porcentagemAPI + porcentagemAtividades #descobrir cálculo final

    if notaFinal >= 6:
        print('Aprovada nas provas')
        print(f'Nota final {notaFinal:.1f}')
    else: 
        print('Reprovada')
        print(f'Nota final {notaFinal:.1f}')

sistemasOperacionais() """

""" def engenhariaSoftware():
    print('Nota em Engenharia de Software')
    atv =  float(input("Nota das atividades avaliativas: ")) #verificar quanto vale cada atividade
    api = float(input("Nota do trabalho prático: "))

    notaFinal = api + atv

    if api < 7:
        notaFinal = atv
        print('Aprovada nas provas')
        print(f'Nota final {notaFinal:.1f}')
    elif api >= 7: 
        print(f'Nota final {notaFinal:.1f}')
    else: 
        print('Reprovada')
        print(f'Nota final {notaFinal:.1f}')
        
engenhariaSoftware()  """

""" def progOrientada():
    print('Nota em Programação Orientada a Objetos')
    t1 =  float(input("Nota das atividade 1: ")) #verificar quanto vale cada atividade
    t2 =  float(input("Nota das atividade 2: "))
    t3 =  float(input("Nota das atividade 3: "))
    t4 =  float(input("Nota das atividade 4: "))
    t5 =  float(input("Nota das atividade 5: "))
    ap1 = float(input("Nota do trabalho prático: "))
    pn = int(input("Pontos perdidos por atraso: "))

    notaFinal = float((0.5*(0.3*t1 + 0.1*t2 + 0.2*t3 + 0.2*t4 + 0.2*t5)) + 0.5*ap1) - pn

    if notaFinal >= 6:
        print('Aprovada nas provas')
        print(f'Nota final {notaFinal:.1f}')
    else: 
        print('Reprovada')
        print(f'Nota final {notaFinal:.1f}')
        
progOrientada()  """