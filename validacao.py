from models import get_estado

def valida_estado(sigla, nome):
    if len(sigla) != 2:
        return False

    if len(nome) == 0:
        return False

    estado = get_estado(sigla)
    if len(estado) > 0:
        return False

    return True
