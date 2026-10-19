import random
import time

from selecao_atividades import (
    obter_inicio,
    obter_termino,
    selecionar_por_inicio,
    selecionar_por_termino,
    mostrar_atividades
)


def gerar_atividades(quantidade_blocos):
    # Cada bloco vai ter uma atividade longa e três curtas
    atividades = []

    for bloco in range(quantidade_blocos):
        inicio_bloco = bloco * 10
        numero = str(bloco + 1)

        atividades.append({
            "nome": "Longa " + numero,
            "inicio": inicio_bloco,
            "termino": inicio_bloco + 10
        })
        atividades.append({
            "nome": "Curta B " + numero,
            "inicio": inicio_bloco + 1,
            "termino": inicio_bloco + 3
        })
        atividades.append({
            "nome": "Curta C " + numero,
            "inicio": inicio_bloco + 3,
            "termino": inicio_bloco + 5
        })
        atividades.append({
            "nome": "Curta D " + numero,
            "inicio": inicio_bloco + 5,
            "termino": inicio_bloco + 7
        })

    random.seed(15)
    random.shuffle(atividades)

    return atividades


def mostrar_decisoes(atividades_ordenadas, selecionadas):
    # Explica as decisões usando o resultado do algoritmo

    ultimo_termino = None

    for atividade in atividades_ordenadas:
        print(
            atividade["nome"],
            "| início:", atividade["inicio"],
            "| término:", atividade["termino"]
        )

        if atividade in selecionadas:
            if ultimo_termino is None:
                print("  Selecionada: é a primeira atividade da ordenação.")
            else:
                print(
                    "  Selecionada: começa em", atividade["inicio"],
                    "e a última selecionada termina em", ultimo_termino
                )

            ultimo_termino = atividade["termino"]
        else:
            print(
                "  Descartada: começa em", atividade["inicio"],
                "antes do término da última selecionada:", ultimo_termino
            )


def executar_teste(titulo, quantidade_blocos, mostrar_passos):
    atividades = gerar_atividades(quantidade_blocos)
    repeticoes = 10
    tempo_total_termino = 0
    tempo_total_inicio = 0

    print("\n" + titulo)
    print("Quantidade de atividades:", len(atividades))
    print("Quantidade de blocos:", quantidade_blocos)
    print("Entrada embaralhada com semente 42.")
    print("Repetições de cada estratégia:", repeticoes)

    # Os algoritmos são chamados com a mesma lista, que eles não modificam.
    for repeticao in range(repeticoes):
        inicio_medicao = time.perf_counter()
        selecionadas_termino = selecionar_por_termino(atividades)
        fim_medicao = time.perf_counter()
        tempo_execucao = fim_medicao - inicio_medicao
        tempo_total_termino = tempo_total_termino + tempo_execucao

        inicio_medicao = time.perf_counter()
        selecionadas_inicio = selecionar_por_inicio(atividades)
        fim_medicao = time.perf_counter()
        tempo_execucao = fim_medicao - inicio_medicao
        tempo_total_inicio = tempo_total_inicio + tempo_execucao

    tempo_medio_termino = tempo_total_termino / repeticoes
    tempo_medio_inicio = tempo_total_inicio / repeticoes

    esperado_termino = quantidade_blocos * 3
    esperado_inicio = quantidade_blocos

    if mostrar_passos:
        print("\nDados de entrada:")
        mostrar_atividades(atividades)

        print("\nDecisões: termina primeiro")
        ordenadas = sorted(atividades, key=obter_termino)
        mostrar_decisoes(ordenadas, selecionadas_termino)
        print("\nSolução: termina primeiro")
        mostrar_atividades(selecionadas_termino)

        print("\nDecisões: começa primeiro")
        ordenadas = sorted(atividades, key=obter_inicio)
        mostrar_decisoes(ordenadas, selecionadas_inicio)
        print("\nSolução: começa primeiro")
        mostrar_atividades(selecionadas_inicio)
    else:
        print("\nSolução: termina primeiro seleciona as três curtas de cada bloco.")
        print("Solução: começa primeiro seleciona a longa de cada bloco.")

    print("\nResultado: termina primeiro")
    print("Selecionadas:", len(selecionadas_termino))
    print("Descartadas:", len(atividades) - len(selecionadas_termino))
    print("Quantidade esperada:", esperado_termino)
    print("Tempo médio em milissegundos:", round(tempo_medio_termino * 1000, 6))

    print("\nResultado: começa primeiro")
    print("Selecionadas:", len(selecionadas_inicio))
    print("Descartadas:", len(atividades) - len(selecionadas_inicio))
    print("Quantidade esperada:", esperado_inicio)
    print("Tempo médio em milissegundos:", round(tempo_medio_inicio * 1000, 6))

    if len(selecionadas_termino) != esperado_termino:
        raise AssertionError("A quantidade selecionada por término difere da esperada.")
    if len(selecionadas_inicio) != esperado_inicio:
        raise AssertionError("A quantidade selecionada por início difere da esperada.")

    print("\nAs quantidades obtidas correspondem às esperadas.")


def main():
    print("TESTES DO PROBLEMA DA SELEÇÃO DE ATIVIDADES")
    print("Cada bloco ocupa 10 unidades de tempo e contém 4 atividades.")
    print("Os blocos não se sobrepõem. Dentro deles, a longa conflita com as três curtas.")

    executar_teste("TESTE 1 - PEQUENO", 1, True)
    executar_teste("TESTE 2 - MÉDIO", 250, False)
    executar_teste("TESTE 3 - GRANDE", 25000, False)


if __name__ == "__main__":
    main()
