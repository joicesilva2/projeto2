# projeto2
O código apresentado é um programa para gerenciar inscrição de candidatos em vagas de emprego e filtrar os candidatos aprovados de acordo com palavras-chave definidas para cada vaga.

O programa começa criando um dicionário vazio chamado "interessados" e outro dicionário "palavras_chave" que contém as palavras-chave para cada vaga.

Em seguida, o programa entra em um loop infinito que permite ao usuário inserir informações sobre os candidatos. O programa solicita o nome do candidato, a vaga desejada e um resumo do currículo do candidato. O programa armazena essas informações no dicionário "interessados" como uma chave composta pelo nome e pela vaga.

Depois que as inscrições são encerradas, o programa chama a função "contar_inscritos" para contar o número de inscritos em cada vaga. Em seguida, o programa exibe o número de inscritos para cada vaga.

Em seguida, o programa chama a função "contar_aprovados" para contar o número de candidatos aprovados em cada vaga. Para isso, a função verifica se alguma das palavras-chave comprovadas para a vaga está presente no resumo do currículo do candidato. Em seguida, o programa exibe o número de candidatos aprovados para cada vaga.

Por fim, o programa chama a função "imprimir_aprovados" para imprimir uma lista dos candidatos aprovados para cada vaga. A função percorreu todas as chaves do dicionário "palavras_chave" e para cada vaga, verifica se o candidato é aprovado. Se for, o programa adiciona o nome do candidato à lista de aprovados. A função imprime a lista de candidatos aprovados para cada vaga.
