#include <bits/stdc++.h>

using namespace std;
typedef long long int64;
#define DEBUG(x) cerr << #x << " = " << x << endl;
#define REP(x, n) for(__typeof(n) x = 0; x < (n); ++x)
#define FOR(x, b, e) for(__typeof(b) x = (b); x != (e); x += 1 - 2 * ((b) > (e)))
const int64 INF = 100000000000001;
const double EPS = 10e-9;

template<class V, class E> struct Graph {
    struct Edge : E {
        int v;
        Edge(E d, int w): E(d), v(w) { }
    };
    struct Vertex : V, vector<Edge> { };

    vector<Vertex> g;

    Graph(int n) : g(n) { }

    void edgeD(int b, int e, E d = E()) {
        g[b].push_back(Edge(d, e));
    }

    void write() {
        REP(x, g.size())        {
            cout << x << ": ";
            for (auto it : g[x]) cout << it.v << " ";
            cout << "\n";
        }
    }

    void dijkstra(int s) {
        auto djcmp = [](const Vertex* a, const Vertex* b) -> bool {
            return (a->t == b->t) ? a < b : a->t < b->t;
        };
        set<Vertex*, decltype(djcmp)> k(djcmp);
        for (auto& it : g) {
            it.t = INF;
            it.s = -1;
        }
        g[s].t = 0;
        g[s].s = -1;
        k.insert(&g[s]);
        while (!k.empty()) {
            Vertex *y = *(k.begin());
            k.erase(k.begin());
            for (auto it : *y) if (g[it.v].t > y->t + it.l) {
                k.erase(&g[it.v]);
                g[it.v].t = y->t + it.l;
                g[it.v].s = y - &g[0];
                k.insert(&g[it.v]);
            }
        }
    }
};

struct Vs {
    int64 s, t;
};
struct Ve {
    int l;
};

struct Vs_d {
    int s;
    double t;
    int distance, speed;
};
struct Ve_d {
    double l;
};

#ifndef CATCH_TEST
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
    cout << fixed << setprecision(10);

    int t;
    cin >> t;
    REP(o, t) {
        int n, q;
        cin >> n >> q;
        Graph<Vs, Ve> g(n);
        Graph<Vs_d, Ve_d> horse(n);
        REP(x, n) {
            cin >> horse.g[x].distance >> horse.g[x].speed;
        }
        REP(x, n) {
            REP(y, n) {
                int d;
                cin >> d;
                if (d != -1) {
                    g.edgeD(x, y, Ve { d });
                }
            }
        }

        REP(x, n) {
            int distance = horse.g[x].distance;
            int speed = horse.g[x].speed;
            g.dijkstra(x);
            REP(y, n) if(x != y) {
                int64 d = g.g[y].t;
                if (d <= distance) {
                    horse.edgeD(x, y, Ve_d { double(d) / speed });
                }
            }
        }
        
        cout << "Case #" << (o + 1) << ": ";
        REP(x, q) {
            int u, v;
            cin >> u >> v;
            horse.dijkstra(u - 1);
            cout << horse.g[v - 1].t << " ";
        }
        cout << endl;
    }

	return 0;
}
#endif