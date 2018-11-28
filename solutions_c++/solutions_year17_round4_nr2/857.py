#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MAX_V 4005
typedef pair<ll,int> P;
ll INF=100000000000LL;

struct edge { ll to,cap,cost,rev; };

int V;
vector<edge> G[MAX_V];
ll h[MAX_V];
ll dist[MAX_V];
int prevv[MAX_V],preve[MAX_V];

void init_edge(){
  for(int i=0;i<V;i++)G[i].clear();
}

void add_edge(int from,int to,int cap,ll cost){
  //  cout<<from<<' '<<to<<' '<<cap<<endl;
  G[from].push_back((edge){to,cap,cost,(int)G[to].size()});
  G[to].push_back((edge){from,0,-cost,(int)G[from].size()-1});
}


ll min_cost_flow(int s,int t,int f){
  ll res = 0;
  fill(h,h+V,0);
  while(f>0){

    priority_queue< P, vector<P>, greater<P> >  que;
    fill( dist, dist+V , INF );
    dist[s]=0;
    que.push(P(0,s));
    while(!que.empty()){
      P p = que.top(); que.pop();
      int v = p.second;
      if(dist[v]<p.first)continue;
      for(int i=0;i<(int)G[v].size();i++){
        edge &e = G[v][i];
        if(e.cap>0&&dist[e.to] > dist[v]+e.cost+h[v]-h[e.to]){
          dist[e.to]=dist[v]+e.cost+h[v]-h[e.to];
          prevv[e.to]=v;
          preve[e.to]=i;
          que.push(P(dist[e.to],e.to));
        }
      }
    }

    if(dist[t]==INF){
      return -1;
    }
    
    for(int v=0;v<V;v++)h[v]+=dist[v];

    int d=f;
    for(int v=t;v!=s;v=prevv[v]){
      d=min(d,(int)G[prevv[v]][preve[v]].cap);
    }
    f-=d;
    res+=(ll)d*h[t];
    for(int v=t;v!=s;v=prevv[v]){
      edge &e = G[prevv[v]][preve[v]];
      e.cap -= d;
      G[v][e.rev].cap += d;
    }
  }
  return res;
}

int N,M,C;
int PX[1000],B[1000];
int si,ti;
map<int,int> mp;

void add_cap(){
  for(int i=0;i<N;i++){
    for(int j=(int)G[C+M+i].size()-1;j>=0;j--){
      edge &e=G[C+M+i][j];
      if(e.to==ti){
        e.cap++;
        break;
      }
    }
  }
}


ll check(int mid){
  
  init_edge();
    
  for(int i=0;i<C;i++){
    add_edge(si,i,mp[i],0);
  }

    
  for(int i=0;i<M;i++){
    add_edge(B[i],C+i,1,0);
    
    add_edge(C+i,C+M+PX[i],1,0);
    for(int j=0;j<PX[i];j++){
      add_edge(C+i,C+M+j,1,1);
    }
  }

  for(int i=0;i<N;i++){
    add_edge(C+M+i,ti, mid ,0);
  }

  return min_cost_flow(si,ti,M);
}

int main(){
  int Tc;
  cin>>Tc;
  for(int tc=1;tc<=Tc;tc++){

    mp.clear();
    
    cin>>N>>C>>M;
    V=N+M+C+2;
    si=V-2;
    ti=V-1;

    int maxm=0;
    for(int i=0;i<M;i++){
      cin>>PX[i]>>B[i];
      PX[i]--;
      B[i]--;

      mp[ B[i] ]++;

      maxm=max(maxm,mp[B[i]]);
    }
    //    cout<<maxm<<endl;

    int key;
    ll ans=0;
    for(int i=maxm;i<=M;i++){
      if(check(i)!=-1){
        key=i;
        break;
      }
    }
    ans=check(key);
    cout<<"Case #"<<tc<<": "<<key<<' '<<ans<<endl;

  }
  return 0;
}

 
