#include <cstdio>
#include <climits>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct edge{ int nxt, inv, cost, cap; };

int V;
vector<edge> con[2010];
int pv[2010], pe[2010];

int dist[2010]; bool inq[2010];
queue<int> q;

void addEdge(int x, int y, int cap, int cost){
  edge ex = {y, (int)con[y].size(), cost, cap};
  edge ey = {x, (int)con[x].size(), -cost, 0};
  con[x].push_back(ex); con[y].push_back(ey);
}

bool spfa(int S, int E){
  for(int i = 0; i < V; i++) dist[i] = INT_MAX;

  q.push(S); inq[S] = true; dist[S] = 0;

  while(!q.empty()){
    int now = q.front(); q.pop(); inq[now] = false;

    int i = 0;
    for(edge& e : con[now]){
      int nxt = e.nxt;

      if(e.cap > 0 && dist[nxt] > dist[now] + e.cost){
        dist[nxt] = dist[now] + e.cost;
        pv[nxt] = now; pe[nxt] = i;
        if(!inq[nxt]){ q.push(nxt); inq[nxt] = true; }
      }

      i++;
    }
  }

  return dist[E] != INT_MAX;
}

int P[1010], B[1010];

int main(){
  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    int N, C, M; scanf("%d%d%d", &N, &C, &M);
    for(int i = 1; i <= M; i++) scanf("%d%d", &P[i], &B[i]);

    V = M + 2; for(int i = 0; i < V; i++) con[i].clear();

    int AC = 0, BC = 0;

    for(int i = 1; i <= M; i++){
      if(B[i] == 1){ AC++; addEdge(0, i, 1, 0); }
      else{ BC++; addEdge(i, V - 1, 1, 0); }
    }

    for(int i = 1; i <= M; i++){
      if(B[i] != 1) continue;
      for(int j = 1; j <= M; j++){
        if(B[j] != 2) continue;

        if(P[i] != P[j]) addEdge(i, j, 1, 0);
        else if(P[i] == P[j] && P[i] != 1) addEdge(i, j, 1, 1);
      }
    }

    int S = 0, E = V - 1;
    int flow = 0, cost = 0;

    while(spfa(S, E)){
      int f = INT_MAX;
      for(int x = E; x != S; x = pv[x]){
        f = min(f, con[pv[x]][pe[x]].cap);
      }

      for(int x = E; x != S; x = pv[x]){
        edge &e = con[pv[x]][pe[x]];
        e.cap -= f; con[x][e.inv].cap += f;
        cost += e.cost * f;
      }

      flow += f;
    }

    printf("Case #%d: %d %d\n", tt, AC + BC - flow, cost);
  }
  return 0;
}
