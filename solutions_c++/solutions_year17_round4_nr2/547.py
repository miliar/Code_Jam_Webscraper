#include <stdio.h>
#include <bits/stdtr1c++.h>

#define MAX 10000010
#define clr(ar) memset(ar, 0, sizeof(ar))
#define read() freopen("lol.txt", "r", stdin)
#define write() freopen("out.txt", "w", stdout)
#define dbg(x) cout << #x << " = " << x << endl
#define ran(a, b) ((((rand() << 15) ^ rand()) % ((b) - (a) + 1)) + (a))

using namespace std;

namespace flow{
    const int INF = 1 << 25;

    struct Edge{
        int u, v;
        int cap, flow;

        inline Edge(){}
        inline Edge(int a, int b, int c, int f){
            u = a, v = b, cap = c, flow = f;
        }
    };

    vector <int> adj[MAX];
    vector <struct Edge> E;
    int n, s, t, ptr[MAX], len[MAX], dis[MAX], Q[MAX];

    inline void init(int nodes, int source, int sink){
        clr(len);
        E.clear();
        n = nodes, s = source, t = sink;
        for (int i = 0; i < MAX; i++) adj[i].clear();
    }

    inline void addEdge(int a, int b, int c){
        adj[a].push_back(E.size());
        E.push_back(Edge(a, b, c, 0));
        len[a]++;
        adj[b].push_back(E.size());
        E.push_back(Edge(b, a, 0, 0));
        len[b]++;
    }

    inline bool bfs(){
        int i, j, k, id, f = 0, l = 0;
        memset(dis, -1, sizeof(dis[0]) * n);

        dis[s] = 0, Q[l++] = s;
        while (f < l && dis[t] == -1){
            i = Q[f++];
            for (k = 0; k < len[i]; k++){
                id = adj[i][k];
                if (dis[E[id].v] == -1 && E[id].flow < E[id].cap){
                    Q[l++] = E[id].v;
                    dis[E[id].v] = dis[i] + 1;
                }
            }
        }
        return (dis[t] != -1);
    }

    inline int dfs(int i, int f){
        if (i == t || !f) return f;
        while (ptr[i] < len[i]){
            int id = adj[i][ptr[i]];
            if (dis[E[id].v] == dis[i] + 1){
                int x = dfs(E[id].v, min(f, E[id].cap - E[id].flow));
                if (x){
                    E[id].flow += x, E[id ^ 1].flow -= x;
                    return x;
                }
            }
            ptr[i]++;
        }
        return 0;
    }

    int dinic(){
        int res = 0;

        while (bfs()){
            memset(ptr, 0, n * sizeof(ptr[0]));
            while (int f = dfs(s, INF)) {
                res += f;
            }
        }
        return res;
    }
}

namespace mcmf{
    const int INF = 1 << 25;

    int potential[MAX], dis[MAX], cap[MAX], cost[MAX];
    int n, m, s, t, to[MAX], from[MAX], last[MAX], next[MAX], adj[MAX];

    struct compare{
        inline bool operator()(int a, int b){
            if (dis[a] == dis[b]) return (a < b);
            return (dis[a] < dis[b]);
        }
    };
    set<int, compare> S;

    void init(int nodes, int source, int sink){
        m = 0, n = nodes;
        s = source, t = sink;
        for (int i = 0; i <= n; i++) potential[i] = 0, last[i] = -1;
    }

    void addEdge(int u, int v, int c, int w){
        from[m] = u, adj[m] = v, cap[m] = c, cost[m] = w, next[m] = last[u], last[u] = m++;
        from[m] = v, adj[m] = u, cap[m] = 0, cost[m] = -w, next[m] = last[v], last[v] = m++;
    }

    pair<int, int> solve(){
        int i, j, e, u, v;
        int w, aug = 0, mincost = 0, maxflow = 0;

        while (1){
            S.clear();
            for (i = 0; i < n; i++) dis[i] = INF;

            dis[s] = 0, S.insert(s);
            while (!S.empty()){
                u = *(S.begin());
                if (u == t) break;
                S.erase(S.begin());

                for (e = last[u]; e != -1; e = next[e]){
                    if (cap[e] != 0){
                        v = adj[e];
                        w = dis[u] + potential[u] + cost[e] - potential[v];

                        if (dis[v] > w){
                            S.erase(v);
                            dis[v] = w, to[v] = e;
                            S.insert(v);
                        }
                    }
                }
            }
            if (dis[t] >= (INF >> 1)) break;

            aug = cap[to[t]];
            for (i = t; i != s; i = from[to[i]]) aug = min(aug, cap[to[i]]);
            for (i = t; i != s; i = from[to[i]]){
                cap[to[i]] -= aug;
                cap[to[i] ^ 1] += aug;
                mincost += (cost[to[i]] * aug);
            }
            for (i = 0; i <= n; i++) potential[i] = min(potential[i] + dis[i], INF);
            maxflow += aug;
        }
        return make_pair(mincost, maxflow);
    }
}

int n, c, m, s, t, nodes, lol[MAX], len[MAX], adj[2222][2222];

void build_graph(int days){
    int i, j, k, l, u, v;
    nodes = n + c + 2, s = n + c, t = n + c + 1;

    flow::init(nodes, s, t);
    for (i = 0; i < n; i++) flow::addEdge(s, i, days);
    for (i = 0; i < c; i++) flow::addEdge(i + n, t, min(days, lol[i]));

    for (i = 0; i < n; i++){
        for (j = 0; j < len[i]; j++){
            k = adj[i][j];
            for (l = 0; l <= i; l++) flow::addEdge(l, k + n, 1);
        }
    }
}

void build_graph2(int days){
    int i, j, k, l, u, v;
    nodes = n + c + 2, s = n + c, t = n + c + 1;

    mcmf::init(nodes, s, t);
    for (i = 0; i < n; i++) mcmf::addEdge(s, i, days, 0);
    for (i = 0; i < c; i++) mcmf::addEdge(i + n, t, min(days, lol[i]), 0);

    for (i = 0; i < n; i++){
        for (j = 0; j < len[i]; j++){
            k = adj[i][j];
            mcmf::addEdge(i, k + n, 1, 0);
            for (l = 0; l < i; l++) mcmf::addEdge(l, k + n, 1, 1);
        }
    }
}

int get_mincost(int days){
    build_graph2(days);
    pair <int, int> res = mcmf::solve();
    return res.first;
}

bool check(int days){
    build_graph(days);
    int res = flow::dinic();
    return (res == m);
}

pair<int, int> solve(){
    int low, high, mid, res;

    low = 1, high = m;
    while ((low + 1) < high){
        mid = (low + high) >> 1;
        if (!check(mid)) low = mid;
        else high = mid;
    }

    if (check(low)) return make_pair(low, get_mincost(low));
    return make_pair(high, get_mincost(high));
}

int main(){
    read();
    write();
    unsigned long long h = 0;
    int T = 0, t, i, j, k, x, y, p, b;

    scanf("%d", &t);
    while (t--){
        clr(lol), clr(len);

        scanf("%d %d %d", &n, &c, &m);
        for (i = 0; i < m; i++){
            scanf("%d %d", &p, &b);
            p--, b--;
            lol[b]++, adj[p][len[p]++] = b;
        }
//
//        clr(lol), clr(len);
//        n = 1000, c = 1000, m = 1000;
//        for (i = 0; i < m; i++){
//            p = ran(1, n);
//            b = ran(1, c);
//            p--, b--;
//            lol[b]++, adj[p][len[p]++] = b;
//        }

        pair<int, int> res = solve();
        printf("Case #%d: %d %d\n", ++T, res.first, res.second);
        fprintf(stderr, "Case #%d: %d %d\n", T, res.first, res.second);
        h = h * 666666667 + res.first + 13;
        h *= 10000000007;
        h = h * 666666667 + res.second + 13;
        h *= 10000000007;
    }

    fprintf(stderr, "hash = %llu\n", h);
    return 0;
}
