import requests

class BuscaEndereco:
    def __init__(self, cep):
        self.cep_ok = cep

    def __str__(self):
        return self.cep_validao()['cep']

    def cep_validao(self):
        try:
            r = requests.get(f'https://viacep.com.br/ws/{self.cep_ok}/json/')

            if 'erro' in r.json():
                print('CEP não existe')
                exit()
            else:
                return r.json()

        except Exception:
            print('CEP Inválido')
            exit()

    def endereco(self):
        rua = self.cep_validao()['logradouro']
        bairro = self.cep_validao()['bairro']
        cidade = self.cep_validao()['localidade']
        uf = self.cep_validao()['uf']

        dados = f'CEP: {self}\n' \
                f'Rua: {rua}\n' \
                f'Bairro: {bairro}\n' \
                f'Cidade: {cidade}\n' \
                f'Estado: {uf}'

        return dados
