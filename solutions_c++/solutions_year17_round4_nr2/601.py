#include<bits/stdc++.h>
using namespace std;
#define int long long
#define MAX_V 2050
vector<int> G[MAX_V];
int match[MAX_V],V;
bool used[MAX_V];
void add_edge(int u,int v){
  G[u].push_back(v);
  G[v].push_back(u);
}
bool dfs(int v){
  used[v]=true;
  for(int i=0;i<(int)G[v].size();i++){
    int u=G[v][i],w=match[u];
    if(w<0||(!used[w]&&dfs(w))){
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

signed main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    cout<<"Case #"<<t<<": ";
    int n,c,m;
    cin>>n>>c>>m;
    int b[m],p[m];
    for(int i=0;i<m;i++) cin>>p[i]>>b[i];
    vector<int> v[c];
    for(int i=0;i<m;i++){
      b[i]--;
      v[b[i]].push_back(p[i]);
    }
    for(int i=0;i<c;i++) sort(v[i].begin(),v[i].end());
    int o[c],x[c];
    memset(o,0,sizeof(o));
    memset(x,0,sizeof(x));
    for(int i=0;i<c;i++)
      for(int j=0;j<(int)v[i].size();j++)
	o[i]+=(v[i][j]==1),x[i]+=(v[i][j]!=1);
    int y=0,z=0;
    for(int i=0;i<c;i++) y=max(y,(int)v[i].size());
    int f=0;
    for(int i=0;i<c;i++) f+=o[i];
    y=max(y,f);
    if(o[0]<x[1]&&o[1]<x[0]){
      int s[c];
      s[0]=x[0]-o[1];
      s[1]=x[1]-o[0];
      int k=max(s[0],s[1]);
      y=max(y,o[0]+o[1]+k);
      for(int i=0;i<MAX_V;i++) G[i].clear();
      V=v[0].size()+v[1].size();
      assert(V==m);
      for(int i=0;i<(int)v[0].size();i++){
	for(int j=0;j<(int)v[1].size();j++){
	  if(v[0][i]==1||v[1][j]==1) continue;
	  if(v[0][i]==v[1][j]) continue;
	  add_edge(i,v[0].size()+j);
	}
      }
      int w=bipartite_matching();
      if(w<min(s[0],s[1])) z=min(s[0],s[1])-w;
    }
    cout<<y<<" "<<z<<endl;
  }
  return 0;
}
