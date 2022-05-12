import re
from datetime import datetime

def validar_cpf(cpf):
    cpf = ''.join(re.findall(r'\d', str(cpf)))
    if not cpf or len(cpf) < 11:
        return False
    antigo = [int(d) for d in cpf]
    novo = antigo[:9]
    while len(novo) < 11:
        resto = sum([v * (len(novo) + 1 - i) for i, v in enumerate(novo)]) % 11
        digito_verificador = 0 if resto <= 1 else 11 - resto
        novo.append(digito_verificador)
    if novo == antigo:
        return True
    return False



def str2date(value, frmt='%d/%m/%Y'):
    try:
        return datetime.strptime(value, frmt)
    except Exception as err:
        print('exception converting str {} to date ... {}'.format(value, err))
    return False


def date2str(value, frmt='%d/%m/%Y'):
    try:
        return datetime.strftime(value, frmt)
    except Exception as err:
        print('exception converting datetime {} to str ... {}'.format(value, err))
    return False