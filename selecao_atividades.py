# Estas funções informam ao sorted qual campo usar na ordenação.
def obter_termino(atividade):
    return atividade["termino"]


def obter_inicio(atividade):
    return atividade["inicio"]


def selecionar_por_termino(atividades):
    # Quem termina primeiro
    atividades_ordenadas = sorted(atividades, key=obter_termino)
    selecionadas = []
    ultimo_termino = None

    for atividade in atividades_ordenadas:
        # Aceita a primeira atividade ou uma que não sobreponha a última.
        if ultimo_termino is None or atividade["inicio"] >= ultimo_termino:
            selecionadas.append(atividade)
            ultimo_termino = atividade["termino"]

    return selecionadas


def selecionar_por_inicio(atividades):
    # Quem começa primeiro
    atividades_ordenadas = sorted(atividades, key=obter_inicio)
    selecionadas = []
    ultimo_termino = None

    for atividade in atividades_ordenadas:
        # A regra de compatibilidade é a mesma entre as duas
        if ultimo_termino is None or atividade["inicio"] >= ultimo_termino:
            selecionadas.append(atividade)
            ultimo_termino = atividade["termino"]

    return selecionadas


def mostrar_atividades(atividades):
    for atividade in atividades:
        print(
            atividade["nome"],
            "| início:", atividade["inicio"],
            "| término:", atividade["termino"]
        )

    print("Quantidade:", len(atividades))


def executar_exemplo(titulo, atividades):
    print("\n" + titulo)
    print("\nAtividades disponíveis:")
    mostrar_atividades(atividades)

    selecionadas_por_termino = selecionar_por_termino(atividades)
    print("\nEstratégia: termina primeiro")
    mostrar_atividades(selecionadas_por_termino)

    selecionadas_por_inicio = selecionar_por_inicio(atividades)
    print("\nEstratégia: começa primeiro")
    mostrar_atividades(selecionadas_por_inicio)


def main():
    # Exemplo em que começar primeiro impede as outras
    atividades_exemplo_1 = [
        {"nome": "A", "inicio": 0, "termino": 10},
        {"nome": "B", "inicio": 1, "termino": 3},
        {"nome": "C", "inicio": 3, "termino": 5},
        {"nome": "D", "inicio": 5, "termino": 7}
    ]

    # Exemplo em que as duas estratégias encontram a mesma quantidade
    atividades_exemplo_2 = [
        {"nome": "A", "inicio": 4, "termino": 6},
        {"nome": "B", "inicio": 0, "termino": 2},
        {"nome": "C", "inicio": 2, "termino": 4},
        {"nome": "D", "inicio": 1, "termino": 5}
    ]

    executar_exemplo("EXEMPLO 1", atividades_exemplo_1)
    executar_exemplo("EXEMPLO 2", atividades_exemplo_2)


if __name__ == "__main__":
    main()
