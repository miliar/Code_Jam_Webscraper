#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long ull;

int const INF = 100 + (int) 1e9;
ll const INFL = 100 + (ll) 1e18;
ld const PI = 3.141592653589793238462643L;
int const N = 300300;

namespace mcmf {
    struct edge_t {
        int to, cap, flow, cost;
        
        edge_t() {}
        
        edge_t(int to, int cap, int cost) :
            to(to), cap(cap), flow(0), cost(cost) {}
    };

    vector<edge_t> edges;
    vector<int> g[N];

    void clear_graph(int oldn) {
        edges.clear();
        for (int i = 0; i < oldn; ++i) {
            g[i].clear();
        }
    }

    int add_edge(int v, int to, int cap, int cost) {
        int ret;
        g[v].push_back(ret = edges.size());
        edges.emplace_back(to, cap, cost);
        g[to].push_back(edges.size());
        edges.emplace_back(v, 0, -cost);
        return ret;
    }

    pair<ll, ll> min_cost_flow(int source, int sink, int n, ll need_flow) {
        ll cost = 0;
        ll flow = 0;
        while (flow < need_flow) {
            static int q[N], in_q[N], dist[N], prev[N];
            int tail = 0;
            q[tail++] = source;
            fill(dist, dist + n, INF);
            dist[source] = 0;
            in_q[source] = true;
            for (int head = 0; head != tail;) {
                int v = q[head];
                ++head;
                if (head == N)
                    head = 0;
                in_q[v] = false;
                for (int x : g[v]) {
                    edge_t const& e = edges[x];
                    int to = e.to;
                    if (e.flow < e.cap && dist[to] > dist[v] + e.cost) {
                        dist[to] = dist[v] + e.cost;
                        prev[to] = x;
                        if (!in_q[to]) {
                            q[tail++] = to;
                            if (tail == N)
                                tail = 0;
                            in_q[to] = true;
                        }
                    }
                }
            }
            if (dist[sink] == INF) {
                break;
            }
            ll cur_flow = need_flow - flow;
            for (int v = sink; v != source;) {
                int x = prev[v];
                cur_flow = min<ll>(cur_flow, edges[x].cap - edges[x].flow);
                v = edges[x ^ 1].to;
            }
            flow += cur_flow;
            cost += (ll) cur_flow * dist[sink];
            for (int v = sink; v != source;) {
                int x = prev[v];
                edges[x].flow += cur_flow;
                edges[x ^ 1].flow -= cur_flow;
                v = edges[x ^ 1].to;
            }
        }
        return {cost, flow};
    }

    pair<ll, ll> min_cost_max_flow(int source, int sink, int n) {
        return min_cost_flow(source, sink, n, INFL);
    }
}

int find_cost(vector<vector<int>> const &a, int cnt, int n) {
    int c = a.size();
    int sz = 0;
    int source = sz++;
    int sink = sz++;
    vector<int> man(c);
    for (int &x : man) {
        x = sz++;
    }
    vector<int> pl(n), cpl(n), epl(n);
    for (int i = 0; i < n; ++i) {
        pl[i] = sz++;
        cpl[i] = sz++;
        epl[i] = sz++;
    }
    mcmf::clear_graph(sz);
    for (int i = 0; i < n; ++i) {
        mcmf::add_edge(pl[i], epl[i], INF, 0);
        mcmf::add_edge(pl[i], cpl[i], INF, 1);
        mcmf::add_edge(cpl[i], epl[i], INF, 0);
        mcmf::add_edge(epl[i], sink, cnt, 0);
        if (i > 0) {
            mcmf::add_edge(cpl[i], cpl[i - 1], INF, 0);
        }
    }
    int need_flow = 0;
    for (int i = 0; i < c; ++i) {
        mcmf::add_edge(source, man[i], a[i].size(), 0);
        need_flow += a[i].size();
        for (int x : a[i]) {
            mcmf::add_edge(man[i], pl[x], 1, 0);
        }
    }
    auto res = mcmf::min_cost_max_flow(source, sink, sz);
    if (res.second != need_flow)
        return -1;
    return res.first;
}

string solve() {
    int n, c, m;
    cin >> n >> c >> m;
    vector<vector<int>> a(c);
    for (int i = 0; i < m; ++i) {
        int p, b;
        cin >> p >> b;
        --p, --b;
        a[b].push_back(p);
    }
    int l = 0, r = m + 1;
    for (int i = 0; i < c; ++i) {
        l = max(l, (int)a[i].size() - 1);
    }
    while (r - l > 1) {
        int cnt = (l + r) / 2;
        if (find_cost(a, cnt, n) != -1) {
            r = cnt;
        } else {
            l = cnt;
        }
    }
    int cnt = r;
    int proms = find_cost(a, cnt, n);
    return to_string(cnt) + " " + to_string(proms);
}



int main() {
    
    //freopen("", "r", stdin);
    //freopen("", "w", stdout);
    
    cout.precision(15);
    cout << fixed;
    cerr.precision(6);
    cerr << fixed;
    
    int tcn = 1;
    cin >> tcn;
    for (int tn = 1; tn <= tcn; ++tn) {
        cerr << "test #" << tn << '\n';
        cout << "Case #" << tn << ": " << solve() << '\n';
    }
#ifdef LOCAL
    cerr << "time: " << (ll) clock() * 1000 / CLOCKS_PER_SEC << " ms" << endl;
#endif
}
