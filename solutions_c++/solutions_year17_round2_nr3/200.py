#include <bits/stdc++.h>
using namespace std;

const long long INF = 1000000000000000LL;

int n;
int e[102], s[102];
int d[102][102];

long long dmin[102][102];

struct State {
  double t; int u;
  State(double _t, int _u, int _from): t(_t), u(_u) {}
  
  bool operator < (const State &other) const {
    return t > other.t;
  }
};

bool vis[102];

int solve() {
  int st, en; 
  scanf("%d %d", &st, &en);
  --st, --en;
  
  priority_queue<State> pq;
  pq.push(State(0, st, st));
  for (int i=0; i<n; i++) vis[i] = 0;
  
  while (pq.size()) {
    int u = pq.top().u;
    double t = pq.top().t;
    pq.pop();
    
    if (u == en) return 0 * printf(" %.12lf", t);
    
    if (vis[u]) continue;
    vis[u] = 1;
    
    for (int i=0; i<n; i++) {
      if (dmin[u][i] > e[u]) continue;
      if (vis[i]) continue;
      
      pq.push(State(t + (double) dmin[u][i] / s[u], i, u));
    }
  }
  
  return 0;
}

int Main() {
  int q;
  scanf("%d %d", &n, &q);
  for (int i=0; i<n; i++) scanf("%d %d", e + i, s + i);
  for (int i=0; i<n; i++) 
    for (int j=0; j<n; j++) 
      scanf("%d", &d[i][j]);
      
  for (int i=0; i<n; i++) for (int j=0; j<n; j++) dmin[i][j] = INF;
  for (int i=0; i<n; i++) dmin[i][i] = 0;
  for (int i=0; i<n; i++) for (int j=0; j<n; j++) {
    if (d[i][j] == -1) continue;
    dmin[i][j] = min(dmin[i][j], (long long) d[i][j]);
  }
  
  for (int k=0; k<n; k++)
    for (int i=0; i<n; i++)
      for (int j=0; j<n; j++)
        dmin[i][j] = min(dmin[i][j], dmin[i][k] + dmin[k][j]);
        
  while (q--) solve();
  printf("\n");
  return 0;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc=0; tc<t; ++tc){ 
    printf("Case #%d:", tc+1);
    Main();
  }
  return 0;
}