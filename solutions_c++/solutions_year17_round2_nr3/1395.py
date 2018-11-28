#include<iostream>
#include<vector>
#include<queue>
#include <stdlib.h>
using namespace std;
long long route[101][101];
struct cav{
  long long dist, speed;
};
struct sol{
  int u;
  long double tim;
  long long dist;
  long long speed;
  bool *cava;
};
struct compara{
  bool operator()(sol a, sol b){
    return a.tim>b.tim;
  }
};
cav cavalli[101];
long double trova(int a, int b, int N){
  bool vis[N];
  for(int i=0;i<N;i++)
    vis[i]=0;
  priority_queue<sol, vector<sol>, compara> q;
  bool *pt=new bool[N];
  for(int i=0;i<N;i++)
    pt[i]=false;
  pt[a]=true;
  sol t={a, 0, cavalli[a].dist, cavalli[a].speed, pt};
  q.push(t);
  while(!q.empty()){
    int u=q.top().u;
    long double tim=q.top().tim;
    long long dist=q.top().dist;
    long long speed=q.top().speed;
    bool *po = q.top().cava;
    //cout<<u<<" "<<tim<<endl;
    q.pop();
    if(u==b)
      return tim;

    for(int i=0;i<N;i++){
      if(i!=u && route[u][i]!=-1){
        if(route[u][i]<=dist){
          sol t={i, tim+(long double)route[u][i]/speed, dist-route[u][i], speed, po};
          q.push(t);
        }
        if(route[u][i]<=cavalli[u].dist){
          if(po[u]==0){
            bool *po2=new bool[N];
            for(int j=0;j<N;j++)
              po2[j]=po[j];
            po2[u]=1;
            sol t={i, tim+(long double)route[u][i]/cavalli[u].speed, cavalli[u].dist-route[u][i], cavalli[u].speed, po2};
            q.push(t);
          }
        }
      }

    }
  }
  return -1;
}
int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    int N, Q;
    cin>>N>>Q;
    for(int i=0;i<N;i++){
      cin>>cavalli[i].dist>>cavalli[i].speed;
    }
    for(int i=0;i<N;i++){
      for(int j=0;j<N;j++)
        cin>>route[i][j];
    }
    int a, b;
    cout<<"Case #"<<t<<":";
    for(int i=0;i<Q;i++){
      cin>>a>>b;
      printf(" %Lf", trova(a-1, b-1, N));
    }
    cout<<endl;
  }
}
