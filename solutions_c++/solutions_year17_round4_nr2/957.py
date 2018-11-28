#include <bits/stdc++.h>
using namespace std;

int N,M,C;
int P[1111],B[1111];

#define MAX_V 10000
int V;
vector<int> G[MAX_V];
int match[MAX_V];
bool used[MAX_V];


void graph_init(){
  for(int i=0;i<MAX_V;i++)G[i].clear();
}

void add_edge(int u,int v){
  G[u].push_back(v);
  G[v].push_back(u);
}

bool dfs(int v){
  used[v]=true;
  for(int i=0;i<(int)G[v].size();i++){
    int u=G[v][i],w=match[u];
    if( w<0 ||( !used[w] && dfs(w) )){
      match[v]=u;
      match[u]=v;
      return true;
    }
  }
  return false;
}

int bipartite_matching(){
  int res=0;
  memset(match,-1,sizeof(match));
  for(int v=0;v<V;v++){
    if(match[v]<0){
      memset(used,0,sizeof(used));
      if(dfs(v)){
        res++;
      }
    }
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  while (T--) {

    vector<int> V1,V2;
    graph_init();

    cin >> N >> C >> M;
    //cout << N << " "<< C << " " << M << endl;
    V = M;

    for(int i=0;i<M;i++) {
      cin >> P[i] >> B[i];
      if( B[i] == 1 ) V1.emplace_back(P[i]);
      else V2.emplace_back(P[i]);
    }


    int res1=0,res2=0;
    if( C == 2 ) {
      for( int i=0;i<V1.size();i++){
        int v1 = V1[i];
        for(int j=0;j<V2.size();j++){
          int v2 = V2[j];
          if( v1 != v2 ) {
            add_edge(i, j + V1.size());
          }
        }
      }

      int mf = bipartite_matching();

//     cout << "mf: " << mf << endl;

      int x1 = 0, x2 = 0;
      for(int v : V1)
        if( v == 1 ) x1++;
      for(int v : V2)
        if( v == 1 ) x2++;
      x1 -= mf; x2 -= mf;
      if( x1 > 0 && x2 > 0){
        //cout << "1: "  << x1 << " " << x2 << " " << max(V1.size(),V2.size()) << " " <<  min(V1.size(),V2.size()) << " " << endl;
        res1 = mf + x1 + x2;
        res2 = 0;
      } else {
        //cout << "2: "<< max(V1.size(),V2.size()) << " " <<  min(V1.size(),V2.size()) << " " << mf << " "<< endl;
        res1 = max(V1.size(),V2.size());
        res2 = min(V1.size(),V2.size())-mf;
        assert(res2>=0);
      }

    } else
      res1 = res2 = -1;

    static int ttt = 1;
    cout << "Case #" << ttt++ << ": ";
    cout << res1 << " " << res2 << endl;
  }

}