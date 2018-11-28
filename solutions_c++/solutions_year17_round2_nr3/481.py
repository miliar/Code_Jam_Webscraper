#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

#include <functional>
#include <cassert>

typedef long long ll;
using namespace std;

#define debug(x) cerr << #x << " = " << x << endl;


#define mod 1000000007 //1e9+7(prime number)
#define INF 1000000000 //1e9
#define LLINF 2000000000000000000LL //2e18
#define SIZE 110

/* Dijkstra O(NlogM)*/

struct Dijkstra{
  
  typedef double Type;
  
  int V;
  vector<vector<pair<int,Type> > > G;
  vector<int> cost;
  
  Dijkstra(int n):
    V(n),G(n,vector<pair<int,Type> >()){}
  
  void add_edge(int u, int v, Type c){
    G[u].push_back({v,c});
  }
  
  Type solve(int s, int g = -1){
    cost.assign(V,-1);
    priority_queue<pair<Type,int> > pq;
    Type max_cost = 0;
    
    pq.push({0,s});
    
    while(pq.size()){
      Type now_cost = pq.top().first;
      int now = pq.top().second;
      pq.pop();
      
      if(cost[now] >= 0) continue;
      
      cost[now] = -now_cost;
      max_cost = max(max_cost, -now_cost);
      
      if(now == g) return -now_cost;
      
      for(int i=0;i<(int)G[now].size();i++){
        pq.push({now_cost-G[now][i].second, G[now][i].first});
      }
    }
    
    return max_cost;
  }
  
};

void solve(){
  int n,q;
  int e[SIZE],s[SIZE];
  int d;
  vector<pair<int,ll> > way[SIZE];
  ll dist[SIZE][SIZE];

  scanf("%d%d",&n,&q);

  for(int i=0;i<n;i++){
    scanf("%d%d",e+i,s+i);
  }
  
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      scanf("%d",&d);
      if(d > 0){
        dist[i][j] = d;
      }else{
        dist[i][j] = LLINF;
      }
    }
  }

  for(int k=0;k<n;k++){
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
        dist[i][j] = min(dist[i][k]+dist[k][j], dist[i][j]);
      }
    }
  }

  Dijkstra dijk(n);
  
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      if(dist[i][j] <= e[i]){
        dijk.add_edge(i,j,(double)dist[i][j]/s[i]);
      }
    }
  }

  for(int i=0;i<q;i++){
    int a,b;
    scanf("%d%d",&a,&b);
    a--; b--;

    printf("%.7lf%c",dijk.solve(a,b)," \n"[i==q-1]);
  }
  
}

int main(){
  int T;

  scanf("%d",&T);

  for(int i=1;i<=T;i++){

    printf("Case #%d: ",i);

    solve();
  }
  
  return 0;
}
