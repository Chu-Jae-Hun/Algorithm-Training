def dfs(graph, start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i)
        cnt += 1
print(cnt)