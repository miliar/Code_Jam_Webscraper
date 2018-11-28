#include <bits/stdc++.h>
using namespace std;

const int INF = 100000000;

vector<int> edge[15], cap[15], rev[15];

bool vis[15];
int dfs(int u, int f) {
  if (u == 13) return f;
  vis[u] = true;
  
  for (int i=0; i<edge[u].size(); i++) {
    int v = edge[u][i];
    int c = cap[u][i];
    
    if (vis[v]) continue;
    if (c <= 0) continue;
    
    int flow = dfs(v, min(f, c));
    if (flow == 0) continue;
    
    cap[u][i] -= flow;
    cap[v][rev[u][i]] += flow;
    return flow;
  }
  
  return 0;
}

int maxFlow() {
  for (int flow=0;; ) {
    memset(vis, 0, sizeof vis);
    int f = dfs(0, INF);
    if (f == 0) return flow;
    flow += f;
  }
}

void addEdge(int u, int v, int c) {
  edge[u].push_back(v);
  cap[u].push_back(c);
  rev[u].push_back(edge[v].size());
  
  edge[v].push_back(u);
  cap[v].push_back(0);
  rev[v].push_back(edge[u].size() - 1);
}

int cur[6];
vector<int> cycle;
vector<int> e[6];
void euler(int u) {
  while (cur[u] < e[u].size()) 
    euler(e[u][cur[u]++]);
  cycle.push_back(u);
}

int Main() {
  int n;
  scanf("%d", &n);
  
  for (int i=0; i<15; i++) {
    edge[i].clear();
    cap[i].clear();
    rev[i].clear();
  }
  
  for (int i=0; i<6; i++) {
    int tmp;
    scanf("%d", &tmp);
    
    addEdge(0, i+1, tmp);
    addEdge(i+7, 13, tmp);
  }
  
  addEdge(1, 9, INF); addEdge(1, 10, INF); addEdge(1, 11, INF);
  addEdge(2, 11, INF);
  addEdge(3, 7, INF); addEdge(3, 11, INF); addEdge(3, 12, INF);
  addEdge(4, 7, INF);
  addEdge(5, 7, INF); addEdge(5, 8, INF); addEdge(5, 9, INF);
  addEdge(6, 9, INF);
  
  int res = maxFlow();
  if (res < n) return 0 * printf("IMPOSSIBLE\n");
  
  for (int i=0; i<6; i++) e[i].clear();
  for (int i=7; i<=12; i++) {
    for (int j=0; j<edge[i].size(); j++) {
      if (edge[i][j] < 1 || edge[i][j] > 6) continue;
      
      for (int k=0; k<cap[i][j]; k++) e[i-7].push_back(edge[i][j] - 1);
    }
  }
  
  for (int i=0; i<6; i++) {
    cycle.clear();
    for (int j=0; j<6; j++) cur[j] = 0;
    euler(i);
    if (cycle.size() <= n) continue;
    
    reverse(cycle.begin(), cycle.end());
    cycle.pop_back();
    for (int c: cycle) {
      if (c == 0) printf("R");
      if (c == 1) printf("O");
      if (c == 2) printf("Y");
      if (c == 3) printf("G");
      if (c == 4) printf("B");
      if (c == 5) printf("V");
    }
    
    return 0 * printf("\n");
  }
  
  return 0 * printf("IMPOSSIBLE\n");
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc=0; tc<t; ++tc) {
    printf("Case #%d: ", tc+1);
    Main();
  }
  return 0;
}