def estado_from_web(**kwargs):
    return {
        "sigla": kwargs["sigla"] if kwargs["sigla"] else "",
        "nome": kwargs["nome"] if kwargs["nome"] else "",
    }

def estado_from_db(*args):
    return {
        "sigla": args[0],
        "nome": args[1],
    }