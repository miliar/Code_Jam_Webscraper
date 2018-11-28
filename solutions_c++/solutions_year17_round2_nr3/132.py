#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
long long dists[100][100];
long long range[100];
long long speed[100];
const long long inf=1LL<<50;
vector<bool>vis;
void floyd(int n)
{
	for(int k=0;k<n;k++)
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				dists[i][j]=min(dists[i][j],dists[i][k]+dists[k][j]);
}
vector<double> test()
{
	int n,q;
	scanf("%d%d",&n,&q);
	for(int i=0;i<n;i++)
		scanf("%lld%lld",range+i,speed+i);
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
		{
			scanf("%lld",&dists[i][j]);
			if(dists[i][j]==-1)
				dists[i][j]=inf;
		}
	floyd(n);
	vector<double>answers;
	for(int i=0;i<q;i++)
	{
		vis.clear();
		vis.resize(n,false);
		priority_queue<pair<double,int>,vector<pair<double,int>>,greater<pair<double,int>>>P;
		int u,v;
		scanf("%d%d",&u,&v);
		u--;
		v--;
		P.push({0.0,u});
		while(!vis[v])
		{
			auto e=P.top();
			P.pop();

			if(e.second==v)answers.push_back(e.first);
			if(vis[e.second])continue;
			vis[e.second]=true;
			for(int j=0;j<n;j++)
			{
				if(vis[j])continue;
				if(dists[e.second][j]>range[e.second])continue;
				P.push({e.first+dists[e.second][j]*1.0/speed[e.second],j});
			}
		}
	}
	return answers;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		auto res=test();
		printf("Case #%d: ",i);
		for(auto &e:res)
			printf("%.6lf ",e);
		printf("\n");
	}
}
