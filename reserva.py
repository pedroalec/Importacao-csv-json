import csv
import json

def csv_para_json_debug(caminho_csv, caminho_json):
    with open(caminho_csv, encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        
        print("Colunas detectadas no CSV:")
        print(leitor.fieldnames)  # Mostra exatamente as colunas do CSV

        resultados = []

        for idx, linha in enumerate(leitor, start=1):
            print(f"\nLinha {idx}:")
            for k, v in linha.items():
                print(f"  {repr(k)} : {repr(v)}")
            
            registro = {
                'nome': linha.get('Nome Completo', '').strip(),
                'cpf': linha.get('CPF', '').strip(),
                'email': linha.get('E-mail', '').strip(),
                'telefone': linha.get('Telefone', '').strip(),
                'cargo': linha.get('Cargo', '').strip(),
                'setor': linha.get('Setor', '').strip(),
                'data_nascimento': linha.get('Data de Nascimento', '').strip(),
                'contato_emergencia_nome': linha.get('Contato de Emergencia (Nome)', '').strip(),
                'contato_emergencia_telefone': linha.get('Contato de Emergencia (Telefone)', '').strip(),
            }

            resultados.append(registro)

        with open(caminho_json, 'w', encoding='utf-8') as jsonfile:
            json.dump(resultados, jsonfile, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    csv_para_json_debug("importacao_dp.csv", "funcionarios.json")
