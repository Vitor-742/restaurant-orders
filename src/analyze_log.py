import csv
from collections import Counter
import os.path


def verify_file(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    if not os.path.isfile(path_to_file):
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def post_text(pratos_maria, arnaldo_hamburguer, joao_pratos, joao_dias):
    with open('data/mkt_campaign.txt', 'w') as file:
        lines = [
            list(Counter(pratos_maria))[0] + '\n',
            str(arnaldo_hamburguer) + '\n',
            str(joao_pratos) + '\n',
            str(joao_dias) + '\n',
        ]
        file.writelines(lines)


def count_joao(row):
    joao_dias = {'segunda-feira', 'terça-feira', 'sabado'}
    joao_pratos = {'hamburguer', 'pizza', 'coxinha', 'misto-quente'}
    if row[2] in joao_dias:
        joao_dias.remove(row[2])
    if row[1] in joao_pratos:
        joao_pratos.remove(row[1])
    return [joao_pratos, joao_dias]


def analyze_log(path_to_file):
    verify_file(path_to_file)
    pratos_maria = []
    arnaldo_hamburguer = 0
    with open(path_to_file) as file:
        csv_reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in csv_reader:
            if row[0] == 'maria':
                pratos_maria.append(row[1])
            if row[0] == 'arnaldo' and row[1] == 'hamburguer':
                arnaldo_hamburguer += 1
            if row[0] == 'joao':
                joao = count_joao(row)
    post_text(pratos_maria, arnaldo_hamburguer, joao[0], joao[1])
