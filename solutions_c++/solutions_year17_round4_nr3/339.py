#include <bits/stdc++.h>

#define x first
#define y second

using namespace std;

typedef long long LL;

struct Edge {
  int from, to, cap, flow, index;
  Edge(int from, int to, int cap, int flow, int index) :
    from(from), to(to), cap(cap), flow(flow), index(index) {}
};

struct PushRelabel {
  int N;
  vector<vector<Edge> > G;
  vector<LL> excess;
  vector<int> dist, active, count;
  queue<int> Q;

  PushRelabel(int N) : N(N), G(N), excess(N), dist(N), active(N), count(2*N) {}

  void AddEdge(int from, int to, int cap) {
    // cerr << "E: " << from << ' ' << to << ' ' << cap << endl;
    G[from].push_back(Edge(from, to, cap, 0, G[to].size()));
    if (from == to) G[from].back().index++;
    G[to].push_back(Edge(to, from, 0, 0, G[from].size() - 1));
  }

  void Enqueue(int v) {
    if (!active[v] && excess[v] > 0) { active[v] = true; Q.push(v); }
  }

  void Push(Edge &e) {
    int amt = int(min(excess[e.from], LL(e.cap - e.flow)));
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

  LL GetMaxFlow(int s, int t) {
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

    LL totflow = 0;
    for (int i = 0; i < G[s].size(); i++) totflow += G[s][i].flow;
    return totflow;
  }
};


struct Solve {
  int R, C;
  vector<string> grid;
  PushRelabel G;
  map <pair <int, int>, int> ef;
  int total_empty, total_beams;
  vector <pair <int, int>> beams;
  vector <bool> least_one;

  Solve(int R, int C): R(R), C(C), grid(R), total_empty(0), total_beams(0), G(1) {}

  void initialize() {
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        if (is_beam({i, j})) {
          beams.push_back({i, j});
          total_beams++;
        } else if (is_empty({ i, j })) {
          ef[{i, j}] = total_empty;
          total_empty++;
        }
      }
    }
  }

  pair<int, int> newdir(pair<int, int> dir, pair<int, int> pos) {
    assert (is_mirror(pos));
    if (grid[pos.x][pos.y] == '/') {
      return { -dir.y, -dir.x };
    } else {
      return { dir.y, dir.x };
    }
  }

  void make_edge(pair<int, int> pos, int b, pair<int, int> dir) {
    least_one[ef[pos]] = true;
    if (dir.x == 0) {
      // -
      G.AddEdge(total_beams + 2 * b + 1, 3 * total_beams + ef[pos] + 1, 1);
    } else {
      // |
      G.AddEdge(total_beams + 2 * b + 2, 3 * total_beams + ef[pos] + 1, 1);
    }
  }

  bool is_mirror(pair <int, int> pos) {
    return grid[pos.x][pos.y] == '/' || grid[pos.x][pos.y] == '\\';
  }

  bool is_wall(pair <int, int> pos) {
    return grid[pos.x][pos.y] == '#';
  }

  bool is_empty(pair <int, int> pos) {
    return grid[pos.x][pos.y] == '.';
  }

  bool is_beam(pair <int, int> pos) {
    return grid[pos.x][pos.y] == '-' || grid[pos.x][pos.y] == '|';
  }

  bool is_outside(pair <int, int> pos) {
    return !(0 <= pos.x && pos.x < R && 0 <= pos.y && pos.y < C);
  }

  bool possible(int index, pair <int, int> dir) {
    auto pos = beams[index];
    while (true) {
      pos.x += dir.x;
      pos.y += dir.y;

      if (is_outside(pos) || is_wall(pos))
        return true;

      if (is_mirror(pos))
        dir = newdir(dir, pos);

      if (is_empty(pos))
        make_edge(pos, index, dir);

      if (is_beam(pos))
        return false;
    }
  }

  bool solve() {
    G = PushRelabel(3 * total_beams + total_empty + 2);
    least_one = vector<bool>(total_empty, false);
    vector <bool> h(total_beams), v(total_beams);
    vector <int> z;
    for (int i = 0; i < beams.size(); i++) {
      G.AddEdge(0, i + 1, total_empty);
      h[i] = possible(i, {0, -1}) && possible(i, {0, 1});
      v[i] = possible(i, {-1, 0}) && possible(i, {1, 0});
      // cerr << "B " << beams[i].x << ' ' << beams[i].y << ' ' << h << ' ' << v << endl;
      if (!h[i] && !v[i]) {
        return false;
      }
      if (!v[i]) {
        G.AddEdge(i + 1, total_beams + 2 * i + 1, total_empty);
        grid[beams[i].x][beams[i].y] = '-';
      }
      if (!h[i]) {
        G.AddEdge(i + 1, total_beams + 2 * i + 2, total_empty);
        grid[beams[i].x][beams[i].y] = '|';
      }
      if (v[i] && h[i]) {
        z.push_back(i);
      }
    }
    bool flag = false;
    for (int i = 0; i < total_empty; i++) {
      if (least_one[i]) flag = true;
      G.AddEdge(3 * total_beams + i + 1, 3 * total_beams + total_empty + 1, 1);
    }

    if(!flag) return false;

    for (int att = 0; att < 2000; att++) {
      auto H = G;
      for (int i: z) {
        int k = rand() % 1;
        G.AddEdge(i + 1, total_beams + 2 * i + 1 + k, total_empty);
        grid[beams[i].x][beams[i].y] = k == 0 ? '-' : '|';
      }
      LL flow = G.GetMaxFlow(0, 3 * total_beams + total_empty + 1);
      if (flow == total_empty)
        return true;
    }
    // cerr << "F: " << flow << endl;

    return false;
  }
};

int main() {
  ios::sync_with_stdio(false);
  srand(time(NULL));

  int t;
  cin >> t;

  for (int cs = 0; cs < t; cs++) {
    int R, C;
    cin >> R >> C;

    Solve S(R, C);

    for (string& row: S.grid) {
      cin >> row;
    }

    S.initialize();
    // cerr << S.total_empty << ' ' << S.total_beams << endl;

    bool possible = S.solve();
    cerr << cs + 1 << endl;
    cout << "Case #" << cs + 1 << ": " << (possible ? "POSSIBLE" : "IMPOSSIBLE") << endl;

    if (possible) {
      for (string& row: S.grid) {
        cout << row << endl;
      }
    }
  }

  return 0;
}
