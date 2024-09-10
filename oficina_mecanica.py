import pandas as pd

# Tabela de Clientes
clientes = pd.DataFrame(columns=['ID_Cliente', 'Nome', 'Endereço', 'Telefone', 'Email'])

# Tabela de Veículos
veiculos = pd.DataFrame(columns=['ID_Veículo', 'ID_Cliente', 'Marca', 'Modelo', 'Ano', 'Placa'])

# Tabela de Serviços
servicos = pd.DataFrame(columns=['ID_Serviço', 'Descrição', 'Preço'])

# Tabela de Ordens de Serviço
ordens_servico = pd.DataFrame(columns=['ID_Ordem', 'ID_Cliente', 'ID_Veículo', 'Data_Início', 'Data_Término', 'Valor_Total'])

# Tabela de Detalhes da Ordem de Serviço
detalhes_ordem = pd.DataFrame(columns=['ID_Detalhe', 'ID_Ordem', 'ID_Serviço', 'Quantidade', 'Subtotal'])

# Tabela de Peças
pecas = pd.DataFrame(columns=['ID_Peça', 'Nome', 'Descrição', 'Preço', 'Quantidade_Estoque'])

# Tabela de Uso de Peças
uso_pecas = pd.DataFrame(columns=['ID_Uso', 'ID_Ordem', 'ID_Peça', 'Quantidade', 'Subtotal'])



# Adicionando um cliente
clientes = clientes.append({
    'ID_Cliente': 1,
    'Nome': 'João Silva',
    'Endereço': 'Rua A, 123',
    'Telefone': '(11) 99999-9999',
    'Email': 'joao@example.com'
}, ignore_index=True)

# Adicionando um veículo
veiculos = veiculos.append({
    'ID_Veículo': 1,
    'ID_Cliente': 1,
    'Marca': 'Toyota',
    'Modelo': 'Corolla',
    'Ano': 2015,
    'Placa': 'ABC-1234'
}, ignore_index=True)

# Adicionando algumas peças
pecas = pecas.append({
    'ID_Peça': 1,
    'Nome': 'Filtro de óleo',
    'Descrição': 'Filtro de óleo de motor',
    'Preço': 30.00,
    'Quantidade_Estoque': 3
}, ignore_index=True)

pecas = pecas.append({
    'ID_Peça': 2,
    'Nome': 'Pastilha de freio',
    'Descrição': 'Pastilha de freio dianteira',
    'Preço': 80.00,
    'Quantidade_Estoque': 2
}, ignore_index=True)

pecas = pecas.append({
    'ID_Peça': 3,
    'Nome': 'Correia dentada',
    'Descrição': 'Correia dentada de motor',
    'Preço': 120.00,
    'Quantidade_Estoque': 7
}, ignore_index=True)

pecas_em_falta = pecas[pecas['Quantidade_Estoque'] < 5]
print('Peças com estoque baixo:')
print(pecas_em_falta)