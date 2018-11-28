#include <bits/stdc++.h>

using namespace std;

#define MAX_V 1005
/*
struct edge { int to,cap,rev; };

vector<edge> G[MAX_V];
int level[MAX_V];
int iter[MAX_V];

void add_edge(int from,int to,int cap){
    G[from].push_back((edge){to,cap,G[to].size()});
    G[to].push_back((edge){from,0,G[from].size()-1});
}

void bfs(int s){
    memset(level,-1,sizeof(level));
    queue<int> que;
    level[s] = 0;
    que.push(s);
    while(!que.empty()){
        int v = que.front();que.pop();
        for(int i = 0;i < G[v].size();i++){
            edge &e = G[v][i];
            if(e.cap > 0 && level[e.to] < 0){
                level[e.to] = level[v]+1;
                que.push(e.to);
            }
        }
    }
}

int dfs(int v,int t,int f){
    if(v == t) return f;
    for(int &i = iter[v];i < G[v].size();i++){
        edge &e = G[v][i];
        if(e.cap > 0 && level[v] < level[e.to]){
            int d = dfs(e.to,t,min(f,e.cap));
            if(d > 0){
                e.cap -= d;
                G[e.to][e.rev].cap += d;
                return d;
            }
        }
    }
    return 0;
}

int max_flow(int s,int t){
    int flow = 0;
    while(1){
        bfs(s);
        if(level[t] < 0) return flow;
        memset(iter,0,sizeof(iter));
        int f;
        while((f = dfs(s,t,INT_MAX)) > 0) {
            flow += f;
        }
    }
}
*/

int V;
vector<int> G[MAX_V];
int match[MAX_V];
bool used[MAX_V];

void add_edge(int u,int v){
  G[u].push_back(v);
  G[v].push_back(u);
}

bool dfs(int v){
  used[v] = true;
  for(int i = 0;i < G[v].size();i++){
    int u = G[v][i],w = match[u];
    if(w < 0 || !used[w] && dfs(w)){
      match[v] = u;
      match[u] = v;
      return true;
    }
  }
  return false;
}

int bipartite_matching(){
  int res = 0;
  memset(match,-1,sizeof(match));
  for(int v = 0;v < V;v++){
    if(match[v] < 0){
      memset(used,0,sizeof(used));
      if(dfs(v)){
        res++;
      }
    }
  }
  return res;
}

void solve(int time){
  int n,m,c;
  cin >> n >> c >> m;
  vector<int> p(m),b(m);
  vector<int> ti[1000];
  for(int i = 0;i < m;i++){
    cin >> p[i] >> b[i];
    p[i]--;b[i]--;
    ti[b[i]].push_back(p[i]);
  }
  for(int i = 0;i < MAX_V;i++){
    G[i].clear();
  }
  /*
  int s = m,t = m+1;
  for(int i = 0;i < ti[0].size();i++){
    add_edge(s,i,1);
  }
  for(int i = 0;i < ti[1].size();i++){
    add_edge(ti[0].size()+i,t,1);
  }*/
  V = m;
  for(int i = 0;i < ti[0].size();i++){
    for(int j = 0;j < ti[1].size();j++){
      if(ti[0][i] != ti[1][j]){
        add_edge(i,ti[0].size()+j);
      }
    }
  }
  int a1 = bipartite_matching();
  for(int i = 0;i < ti[0].size();i++){
    for(int j = 0;j < ti[1].size();j++){
      if(ti[0][i] == ti[1][j] && ti[0][i] != 0){
        add_edge(i,ti[0].size()+j);
      }
    }
  }
  int a2 = bipartite_matching();
  int ans1 = m-a2;
  int ans2 = a2-a1;
  cout << "Case #" << time << ": ";
  cout << ans1 << ' ' << ans2 << endl;
}

int main(void){
  int t;
  cin >> t;
  for(int i = 1;i <= t;i++){
    solve(i);
  }
}
