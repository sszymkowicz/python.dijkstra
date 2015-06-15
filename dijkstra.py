__author__ = 'Slawek'

import networkx as nx
import matplotlib.pyplot as plt

path = []


def dijkstra(graph, start, end, visited=[], distances={}, pre={}) -> list:
    global path
    if start == end:
        path = []
        pred = end
        while pred is not None:
            path.append(pred)
            pred = pre.get(pred, None)
        print("Shortest path: {0}, cost: {1}".format(str(list(reversed(path))), str(distances[end])))

    else:
        if not visited:
            distances[start] = 0

        for n in graph[start]:
            if n not in visited:
                new_dist = distances[start] + graph[start][n]
                if new_dist < distances.get(n, float('inf')):
                    distances[n] = new_dist
                    pre[n] = start

        visited.append(start)
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))
        try:
            x = min(unvisited, key=unvisited.get)
            dijkstra(graph, x, end, visited, distances, pre)
        except ValueError:
            path = []
            pred = end
            while pred is not None:
                path.append(pred)
                pred = pre.get(pred, None)
            print("Shortest path: {0}, cost: {1}".format(str(list(reversed(path))), str(distances[end])))

g = {
    'A': {'C': 1, 'D': 2},
    'B': {'C': 2, 'F': 3},
    'C': {'A': 1, 'B': 2, 'D': 1, 'E': 3},
    'D': {'A': 2, 'C': 1, 'G': 1},
    'E': {'C': 3, 'F': 2},
    'F': {'B': 3, 'E': 2, 'G': 1},
    'G': {'D': 1, 'F': 1}
    }

'''g = {
    1: {3: 1, 4: 2},
    2: {3: 2, 6: 3},
    3: {1: 1, 2: 2, 4: 1, 5: 3},
    4: {1: 2, 3: 1, 7: 1},
    5: {3: 3, 6: 2},
    6: {2: 3, 5: 2, 7: 1},
    7: {4: 1, 6: 1}
    }'''


def main():
    labels = dict()
    for i in g:
        labels[i] = i

    print("*** Shortest path finding ***")
    print("Nodes available in graph: {}".format(labels.keys().__str__()))
    while True:
        try:
            start = str(input(" Start node: ")).upper()
            if start not in labels.keys():
                raise ResourceWarning
        except ValueError:
            print("\t\tError: Input has to be a string!\n")
            continue
        except ResourceWarning:
            print("\t\tWarning: Input node is not available!\n")
            continue
        else:
            break
    while True:
        try:
            end = str(input("   End node: ")).upper()
            if end not in labels.keys():
                raise ResourceWarning
        except ValueError:
            print("\t\tError: Input has to be a string!\n")
            continue
        except ResourceWarning:
            print("\t\tWarning: Input node is not available!\n")
            continue
        else:
            break

    dijkstra(g, start, end)
    G = nx.Graph(g)
    pos = nx.spring_layout(G)

    for n in G.edges_iter():
        G.edge[n[0]][n[1]]['dist'] = str(g[n[0]][n[1]])
        if (n[0] in path) and (n[1] in path):
            G.edge[n[0]][n[1]]['color'] = 'r'
            G.edge[n[0]][n[1]]['width'] = 6
        else:
            G.edge[n[0]][n[1]]['color'] = 'k'
            G.edge[n[0]][n[1]]['width'] = 2
    edge_labels = nx.get_edge_attributes(G, 'dist')

    edges = G.edges()
    colors = [G[u][v]['color'] for u, v in edges]
    widths = [G[u][v]['width'] for u, v in edges]

    nx.draw(G, pos, node_size=1000, edges=edges, edge_color=colors, width=widths)
    nx.draw_networkx_labels(G, pos, labels, font_size=16, font_color='w')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=14)
    plt.show()

if __name__ == '__main__':
    import sys
    sys.exit(main())