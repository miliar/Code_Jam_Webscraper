#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MAXN = 110;
const int MAXQ = 110;
const double INF = 1e16;

int n, q;
ll e[MAXN], s[MAXN];
ll dist[MAXN][MAXN];
double tim[MAXN][MAXN];

void compute_time(int v) {
  bool visited[MAXN];
  ll remain[MAXN];
  for (int i = 0; i < n; i++) {
    remain[i] = e[v] + 1;
    visited[i] = false;
  }
  remain[v] = e[v];
  visited[v] = false;
  bool done = false;
  while (!done) {
    int u = -1;
    for (int i = 0; i < n; i++) {
      if (!visited[i] && remain[i] != (e[v] + 1) && (u == -1 || remain[i] > remain[u])) u = i;
    }
    if (u == -1) {
      done = true;
      continue;
    }
    visited[u] = true;
    for (int i = 0; i < n; i++) {
      if (!visited[i] && dist[u][i] != -1 && remain[u] >= dist[u][i] && (remain[i] == (e[v] + 1) || remain[u] - dist[u][i] > remain[i])) {
        remain[i] = remain[u] - dist[u][i];
      }
    }
  }
  for (int i = 0; i < n; i++) {
    tim[v][i] = remain[i] != (e[v] + 1)? (double)(e[v] - remain[i]) / s[v]: INF;
  }
}

void floyd_warshall() {
  for (int k = 0; k < n; k++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (tim[i][j] > tim[i][k] + tim[k][j]) {
          tim[i][j] = tim[i][k] + tim[k][j];
        }
      }
    }
  }
}

int main(void) {
  if (fopen("probCsmall.in", "r")) {
    freopen("probCsmall.in", "r", stdin);
    freopen("probCsmall.out", "w", stdout);
  }
  if (fopen("probClarge.in", "r")) {
    freopen("probClarge.in", "r", stdin);
    freopen("probClarge.out", "w", stdout);
  }
  int t;
  cin >> t;
  for (int ii = 1; ii <= t; ii++) {
    cin >> n >> q;
    for (int i = 0; i < n; i++) cin >> e[i] >> s[i];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        cin >> dist[i][j];
      }
    }
    for (int i = 0; i < n; i++) {
      compute_time(i);
    }
    floyd_warshall();
    vector<double> ans;
    for (int i = 0; i < q; i++) {
      int u, v;
      cin >> u >> v;
      u--; v--;
      ans.push_back(tim[u][v]);
    }
    printf("Case #%d: ", ii);
    for (int i = 0; i < q; i++) {
      printf("%.9f%c", ans[i], " \n"[i == q - 1]);
    }
  }
  return 0;
}
