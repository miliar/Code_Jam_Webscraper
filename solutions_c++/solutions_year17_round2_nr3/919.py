#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double db;
const int N=105;
int n,q;
ll d[N][N],e[N],s[N];
db dist[N][N];
void solve()
{
  scanf("%d%d",&n,&q);
  for(int i=1; i<=n; ++i) scanf("%lld%lld",&e[i],&s[i]);
  for(int i=1; i<=n; ++i) 
    for(int j=1; j<=n; ++j)
    {
      scanf("%lld",&d[i][j]);
      if(d[i][j]==-1) 
        d[i][j]=1e18;
    }
  for(int k=1; k<=n; ++k)
    for(int i=1; i<=n; ++i)
      for(int j=1; j<=n; ++j)
        d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
  for(int i=1; i<=n; ++i)
  {
    priority_queue<pair<db,int>> Q; Q.push(make_pair(0,i));
    for(int v=1; v<=n; ++v) dist[i][v]=1e18;
    dist[i][i]=0;
    while(!Q.empty())
    {
      int v=Q.top().second; db di=-Q.top().first; Q.pop();
      if(dist[i][v]!=di) continue;
      for(int u=1; u<=n; ++u) if(d[v][u]!=(ll)1e18 && e[v]>=d[v][u])
      { 
        if(dist[i][u]>dist[i][v]+((db)d[v][u]/(db)s[v]))
        {
          dist[i][u]=dist[i][v]+(db)d[v][u]/(db)s[v];
          Q.push(make_pair(-dist[i][u],u));
        }
      }
    }
  }
  for(int i=1; i<=q; ++i)
  {
    int u,k; scanf("%d%d",&u,&k);
    printf("%.10Lf ",dist[u][k]);
  }
  printf("\n");
}
int main()
{
	int tt; scanf("%d",&tt); 
	for(int i=1; i<=tt; ++i)
	{
		printf("Case #%d: ",i);
		solve();
	}
}
