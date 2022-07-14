''' ввод графа'''
def graph_input(N,M):


    graph = {i: set() for i in range(N)}
    for i in range(M):
        v1, v2 = map(int, input().split()) # v1 - вершина
        graph[v1].add(v2)                   # v2 - соседи
        graph[v2].add(v1)
    return(graph)

N, M = map(int, input().split())
graph = graph_input(N, M)
def search(graph):

    from collections import deque
    distances = [None] * N
    start_vertex = 0
    distances[start_vertex] = 0
    start_vertex = 0
    queue = deque([start_vertex])
    while queue:
        cur_v = queue.popleft()
        for neigh_v in graph[cur_v]:
            if distances[neigh_v] is None:
                distances[neigh_v] = distances[cur_v] + 1
                queue.append(neigh_v)
    return (distances)
print(search(graph))

# 15 16 (количество вершин и ребёр)
# 0 1 (вершина и связанная с ней вершина)
# 0 12
# 0 11
# 0 10
# 2 6
# 1 7
# 3 11
# 4 10
# 5 8
# 5 13
# 6 10
# 7 13
# 8 12
# 9 11
# 11 12
# 11 14

