#include<bits/stdc++.h>
using namespace std;
const int maxn=200;
long long d[maxn][maxn];
int e[maxn],s[maxn];
int inf= (~0u)>>2;
vector<pair<int,double> > mp[maxn];
double dis[maxn];
int n;
priority_queue<pair<double,int> > q;
void dij(int s)
{
	for(int i=1;i<=n;++i)dis[i]=1e300;
	dis[s]=0;
	q.push(make_pair(0,s));
	while(!q.empty())
	{
		int u=q.top().second;
		double len=-q.top().first;
		q.pop();
		for(int i=0;i<mp[u].size();++i)
		{
			int v=mp[u][i].first;
			if(dis[v]>dis[u]+mp[u][i].second)
			{
				dis[v]=dis[u]+mp[u][i].second;
				//cout <<dis[v]<<" "<<u<<" "<<v<<endl;
				q.push(make_pair(-dis[v],v));
			}
		}
	}
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;++cas)
	{
		int Q;
		scanf("%d%d",&n,&Q);
		for(int i=1;i<=n;++i)
			scanf("%d%d",&e[i],&s[i]);
		for(int i=1;i<=n;++i)
			for(int j=1;j<=n;++j)
			{
				scanf("%I64d",&d[i][j]);
				if(d[i][j]==-1)d[i][j]=inf;
			}
		for(int k=1;k<=n;k++)
			for(int i=1;i<=n;i++)
				for(int j=1;j<=n;j++) 
					if(d[i][k]+d[k][j]<d[i][j]) 
						d[i][j]=d[i][k]+d[k][j];
		//for(int i=1;i<=n;++i,cout <<endl) for(int j=1;j<=n;++j)cout <<d[i][j]<<" ";
		for(int i=1;i<=n;++i)
		{
			mp[i].clear();
			for(int j=1;j<=n;++j)
			{
				if(i==j)continue;
				if(d[i][j]<=e[i])
				{
					//cout <<i<<" "<<j<<" "<<d[i][j]<<" "<<double(d[i][j])/s[i]<<" "<<s[i]<<endl;
					mp[i].push_back(make_pair(j,double(d[i][j])/s[i]));
				}
			}
		}
		printf("Case #%d:",cas);
		for(int i=0;i<Q;++i)
		{
			int u,v;
			scanf("%d%d",&u,&v);
			dij(u);
			printf(" %.6f",dis[v]);
		}
		puts("");
	}
	return 0;
}
