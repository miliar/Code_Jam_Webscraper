#include <bits/stdc++.h>
using namespace std;

const int MAXN1 = 222;
const int MAXN2 = 222;
const int MAXM = 44444;

// https://sites.google.com/site/indy256/algo_cpp/hopcroft_karp
struct Bipartite {
  int n1, n2, edges, last[MAXN1], prev[MAXM], head[MAXM];
  int matching[MAXN2], dist[MAXN1], Q[MAXN1];
  bool used[MAXN1], vis[MAXN1];
  
  void init(int _n1, int _n2) {
    n1 = _n1;
    n2 = _n2;
    edges = 0;
    fill(last, last + n1, -1);
  }

  void addEdge(int u, int v) {
    head[edges] = v;
    prev[edges] = last[u];
    last[u] = edges++;
  }

  void bfs() {
    fill(dist, dist + n1, -1);
    int sizeQ = 0;
    for (int u = 0; u < n1; ++u) {
      if (!used[u]) {
        Q[sizeQ++] = u;
        dist[u] = 0;
      }
    }
    for (int i = 0; i < sizeQ; i++) {
      int u1 = Q[i];
      for (int e = last[u1]; e >= 0; e = prev[e]) {
        int u2 = matching[head[e]];
        if (u2 >= 0 && dist[u2] < 0) {
          dist[u2] = dist[u1] + 1;
          Q[sizeQ++] = u2;
        }
      }
    }
  }

  bool dfs(int u1) {
    vis[u1] = true;
    for (int e = last[u1]; e >= 0; e = prev[e]) {
      int v = head[e];
      int u2 = matching[v];
      if (u2 < 0 || !vis[u2] && dist[u2] == dist[u1] + 1 && dfs(u2)) {
        matching[v] = u1;
        used[u1] = true;
        return true;
      }
    }
    return false;
  }

  int maxMatching() {
    fill(used, used + n1, false);
    fill(matching, matching + n2, -1);
    for (int res = 0;;) {
      bfs();
      fill(vis, vis + n1, false);
      int f = 0;
      for (int u = 0; u < n1; ++u)
        if (!used[u] && dfs(u))
          ++f;
      if (!f)
        return res;
      res += f;
    }
  }
} A, B;

bool inrange(int x, int n) {
  return x >= 0 && x < n;
}

int Main() {
  int n, m;
  scanf("%d %d", &n, &m);
  
  char c[n][n];
  memset(c, '.', sizeof c);
  
  for (int i=0; i<m; i++) {
    getchar();
    char model = getchar();
    
    int x, y;
    scanf("%d %d", &x, &y);
    c[--x][--y] = model;
  }
  
  A.init(2*n-1, 2*n-1); B.init(n, n);
  
  for (int i=0; i<n; i++) {
    for (int j=0; j<n; j++) {
      bool can = 1;
      for (int k=-n; k<n; k++) {
        if (inrange(i+k, n) && inrange(j+k, n) && (c[i+k][j+k] == 'o' || c[i+k][j+k] == '+')) can = 0;
        if (inrange(i+k, n) && inrange(j-k, n) && (c[i+k][j-k] == 'o' || c[i+k][j-k] == '+')) can = 0;
      }
      
      if (can) A.addEdge(i+j, i-j+n-1);
    }
  }
  
  for (int i=0; i<n; i++) {
    for (int j=0; j<n; j++) {
      bool can = 1;
      for (int k=0; k<n; k++) {
        if (inrange(k, n) && inrange(j, n) && (c[k][j] == 'o' || c[k][j] == 'x')) can = 0;
        if (inrange(i, n) && inrange(k, n) && (c[i][k] == 'o' || c[i][k] == 'x')) can = 0;
      }
      
      if (can) B.addEdge(i, j);
    }
  }
  
  A.maxMatching();
  B.maxMatching();
  
  char d[n][n];
  for (int i=0; i<n; i++) for (int j=0; j<n; j++) d[i][j] = c[i][j];
  
  for (int i=0; i<n; i++) {
    for (int j=0; j<n; j++) {
      bool a = (A.matching[i-j+n-1] == i+j);
      bool b = (B.matching[j] == i);
      
      if (a && b || a && d[i][j] != '.' || b && d[i][j] != '.') d[i][j] = 'o';
      else if (a && d[i][j] == '.') d[i][j] = '+';
      else if (b && d[i][j] == '.') d[i][j] = 'x';
    }
  }
  
  int ans1 = 0, ans2 = 0;
  for (int i=0; i<n; i++) for (int j=0; j<n; j++) {
    if (d[i][j] == '+' || d[i][j] == 'x') ans1 += 1;
    else if (d[i][j] == 'o') ans1 += 2;
    
    if (d[i][j] != c[i][j]) ans2++;
  }
  
  printf("%d %d\n", ans1, ans2);
  for (int i=0; i<n; i++) for (int j=0; j<n; j++) {
    if (c[i][j] != d[i][j]) printf("%c %d %d\n", d[i][j], i+1, j+1);
  }
  
  return 0;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc=0; tc<t; ++tc) {
    printf("Case #%d: ", tc+1);
    Main();
  }
}