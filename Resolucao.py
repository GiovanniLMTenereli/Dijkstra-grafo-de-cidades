#Feito por Giovanni Lisboa de Miranda Tenereli GRR20230945
import heapq


cidades_grafo = {
    'A': {'B': 4, 'C': 2, 'D': 7},
    'B': {'A': 4, 'C': 1, 'E': 1},
    'C': {'A': 2, 'B': 1, 'D': 3, 'E': 3},
    'D': {'A': 7, 'C': 3, 'E': 2},
    'E': {'B': 1, 'C': 3, 'D': 2}
}

def dijkstra(cidades_grafo, inicio):
    distancias = {cidade: float('inf') for cidade in cidades_grafo}
    distancias[inicio] = 0
    caminho = {cidade: [] for cidade in cidades_grafo}
    caminho[inicio] = [inicio]
    
    fila = [(0, inicio)]
    
    while fila:
        distancia_atual, cidade_atual = heapq.heappop(fila)
        
        if distancia_atual > distancias[cidade_atual]:
            continue
        
        for vizinho, peso in cidades_grafo[cidade_atual].items():
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                caminho[vizinho] = caminho[cidade_atual] + [vizinho]
                heapq.heappush(fila, (nova_distancia, vizinho))
    
    return distancias, caminho

distancias, caminhos = dijkstra(cidades_grafo, 'A')

tempo_A_para_E = distancias['E']
caminho_A_para_E = ' -> '.join(caminhos['E'])

tempo_A_para_D = distancias['D']
caminho_A_para_D = ' -> '.join(caminhos['D'])

print(f"Menor tempo para chegar de A até E: {tempo_A_para_E} horas")
print(f"Caminho de A até E: {caminho_A_para_E}\n")

print(f"Menor tempo para chegar de A até D: {tempo_A_para_D} horas")
print(f"Caminho de A até D: {caminho_A_para_D}\n")
