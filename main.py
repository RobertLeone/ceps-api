from acesso_cep import BuscaEndereco

cep = '01001000'
cep_obj = BuscaEndereco(cep)

print(cep_obj.endereco())