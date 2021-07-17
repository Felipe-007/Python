import requests

def main():
    print('##################')
    print('## Consulta CEP ##')
    print('##################')
    print()

    cep_input = input('Digite um CEP para a consulta: ')
    if len(cep_input) != 8:
        print('Quantidade de digitos inválida')
        exit()

    request = requests.get(f'https://viacep.com.br/ws/{cep_input}/json')

    address_data = request.json()

    if 'erro' not in address_data:
        print('==> CEP ENCONTRADO <==')

        print(f'CEP: {address_data["cep"]}')
        print(f'Logradouro: {address_data["logradouro"]}')
        print(f'Complemento: {address_data["complemento"]}')
        print(f'Bairro: {address_data["bairro"]}')
        print(f'Cidade: {address_data["localidade"]}')
        print(f'Estado: {address_data["uf"]}')

    else:
        print(f'{cep_input} CEP inválido.')

    print('------------------------')

    option = int(input('Deseja realizar uma nova consulta?\n1. Sim\n2. Sair'))
    if option == 1:
        main()
    else:
        print('Saindo...')

if __name__ == '__main__':
    main()