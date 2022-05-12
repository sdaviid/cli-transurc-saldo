import argparse
from core.transurc import transurc

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--cpf', '--documento', '--doc', type=str, required=True, help='CPF do titular')
    parser.add_argument('--nascimento', type=str, required=True, help='Nascimento do titular (DD/MM/YYYY)')
    args = parser.parse_args()
    inst_transurc = transurc(cpf=args.cpf, nascimento=args.nascimento)
    inst_transurc.consultar()