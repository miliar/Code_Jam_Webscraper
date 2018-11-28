#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;
typedef unsigned long long ull;

int N, C, M;
vector<int> P, B;

#define MAX_V 5005
int V;
vector<int> G[MAX_V];
int match[MAX_V];
bool used[MAX_V];

void init_graph(){
  for(int i=0; i<MAX_V; i++){
    G[i].clear();
    match[i] = -1;
    used[i] = false;
  }
}
void add_edge(int u, int v){
  G[u].push_back(v);
  G[v].push_back(u);
}
bool dfs(int v){
  used[v] = true;
  for(int i=0; i<G[v].size(); i++){
    int u = G[v][i], w = match[u];
    if(w<0||!used[w]&&dfs(w)){
      match[v] = u;
      match[u] = v;
      return true;
    }
  }
  return false;
}
int bipartite_matching(){
  int res = 0;
  rep(i,MAX_V) match[i] = -1;
  for(int v=0; v<V; v++){
    if(match[v] < 0){
      rep(i,MAX_V) used[i] = false;
      if(dfs(v)){
        res++;
      }
    }
  }
  return res;
}


void solve(){
  vector<int> x, y;
  rep(i,P.size()){
    if(B[i]==1) x.push_back(P[i]);
    if(B[i]==2) y.push_back(P[i]);
  }
  sort(ALLOF(x));
  sort(ALLOF(y));

  init_graph();
  V = x.size() + y.size();
  rep(i,x.size()){
    rep(j,y.size()){
      if(x[i]!=y[j]) add_edge(i,x.size()+j);
    }
  }
  int ret = bipartite_matching();
  vector<int> xx, yy;
  rep(i,x.size()){
    if(match[i] == -1) xx.push_back(x[i]);
  }
  rep(i,y.size()){
    if(match[i+x.size()] == -1) yy.push_back(y[i]);
  }

  int promo = 0;
  int mn = min(xx.size(), yy.size());
  if(mn > 0){
    if(xx[0] == 1) ret += xx.size() + yy.size();
    else {
      promo = mn;
      ret += mn + (xx.size()-mn) + (yy.size()-mn);
    }
  }else{
    ret += xx.size() + yy.size();
  }
  cout << ret << " " << promo << endl;
}

int main(){
  int T;
  cin >> T;

  rep(t,T){
    cin >> N >> C >> M;
    P.clear();
    B.clear();
    rep(i,M){
      int p, b;
      cin >> p >> b;
      P.push_back(p);
      B.push_back(b);
    }
    
    cout << "Case #" << t+1 << ": ";
    solve();
  }
  
  return 0;
}



//ios::sync_with_stdio(false);
