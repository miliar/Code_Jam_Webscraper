#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <iomanip>
#include <functional>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;


typedef long long lint, ll;
typedef long double ldouble, ld;

#ifdef LOCAL
	#define dbg(expr) cerr << "[" << __LINE__ << "] " << #expr << " = " << (expr) << '\n';
#else
	#define dbg(expr) (void) 0;
#endif


const double inf = 1e18 + 7;

struct Horse {
    lint max_dist, speed;

    Horse() {}

    Horse(lint max_dist, lint speed): max_dist(max_dist), speed(speed) {}

    friend istream & operator >>(istream & input, Horse & value) {
        input >> value.max_dist >> value.speed;
        return input;
    }
};

struct Node {
    int lvl, number;

    Node() {}

    Node(int lvl, int number): lvl(lvl), number(number) {}

    bool operator <(const Node & other) const {
        if (lvl == other.lvl)
            return number < other.number;
        return lvl < other.lvl;
    }
};

vector<lint> get_dists(int start, const vector<vector<lint>> & d) {
    int n = d.size();
    vector<lint> dist(d.size(), inf);
    dist[start] = 0;
    set<pair<lint, int>> q;
    for (int i = 0; i < (int)d.size(); i++)
        q.emplace(inf, i);
    q.erase({inf, start});
    q.emplace(0, start);
    while (!q.empty()) {
        auto cur = q.begin()->second;
        q.erase(q.begin());
        for (int u = 0; u < n; u++) {
            if (d[cur][u] == -1)
                continue;
            if (dist[u] > dist[cur] + d[cur][u]) {
                q.erase({dist[u], u});
                dist[u] = dist[cur] + d[cur][u];
                q.emplace(dist[u], u);
            }
        }
    }
    return dist;
}

template<typename T>
struct Graph {
    map<T, vector<pair<T, double>>> edges;

	Graph() {}

    void add_node(T v) {
        edges[v] = vector<pair<T, double>>();
    }

    void add_edge(T v, T u, double len) {
        edges[v].emplace_back(u, len);
    }

    map<T, double> find_dists(T start) {
        map<T, double> dist;
        for (const auto & e : edges)
            dist[e.first] = inf;
        dist[start] = 0;
        set<pair<double, T>> q;
        for (auto v : dist)
            q.emplace(v.second, v.first);
        while (!q.empty()) {
            auto cur = q.begin()->second;
            q.erase(q.begin());
            for (auto e : edges[cur]) {
                auto u = e.first;
                auto l = e.second;
                if (dist[u] > dist[cur] + l) {
                    q.erase({dist[u], u});
                    dist[u] = dist[cur] + l;
                    q.emplace(dist[u], u);
                }
            }
        }
        return dist;
    }

    int size() const {
        return edges.size();
    }
};

void solve(int test_case) {
    int n, q;
    cin >> n >> q;
    vector<Horse> horse(n);
    for (int i = 0; i < n; i++)
        cin >> horse[i];
    auto g = Graph<Node>();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            g.add_node(Node(i, j));
    }
    vector<vector<lint>> d(n);
    for (int i = 0; i < n; i++) {
        d[i].resize(n);
        for (int j = 0; j < n; j++)
            cin >> d[i][j];
    }
    for (int v = 0; v < n; v++) {
        auto dist = get_dists(v, d);
        for (int u = 0; u < n; u++) {
            if (dist[u] <= horse[v].max_dist)
                g.add_edge(Node(v, v), Node(v, u), (double)dist[u] / horse[v].speed);
        }
        for (int u = 0; u < n; u++)
            g.add_edge(Node(v, u), Node(u, u), 0);
    }
    cout << fixed << setprecision(8);
    cout << "Case #" << test_case + 1 << ": ";
    for (int i = 0; i < q; i++) {
        int v, u;
        cin >> v >> u;
        v--;
        u--;
        auto dist = g.find_dists(Node(v, v));
        double min_value = inf;
        for (int lvl = 0; lvl < n; lvl++)
            min_value = min(min_value, dist[Node(lvl, u)]);
        cout << min_value << ' ';
    }
    cout << endl;
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
        solve(i);
}
