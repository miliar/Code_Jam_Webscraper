#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <climits>
#include <cmath>

typedef long long LL;
using namespace std;

struct Edge {
    int u, v;
    LL cap, flow;
    Edge () {}
    Edge (int u, int v, LL cap) : u(u), v(v), cap(cap), flow(0) {}
};

struct Dinic {
    int N;
    vector<vector<int> > g;
    vector<Edge> E;
    vector<int> layer, C, path;

    Dinic(int n) : N(n), g(n), E(0), layer(n), C(n), path(0) {}

    void AddEdge(int u, int v, LL c) {
        if (u != v) {
            E.emplace_back(Edge(u, v, c));
            g[u].emplace_back(E.size()-1);
            E.emplace_back(Edge(v, u, 0));
            g[v].emplace_back(E.size()-1);
        }
    }

    LL BFlow(int s, int t) {
        queue<int> q;//BFS to build layered graph
        q.push(s);
        fill(layer.begin(), layer.end(), INT_MAX);
        layer[s] = 0;
        while(q.size()) {
            int u = q.front(); q.pop();
            if (u == t) break;
            for(int k: g[u]) {
                Edge &e = E[k];
                if (e.cap > e.flow && layer[e.v] > layer[u] + 1) {
                    layer[e.v] = layer[u] + 1;
                    q.emplace(e.v);
                }
            }
        }
        if (layer[t] > N) return 0;//t not reachable
        LL flow = 0;//Start searching on the layered graph
        fill(C.begin(), C.end(), 0);
        while(LL f = Search(s,t)) {
            flow += f;
            int u = s;
            for(auto it = path.rbegin(); it != path.rend(); it++) {
                Edge &e = E[g[u][*it]];
                Edge &oe = E[g[u][*it] ^ 1];
                e.flow += f;
                oe.flow -= f;
                u = e.v;
            }
            path.clear();
        }
        return flow;
    }

    LL Search(int s, int t) {
        if (s == t) return INT64_MAX;
        for(int &i = C[s], len = g[s].size(); i < len; i++) {
            Edge &e = E[g[s][i]];
            if ((layer[e.v] == (layer[s] + 1)) && e.cap > e.flow) {
                if (LL f = Search(e.v,t)){
                    LL res = min(f, e.cap - e.flow);
                    path.push_back(i);
                    return res;
                }
            }
        }
        return 0;
    }

    LL MFlow(int s, int t) {
        LL res = 0;
        while(LL flow = BFlow(s, t)) res += flow;
        return res;
    }

};


typedef pair<double, double> PII;

void solve() {
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++) {
        int N, P, R[51], t;
        PII Q[51][51];
        scanf("%d %d", &N, &P);
        for(int j = 0; j < N; j++) {
            scanf("%d", &R[j]);
        }
        for(int j = 0; j < N; j++) {
            for(int k = 0; k < P; k++) {
                scanf("%d", &t);
                double tu = t / (0.9 * R[j]), tl = t / (1.1 * R[j]);
                Q[j][k] = PII(ceil(tl), floor(tu));
                // fprintf(stderr, "%d %d %lf,%lf\n", t, R[j], ceil(tl), floor(tu));
            }
        }
        int s = 0, Z = 50;
        t = 5051;
        Dinic D(5055);
        for(int k = 1; k <= P; k++) {
            D.AddEdge(s, k, 1);
            D.AddEdge(k, s, 1);
        }
        for(int j = 0; j < (N-1); j++) {
            int off = j * Z + 1;
            for(int k = 0; k < P; k++) {
                PII p = Q[j][k];
                for(int l = 0; l < P; l++) {
                    PII p2 = Q[j+1][l];
                    if (p.second >= p2.first && p.first <= p.second && p2.first <= p2.second) {
                        // fprintf(stderr, "%d %d %d %lf %lf\n", j, k, l,p.second, p2.first);
                        D.AddEdge(off+k, off+l+Z, 1);
                        D.AddEdge(off+Z+l, off+k, 1);
                    }
                }
            }
        }
        int off = (N-1) * Z + 1;
        for(int k = 0; k < P; k++) {
            if (Q[N-1][k].first <= Q[N-1][k].second) {
                D.AddEdge(off+k, t, 1);
                D.AddEdge(t, off+k, 1);
            }
        }
        printf("Case #%d: ", i);
        // if (N > 1) {
        cout << D.MFlow(s, t) << endl;
        // } else {
            // int res = 0;
            // for(int k = 0; k < P; k++) {
                // res += Q[0][k].first <= Q[0][k].second;
            // }
            // cout << res << endl;
        // }
    }


}

int main() {
    // std::ios::sync_with_stdio(false);
    freopen("B-large.in", "r", stdin);
    freopen("Bl.out", "w+", stdout);
    solve();
    return 0;
}
