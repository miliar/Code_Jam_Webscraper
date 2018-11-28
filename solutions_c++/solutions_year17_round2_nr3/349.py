#include<bits/stdc++.h>
using namespace std;
typedef pair<double, int> di;
int V,Q,e[105],s[105],d[105][105];
double Time[105][105], dist[105];
void Dijkstra(int U)
{
	for(int i=1; i<=V; i++) dist[i] = 1e13;
	dist[U] = 0;
	priority_queue<di, vector<di>, greater<di> > pq;
	pq.push(di(0, U));
	while(pq.size())
	{
		double w = pq.top().first;
		int u = pq.top().second;
		pq.pop();
		for(int i=1; i<=V; i++)
			if(d[u][i]!=-1 && dist[i] > dist[u] + d[u][i])
			{
				dist[i] = dist[u] + d[u][i];
				pq.push(di(dist[i],i));
			}
	}
	for(int i=1; i<=V; i++)
		if(dist[i]!=-1 && dist[i]<=e[U])
		{
			Time[U][i] = dist[i]/s[U];
			//printf("Dist %d %d %lf %lf\n",U,i,dist[i], Time[U][i]);
		}
}
void init()
{
	for(int i=1; i<=V; i++)
		for(int j=1; j<=V; j++) Time[i][j] = -1;
	for(int i=1; i<=V; i++) Time[i][i] = 0;
	for(int i=1; i<=V; i++) Dijkstra(i);
	for(int k=1; k<=V; k++)
		for(int i=1; i<=V; i++)
			for(int j=1; j<=V; j++)
				if(Time[i][k] != -1 && Time[k][j] != -1)
					if(Time[i][j]== -1 || Time[i][j] > Time[i][k] + Time[k][j]) Time[i][j] = Time[i][k] + Time[k][j];
}
void execute()
{
	int u,v;
	scanf("%d %d",&V,&Q);
	for(int i=1; i<=V; i++) scanf("%d %d",&e[i],&s[i]);
	for(int i=1; i<=V; i++)
		for(int j=1; j<=V; j++) scanf("%d",&d[i][j]);
	init();
	for(int i=1; i<=Q; i++)
	{
		scanf("%d %d",&u,&v);
		printf(" %.6lf",Time[u][v]);
	}
	printf("\n");
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	int test;
	scanf("%d",&test);
	for(int tc=1; tc<=test; tc++)
	{
		printf("Case #%d:",tc);
		execute();
	}
	return 0;
}
