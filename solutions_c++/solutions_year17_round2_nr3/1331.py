#include <bits/stdc++.h>

using namespace std;
#define lli long long int
#define INF 10000000000000007


int n,q,e[105],u,v;
double s[105];

lli dist[105][105];

double dp[105];

double solve(int u, int v, int p, bool vis[]) {

  if (u == v) {
    return 0.0;
  }

  double ans = 100000000000000.00;
  if (dp[u] == 100000000000000.00) {
    for(int i=1;i<=n;i++){
      if(dist[u][i]!=INF && dist[u][i] <= e[u] && i!=p && !vis[i]) {
        double sol = solve(i,v,u, vis);
        vis[i] = true;
        // printf("%d %d %.6f\n", i,p,sol+((dist[u][i]*1.0)/s[u]));
        ans = min (ans , (sol+((dist[u][i]*1.0)/s[u])));
        vis[i] = false;
        // printf("%.6f\n",ans );
      }
      dp[u] = ans;
    }
  }
  return dp[u];
}

void floydWarshall() {
  for(int k=1;k<=n;k++) {
    for(int i=1;i<=n;i++) {
      for(int j=1;j<=n;j++) {
        dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]);
      }
    }
  }
}


int main() {
  freopen("incs.in","r",stdin);
  freopen("outcs-2.txt","w",stdout);
  int t;cin>>t;
  for(int test=1;test<=t;test++) {
    cout<<"Case #"<<test<<": ";
    cin>>n>>q;
    for(int i=1;i<=n;i++){
      cin>>e[i]>>s[i];
    }

    for(int i=1;i<=n;i++){
      for(int j=1;j<=n;j++){
        cin>>dist[i][j];
        if(dist[i][j]==-1) {
          dist[i][j]=INF;
        }
      }
    }

    for(int i=0;i<=n;i++){
      dp[i] =100000000000000.00;
    }
    floydWarshall();

    bool vis[n+1];
    memset(vis,false,sizeof(vis));
    for(int i=1;i<=q;i++){
      cin>>u>>v;
      double sol = solve(u,v,-1,vis);
      printf("%.6f\n",sol);
    }

  }
  return 0;
}
