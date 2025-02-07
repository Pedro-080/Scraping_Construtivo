import pandas as pd
print (pd.__version__)

import requests

# URL da página de login
login_url = 'https://ctg.construtivo.com'

# Credenciais de login
username = 'gel.salatec'
password = 'aA1795848@'

# Dados do formulário de login
login_data = {
    'username': username,  # Substitua pelo nome do campo de usuário
    'password': password,  # Substitua pelo nome do campo de senha
    # Adicione outros campos necessários (como tokens CSRF, se houver)
}

# Iniciar uma sessão para manter os cookies
session = requests.Session()

# Fazer a requisição POST para o login
response = session.post(login_url, data=login_data)

# Verificar se o login foi bem-sucedido
if response.status_code == 200:
    print("Login realizado com sucesso!")
    
    # Verificar se estamos autenticados tentando acessar uma página restrita
    restricted_url = 'https://exemplo.com/pagina_restrita'
    response = session.get(restricted_url)
    
    if response.status_code == 200:
        print("Acesso à página restrita concedido!")
    else:
        print("Falha ao acessar a página restrita. Verifique as credenciais.")
else:
    print("Falha no login. Verifique as credenciais e os dados do formulário.")