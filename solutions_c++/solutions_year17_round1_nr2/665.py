#include <bits/stdc++.h>

typedef long long ll;

using namespace std;


struct edge{
    int to, rev, cap, flow;
};

struct Dinic{

    static const int MAX_NODES = 5001, MAX_FLOW = 1 << 30;

    vector <edge> graph[MAX_NODES];

    int dist[MAX_NODES], ptr[MAX_NODES], s, t, n;

    void addEdge (int a, int b, int cap){
        edge e1 = {b, (int)graph[b].size(), cap, 0};
        edge e2 = {a, (int)graph[a].size(), 0, 0};
        graph[a].push_back (e1);
        graph[b].push_back (e2);
    }

    bool bfs (){
        queue <int> q;
        for (int i = 0; i < n; i++) dist[i] = -1;
        q.push(s);
        dist[s] = 0;
        while (!q.empty()){
            int v = q.front();
            q.pop();
            for (int i = 0; i < graph[v].size(); i++){
                edge e = graph[v][i];
                if (dist[e.to] == -1 && e.flow < e.cap){
                    q.push(e.to);
                    dist[e.to] = dist[v] + 1;
                }
            }
        }
        return dist[t] != -1;
    }

    int dfs (int v, int flow){
        if (!flow) return 0;
        if (v == t) return flow;
        for (; ptr[v] < graph[v].size(); ptr[v]++){
            edge &e = graph[v][ptr[v]];
            if (dist[v] + 1 != dist[e.to]) continue;
            int f = dfs (e.to, min (flow, e.cap - e.flow));
            if (f){
                e.flow += f;
                graph[e.to][e.rev].flow -= f;
                return f;
            }
        }
        return 0;
    }

    int getMaxFlow (int src, int sink, int qtd_nodes){
        s = src, t = sink, n = qtd_nodes;
        int flow = 0;
        while (bfs()){
            for (int i = 0; i < n; i++) ptr[i] = 0;
            while (int f = dfs(s, MAX_FLOW)){
                flow += f;
            }
        }
        return flow;
    }
};

struct node{
    int id;
    set <int> values;
};

bool contain (set<int> &a, set<int> &b){
    for (auto x: a)
        if (b.count(x)) return true;
    return false;
}

int main(){

    int cases;
    scanf ("%d", &cases);

    for (int nth_case = 1; nth_case <= cases; nth_case++){

        int n, p;
        scanf ("%d %d", &n, &p);
        int qtd[n];
        for (int i = 0; i < n; i++) scanf ("%d", qtd + i);

        int id = 0;

        vector <node> nodes[n];

        for (int j = 0; j < p; j++){
            int ingre;
            scanf ("%d", &ingre);

            node no;
            no.id = id++;

            int q = (ingre * 10) / (9 * qtd[0]);

            while (ingre * 10 <= q * qtd[0] * 11){
                if (ingre * 10 >= q * qtd[0] * 9)
                    no.values.insert (q);
                q--;
            }

            nodes[0].push_back(no);
        }

        for (int i = 1; i < n; i++){
            for (int j = 0; j < p; j++){
            int ingre;
            scanf ("%d", &ingre);

            node no;
            no.id = id++;

            int q = (ingre * 10) / (9 * qtd[i]);

            while (ingre * 10 <= q * qtd[i] * 11){
                if (ingre * 10 >= q * qtd[i] * 9)
                    no.values.insert (q);
                q--;
            }

            nodes[i].push_back(no);

            }
        }

        int s = id++;
        int t = id++;

        Dinic d;

        for (int i = 0; i < p; i++){
            if (nodes[0][i].values.size())
                d.addEdge(s, nodes[0][i].id, 1);
        }
        for (int i = 0; i < p; i++)
            d.addEdge(nodes[n-1][i].id, t, 1);

        for (int i = 0; i < n -1; i++){
            for (int j = 0; j < p; j++){
                for (int j2 = 0; j2 < p; j2++){
                    if (contain(nodes[i][j].values, nodes[i+1][j2].values)){
                        d.addEdge(nodes[i][j].id, nodes[i+1][j2].id, 1);
                    }
                }
            }
        }

        printf ("Case #%d: %d", nth_case, d.getMaxFlow(s, t, id));

        printf ("\n");
    }

    return 0;
}
