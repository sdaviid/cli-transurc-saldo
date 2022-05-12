import requests
from utils.utils import(
    validar_cpf,
    str2date,
    date2str
)




class transurc(object):
    def __init__(self, cpf, nascimento):
        self.cpf = cpf
        self.nascimento = nascimento
        self.formatar_dados()
    def formatar_dados(self):
        cpf = self.cpf.replace('.', '').replace(',', '')
        nascimento = str2date(self.nascimento)
        if validar_cpf(cpf) == True and nascimento != False:
            self.cpf = cpf
            self.nascimento = nascimento
        else:
            raise ValueError('Dados invalidos')
    def consultar(self):
        resposta_consulta = self.consultar_saldo()
        if isinstance(resposta_consulta, requests.models.Response):
            self.exibir_detalhes(resposta_consulta)
        else:
            print('falha ao consultar dados cpf {} nascimento {}'.format(self.cpf, self.nascimento))
    def consultar_saldo(self):
        nascimento_str = date2str(self.nascimento, frmt='%Y-%m-%d')
        url = 'https://api.transurc.com.br/consultas/cartao/getsaldo'
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Authorization': 'Basic c2FsZG86ZVE4YkY2SCY/eUAhRFI=',
            'Content-Type': 'application/json',
            'Host': 'api.transurc.com.br',
            'Origin': 'https://servicos.transurc.com.br',
            'Referer': 'https://servicos.transurc.com.br/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
        }
        payload = {
            'consentimento': True,
            'cpf': self.cpf,
            'imei': '0',
            'latitude': 0,
            'longitude': 0,
            'nascimento': nascimento_str,
            'recaptchaReactive': '',
            'sistema': 'WEB'
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                return response
            else:
                raise Exception('Consulta retornou status != 200 - {}'.format(response.status_code))
        except Exception as err:
            print('exception on transurc.consultar_saldo ... {}'.format(err))
        return False
    def exibir_detalhes(self, resposta_consulta):
        resposta_json = resposta_consulta.json()
        print('Nome\t{}'.format(resposta_json.get('nome', False)))
        print('Total Cartoes\t{}\n'.format(len(resposta_json.get('cartoes', []))))
        cartao_index = 1
        for cartao in resposta_json.get('cartoes', []):
            print('#{} - Numero {}\tTipo {}\tSaldo {}\tCompras {}'.format(cartao_index, cartao.get('nrExtenso', False), \
                                                cartao.get('aplicacao', False), cartao.get('saldo', False), \
                                                len(cartao.get('compras', []))))
            cartao_index += 1