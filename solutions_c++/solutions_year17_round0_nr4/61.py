#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
using namespace std;

#define TRACE(x) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define WATCHR(b, e) TRACE( \
    for (auto it = b; it != e; ++it) \
        { if (it != b) cout << " "; cout << *it; } \
    cout << endl)
#define WATCHC(v) TRACE({cout << #v" = "; WATCHR(v.begin(), v.end());})

using ll = long long;

#define FU(i, a, b) for (auto i = (a); i < (b); ++i)
#define fu(i, b) FU(i, 0, b)
#define FD(i, a, b) for (auto i = (b) - 1; i >= (a); --i)
#define fd(i, b) FD(i, 0, b)
#define all(x) (x).begin(), (x).end()
#define mp make_pair
#define pb emplace_back

struct Edge {
  int from, to, cap, flow, index;
  Edge(int from, int to, int cap, int flow, int index) :
    from(from), to(to), cap(cap), flow(flow), index(index) {}
};

struct PushRelabel {
  int N;
  vector<vector<Edge>> G;
  vector<ll> excess;
  vector<int> dist, active, count;
  queue<int> Q;

  PushRelabel(int N) : N(N), G(N), excess(N), dist(N), active(N), count(2*N) {}

  void AddEdge(int from, int to, int cap) {
    G[from].push_back(Edge(from, to, cap, 0, G[to].size()));
    if (from == to) G[from].back().index++;
    G[to].push_back(Edge(to, from, 0, 0, G[from].size() - 1));
  }

  void Enqueue(int v) {
    if (!active[v] && excess[v] > 0) { active[v] = true; Q.push(v); }
  }

  void Push(Edge &e) {
    int amt = int(min(excess[e.from], ll(e.cap - e.flow)));
    if (dist[e.from] <= dist[e.to] || amt == 0) return;
    e.flow += amt;
    G[e.to][e.index].flow -= amt;
    excess[e.to] += amt;
    excess[e.from] -= amt;
    Enqueue(e.to);
  }

  void Gap(int k) {
    for (int v = 0; v < N; v++) {
      if (dist[v] < k) continue;
      count[dist[v]]--;
      dist[v] = max(dist[v], N+1);
      count[dist[v]]++;
      Enqueue(v);
    }
  }

  void Relabel(int v) {
    count[dist[v]]--;
    dist[v] = 2*N;
    for (int i = 0; i < G[v].size(); i++)
      if (G[v][i].cap - G[v][i].flow > 0)
    dist[v] = min(dist[v], dist[G[v][i].to] + 1);
    count[dist[v]]++;
    Enqueue(v);
  }

  void Discharge(int v) {
    for (int i = 0; excess[v] > 0 && i < G[v].size(); i++) Push(G[v][i]);
    if (excess[v] > 0) {
      if (count[dist[v]] == 1)
    Gap(dist[v]);
      else
    Relabel(v);
    }
  }

  ll GetMaxFlow(int s, int t) {
    count[0] = N-1;
    count[N] = 1;
    dist[s] = N;
    active[s] = active[t] = true;
    for (int i = 0; i < G[s].size(); i++) {
      excess[s] += G[s][i].cap;
      Push(G[s][i]);
    }

    while (!Q.empty()) {
      int v = Q.front();
      Q.pop();
      active[v] = false;
      Discharge(v);
    }

    ll totflow = 0;
    for (int i = 0; i < G[s].size(); i++) totflow += G[s][i].flow;
    return totflow;
  }
};

int main() {
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        ll res = 0;
        int n, m;
        cin >> n >> m;
        vector<vector<char>> grid(n, vector<char>(n, '.'));
        vector<bool> row(n), col(n), left(2*n), right(2*n);
        fu(i, m) {
            char kind;
            int r, c;
            cin >> kind >> r >> c;
            --r, --c;
            grid[r][c] = kind;
            row[r] = row[r] || kind != '+';
            col[c] = col[c] || kind != '+';
            left[r+n-c-1] = left[r+n-c-1] || kind != 'x';
            right[r+c] = right[r+c] || kind != 'x';
            res += kind == 'o' ? 2 : 1;
        }

        PushRelabel vert(2*n + 2);
        int source = 2*n, sink = 2*n + 1;
        fu(i, n) {
            if (!row[i])
                vert.AddEdge(source, i, 1);
            if (!col[i])
                vert.AddEdge(n + i, sink, 1);
        }
        fu(i, n) fu(j, n)
            vert.AddEdge(i, n + j, 1);
        res += vert.GetMaxFlow(source, sink);

        PushRelabel diag(4*n + 2);
        source = 4*n, sink = 4*n + 1;
        fu(i, 2*n - 1) {
            if (!left[i])
                diag.AddEdge(source, i, 1);
            if (!right[i])
                diag.AddEdge(i + 2*n - 1, sink, 1);
        }
        fu(i, 2*n - 1) fu(j, 2*n - 1)
            if (((i % 2) ^ (j % 2) ^ (n % 2)) && abs(n-i-1) + abs(n-j-1) < n)
                diag.AddEdge(i, j + 2*n - 1, 1);
        res += diag.GetMaxFlow(source, sink);

        auto updated = grid;
        fu(i, n)
            for (auto& e : vert.G[i])
                if (e.flow == 1)
                    updated[e.from][e.to-n] = updated[e.from][e.to-n] == '+' ? 'o' : 'x';

        map<pair<int,int>,pair<int,int>> map;
        fu(i, n) fu(j, n)
            map[mp(i+n-j-1, i+j)] = mp(i,j);
        fu(i, 2*n - 1)
            for (auto& e : diag.G[i])
                if (e.flow == 1) {
                    auto p = map[mp(e.from,e.to-2*n+1)];
                    updated[p.first][p.second] = updated[p.first][p.second] == 'x' ? 'o' : '+';
                }

        int count = 0;
        fu(i, n) fu(j, n)
            if (updated[i][j] != grid[i][j])
                ++count;

        cout << "Case #" << t << ": " << res << " " << count << endl;
        fu(i, n) fu(j, n)
            if (updated[i][j] != grid[i][j])
                cout << updated[i][j] << " " << (i+1) << " " << (j+1) << endl;
    }
    return 0;
}
