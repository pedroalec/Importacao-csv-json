import csv
from datetime import datetime
import json

def csv_para_json(caminho_csv, caminho_json):
    funcionarios = []

    with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        for row in leitor:
            funcionario = {
                "nome": row.get("Nome Completo", "").strip(),
                "cpf": row.get("CPF", "").strip(),
                "email": row.get("E-mail", "").strip(),
                "telefone": row.get("Telefone", "").strip(),
                "cargo": row.get("Cargo", "").strip(),
                "setor": row.get("Setor", "").strip(),
                "data_nascimento": "",
                "contato_emergencia_nome": row.get("Contato de Emergencia (Nome)", "").strip(),
                "contato_emergencia_telefone": row.get("Contato de Emergencia (Telefone)", "").strip(),
            }

            # Converter data de nascimento para formato ISO YYYY-MM-DD
            data_nasc = row.get("Data de Nascimento", "").strip()
            if data_nasc:
                try:
                    dt = datetime.strptime(data_nasc, "%d/%m/%Y")
                    funcionario["data_nascimento"] = dt.strftime("%Y-%m-%d")
                except Exception:
                    funcionario["data_nascimento"] = ""

            funcionarios.append(funcionario)

    with open(caminho_json, "w", encoding='utf-8') as jsonfile:
        json.dump(funcionarios, jsonfile, ensure_ascii=False, indent=4)

    print(f"Arquivo JSON gerado: {caminho_json}")
