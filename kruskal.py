def kruskal(vertices, aristas):
    grupo = {vertice: vertice for vertice in vertices}
    arbol = []
    peso_total = 0

    # Revisamos las aristas de menor a mayor peso.
    for origen, destino, peso in sorted(aristas, key=lambda arista: arista[2]):
        grupo_origen = grupo[origen]
        grupo_destino = grupo[destino]

        # Si ya estan conectados, agregar la arista formaria un ciclo.
        if grupo_origen == grupo_destino:
            continue

        arbol.append((origen, destino, peso))
        peso_total += peso

        # Unimos los dos grupos.
        for vertice in grupo:
            if grupo[vertice] == grupo_destino:
                grupo[vertice] = grupo_origen

        if len(arbol) == len(grupo) - 1:
            break

    return arbol, peso_total


if __name__ == "__main__":
    vertices = ["A", "B", "C", "D"]
    aristas = [
        ("A", "B", 1),
        ("A", "C", 4),
        ("B", "C", 2),
        ("B", "D", 5),
        ("C", "D", 3),
    ]

    arbol, peso_total = kruskal(vertices, aristas)
    print("Aristas seleccionadas:", arbol)
    print("Peso total:", peso_total)
