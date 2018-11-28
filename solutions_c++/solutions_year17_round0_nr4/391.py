#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

struct Edge {
  int u, v;
  LL cap, flow;
  Edge() {}
  Edge(int u, int v, LL cap): u(u), v(v), cap(cap), flow(0) {}
};

struct Dinic {
  int N;
  vector<Edge> E;
  vector<vector<int>> g;
  vector<int> d, pt;

  Dinic(int N): N(N), E(0), g(N), d(N), pt(N) {}

  void AddEdge(int u, int v, LL cap) {
    if (u != v) {
      E.emplace_back(Edge(u, v, cap));
      g[u].emplace_back(E.size() - 1);
      E.emplace_back(Edge(v, u, 0));
      g[v].emplace_back(E.size() - 1);
    }
  }

  bool BFS(int S, int T) {
    queue<int> q({S});
    fill(d.begin(), d.end(), N + 1);
    d[S] = 0;
    while(!q.empty()) {
      int u = q.front(); q.pop();
      if (u == T) break;
      for (int k: g[u]) {
        Edge &e = E[k];
        if (e.flow < e.cap && d[e.v] > d[e.u] + 1) {
          d[e.v] = d[e.u] + 1;
          q.emplace(e.v);
        }
      }
    }
    return d[T] != N + 1;
  }

  LL DFS(int u, int T, LL flow = -1) {
    if (u == T || flow == 0) return flow;
    for (int &i = pt[u]; i < g[u].size(); ++i) {
      Edge &e = E[g[u][i]];
      Edge &oe = E[g[u][i]^1];
      if (d[e.v] == d[e.u] + 1) {
        LL amt = e.cap - e.flow;
        if (flow != -1 && amt > flow) amt = flow;
        if (LL pushed = DFS(e.v, T, amt)) {
          e.flow += pushed;
          oe.flow -= pushed;
          return pushed;
        }
      }
    }
    return 0;
  }

  LL MaxFlow(int S, int T) {
    LL total = 0;
    while (BFS(S, T)) {
      fill(pt.begin(), pt.end(), 0);
      while (LL flow = DFS(S, T))
        total += flow;
    }
    return total;
  }
};

const int MAXN = 100 + 10;
const int INF = (int)(1e9);

char a[MAXN][MAXN], aa[MAXN][MAXN];
vector<char> b[MAXN][MAXN];
int n, score;

void init() {
    int m;
    cin >> n >> m;
    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= n; ++j) {
            a[i][j] = '.';
            b[i][j].clear();
        }
    score = 0;
    for(int i = 1; i <= m; ++i) {
        char c; int u, v;
        cin >> c >> u >> v;
        a[u][v] = c;
        score += (c == 'o') ? 2 : 1;
    }
}

vector<pair<int, int>> max_matching(int min_L, int max_L, int min_R, int max_R, set<int> &L, set<int> &R, vector<pair<int, int>> &relations) {
    int nl = max_L - min_L + 1, nr = max_R - min_R + 1;
    Dinic dn(nl + nr + 2);
    for(auto p : relations) {
        assert((min_L <= p.first) && (p.first <= max_L));
        assert((min_R <= p.second) && (p.second <= max_R));
        dn.AddEdge(p.first - min_L + 1, p.second - min_R + 1 + nl, 1);
        //cout << "edge " << p.first << " " << p.second << " " << p.first - min_L + 1 << " " << p.second - min_R + 1 + nl << endl;
    }
    for(int i = 1; i <= nl; ++i) dn.AddEdge(0, i, 1 - L.count(min_L + i - 1));
    for(int i = 1; i <= nr; ++i) dn.AddEdge(nl + i, nl + nr + 1, 1 - R.count(min_R + i - 1));

    int mm = dn.MaxFlow(0, nl + nr + 1);

    vector<pair<int, int>> pairs;
    for(auto e : dn.E) {
        if ((min(e.u, e.v) > 0) && (max(e.u, e.v) < nl + nr + 1)) {
            //cout << "la la " << e.u << " " << e.v << " " << e.cap << " " << e.flow << endl;
            //cout << min_L + e.u - 1 << " " << min_R + e.v - nl - 1 << endl;
            if (e.flow > 0) pairs.push_back(make_pair(min_L + e.u - 1, min_R + e.v - nl - 1));
        }
    }
    assert((mm == pairs.size()));
    set<int> check_L, check_R;
    for(auto p : pairs) {
        assert((check_L.count(p.first) == 0));
        assert((check_R.count(p.second) == 0));
        check_L.insert(p.first); check_R.insert(p.second);
    }
    return pairs;
}

void case_plus() {
    vector<pair<int, int>> relations;
    set<int> L, R;
    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= n; ++j)
            if ((a[i][j] == '.') || (a[i][j] == 'x'))
                relations.push_back(make_pair(i + j, i - j));
            else if (a[i][j] == '+') {
                L.insert(i + j); R.insert(i - j);
            }
    vector<pair<int, int>> pairs = max_matching(2, n + n, 1 - n, n - 1, L, R, relations);
    for(auto p : pairs) {
        int i = (p.first + p.second) / 2, j = (p.first - p.second) / 2;
        b[i][j].push_back('+');
        score++;
        //cout << i << " " << j << "+\n";
    }
}

void case_x() {
    vector<pair<int, int>> relations;
    set<int> L, R;
    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= n; ++j)
            if ((a[i][j] == '.') || (a[i][j] == '+'))
                relations.push_back(make_pair(i, j));
            else if (a[i][j] == 'x') {
                L.insert(i); R.insert(j);
            }
    vector<pair<int, int>> pairs = max_matching(1, n, 1, n, L, R, relations);
    for(auto p : pairs) {
        int i = p.first, j = p.second;
        b[i][j].push_back('x');
        score++;
    }
}

void solve() {

    case_plus();
    case_x();

    vector<pair<char, pair<int, int>>> res;
    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= n; ++j) {
            aa[i][j] = (b[i][j].size() == 0) ? '.' : ((b[i][j].size() == 1) ? b[i][j][0] : 'o');
            if (aa[i][j] != '.') {
                char c = (a[i][j] == '.') ? aa[i][j] : 'o';
                res.push_back(make_pair(c, make_pair(i, j)));
            }
        }
    res.clear();
    cout << score << " " << res.size() << endl;
    for(auto x : res) {
        cout << x.first << " " << x.second.first << " " << x.second.second << endl;
    }
}

void run() {
    init();
    solve();
}

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D_old.out", "w", stdout);

    int ntests = 1;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; ++tc) {
        cout << "Case #" << tc << ": ";
        run();
    }
}
