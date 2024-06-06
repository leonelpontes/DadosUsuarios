from rich.console import Console
from rich.table import Table

console = Console()

def get_user_data():
  users = []
  while True:
    nome = input("Digite o nome: (ou 'ok' para encerrar)")
    if nome.lower() == 'ok':
      break
    idade = input("Digite a idade: ")
    email = input("Digite seu email: ")

    try:
      idade = int(idade)
    except ValueError:
      console.print("[bold red]Idade inválida. Entre com os teclados númericos corretos.[/bold red]")
      continue

  users.append({"Nome": nome, "Idade": idade, "Email": email})

  return users

users = get_user_data()

table = Table(title="User Information")

table.add_column("Nome", justify="left", style="cyan", no_wrap=True)
table.add_column("Idade", justify="right", style="magenta")
table.add_column("Email", justify="left", style="green")

for user in users:
  table.add_row(user["Nome"], str(user["Idade"]), user["Email"])

console.print(table)