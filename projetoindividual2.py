def contar_inscritos(interessados):
    inscritos = {}
    for nome, vaga in interessados.keys():
        inscritos[vaga] = inscritos.get(vaga, 0) + 1
    return inscritos

def contar_aprovados(interessados, palavras_chave):
    aprovados = {}
    for nome, vaga in interessados.keys():
        resumo = interessados[(nome, vaga)]
        if any(palavra in resumo for palavra in palavras_chave[vaga]):
            aprovados[vaga] = aprovados.get(vaga, 0) + 1
    return aprovados

def imprimir_aprovados(interessados, palavras_chave):
    for vaga in palavras_chave.keys():
        aprovados = [nome for (nome, v) in interessados.keys() if v == vaga and any(p in interessados[(nome, v)] for p in palavras_chave[vaga])]
        print(f'Candidatos aprovados para a {vaga}:')
        for nome in aprovados:
            print(nome)

interessados = {}
palavras_chave = {
    'vaga 1': ['python', 'programação', 'desenvolvimento'],
    'vaga 2': ['análise de dados', 'dados', 'sql']
}

print('Digite "0" para encerrar a inscrição de candidatos.')
while True:
    nome = input('Digite o nome do candidato: ')
    if nome == '0':
        break
    vaga = input('Digite a vaga desejada (vaga 1 ou vaga 2): ')
    while vaga not in palavras_chave.keys():
        vaga = input('Vaga inexistente. Digite novamente a vaga desejada (vaga 1 ou vaga 2): ')
    resumo = input('Digite um resumo do currículo do candidato: ')
    interessados[(nome, vaga)] = resumo
    print(f'Candidato {nome} inscrito na {vaga} com sucesso!')

inscritos = contar_inscritos(interessados)
for vaga, n in inscritos.items():
    print(f'{n} candidatos inscritos para a {vaga}')

aprovados = contar_aprovados(interessados, palavras_chave)
for vaga, n in aprovados.items():
    print(f'{n} candidatos aprovados para a {vaga}')

imprimir_aprovados(interessados, palavras_chave)



