#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
#include <set>

using namespace std;

typedef long long li;
typedef long double ld;

const int N = 310;
const li INF = static_cast<li>(1e18);

int n, q;
li e[N], s[N];
li d[N][N], t[N][N];

ld get_time(int fr, int to) {
  vector<ld> d(n, INF);
  d[fr] = 0;

  set<pair<ld, int>> q;
  q.emplace(d[fr], fr);

  while (!q.empty()) {
    int v = q.begin()->second;
    q.erase(q.begin());

    for (int u = 0; u < n; ++u) {
      ld new_d = d[v] + static_cast<ld>(t[v][u]) / s[v];
      if (t[v][u] <= e[v] && d[u] > new_d) {
        pair<ld, int> cur(d[u], u);
        q.erase(cur);
        cur.first = d[u] = new_d;
        q.insert(cur);
      }
    }
  }

  return d[to];
}

int main() {
  int tests;
  cin >> tests;

  cout.precision(10);
  cout << fixed;

  for (int test = 1; test <= tests; ++test) {
    cout << "Case #" << test << ": ";

    cin >> n >> q;

    for (int i = 0; i < n; ++i) {
      cin >> e[i] >> s[i];
    }

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        cin >> d[i][j];
        t[i][j] = (d[i][j] == -1) ? INF : d[i][j];
        if (i == j)
          t[i][j] = 0;
      }
    }

    for (int x = 0; x < n; ++x) {
      for (int v = 0; v < n; ++v) {
        for (int u = 0; u < n; ++u) {
          t[v][u] = min(t[v][u], t[v][x] + t[x][u]);
        }
      }
    }

    for (int qi = 0; qi < q; ++qi) {
      int v, u;
      cin >> v >> u;
      v--; u--;
      cout << get_time(v, u) << " ";
    }
    cout << endl;
  }
  return 0;
}