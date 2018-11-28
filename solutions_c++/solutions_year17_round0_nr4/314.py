#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define ALL(a) begin(a), end(a)
#define SZ(a) ((int)(a).size())

#ifdef __DEBUG
#define debug if (true)
#else
#define debug if (false)
#endif

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

// {{{ Bipartite Graph
struct BipartiteGraph {
  int n, m;
  vector<vi> g;
  vi match;

  // [0, n) on the left
  // [n, n + m) on the right
  BipartiteGraph(int n, int m) : n(n), m(m) {
    g.resize(n);
    match.resize(n + m);
  }

  void addEdge(int from, int to) {
    assert(from >= 0 && from < n);
    assert(to >= n && to < n + m);
    g[from].push_back(to);
  }

  int aug(int u, vi &visit) {
    if (visit[u]) {
      return 0;
    }
    visit[u] = 1;
    for (int v : g[u]) {
      if (match[v] == -1 || aug(match[v], visit)) {
        match[u] = v;
        match[v] = u;
        return 1;
      }
    }
    return 0;
  }

  int calcMaximumMatching() {
    fill_n(begin(match), n + m, -1);
    vi visit(n);
    int cnt = 0;
    for (int i = 0; i < n; i++) {
      fill_n(begin(visit), n, 0);
      cnt += aug(i, visit);
    }
    return cnt;
  }
};
// }}}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
  cin >> T;
  while (T--) {
    int n, m;
    cin >> n >> m;
    vi rowOccupied(n);
    vi colOccupied(n);
    vi d1Occupied(2 * n - 1);
    vi d2Occupied(2 * n - 1);
    vector<string> grid(n, string(n, '.'));
    int score = 0;
    for (int i = 0; i < m; i++) {
      char ch;
      int posR, posC;
      cin >> ch >> posR >> posC;
      posR--; posC--;
      grid[posR][posC] = ch;
      if (ch == 'o' || ch == '+') {
        d1Occupied[posR + posC] = 1;
        d2Occupied[posR - posC + n - 1] = 1;
      }
      if (ch == 'o' || ch == 'x') {
        rowOccupied[posR] = 1;
        colOccupied[posC] = 1;
      }
      score += ch == 'o' ? 2 : 1;
    }
    map<pii, char> changes;
    BipartiteGraph bgRowCol(n, n);
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (!rowOccupied[i] && !colOccupied[j]) {
          bgRowCol.addEdge(i, n + j);
        }
      }
    }
    score += bgRowCol.calcMaximumMatching();
    for (int i = 0; i < bgRowCol.n; i++) {
      int row = i;
      int col = bgRowCol.match[i];
      if (col == -1) {
        continue;
      }
      col -= n;
      if (grid[row][col] == '.') {
        grid[row][col] = 'x';
        changes[{row, col}] = 'x';
      } else if (grid[row][col] == '+') {
        grid[row][col] = 'o';
        changes[{row, col}] = 'o';
      } else {
        assert(false);
      }
    }
    BipartiteGraph bgD1D2(2 * n - 1, 2 * n - 1);
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (!d1Occupied[i + j] && !d2Occupied[i - j + n - 1]) {
          bgD1D2.addEdge(i + j, 2 * n - 1 + i - j + n - 1);
        }
      }
    }
    score += bgD1D2.calcMaximumMatching();
    for (int i = 0; i < bgD1D2.n; i++) {
      int d1 = i;
      int d2 = bgD1D2.match[i];
      if (d2 == -1) {
        continue;
      }
      d2 -= 2 * n - 1;
      int row = (d1 + d2 - (n - 1)) / 2;
      int col = (d1 - d2 + (n - 1)) / 2;
      if (grid[row][col] == '.') {
        grid[row][col] = '+';
        changes[{row, col}] = '+';
      } else if (grid[row][col] == 'x') {
        grid[row][col] = 'o';
        changes[{row, col}] = 'o';
      } else {
        assert(false);
      }
    }
    static int caseNo = 1;
    printf("Case #%d: %d %d\n", caseNo++, score, SZ(changes));
    for (auto it : changes) {
      printf("%c %d %d\n", it.se, it.fi.fi + 1, it.fi.se + 1);
    }
    debug {
      for (int i = 0; i < n; i++) {
        puts(grid[i].c_str());
      }
    }
  }
  return 0;
}

