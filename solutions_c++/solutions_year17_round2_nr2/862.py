#include <bits/stdc++.h>

using namespace std;

int T;
int N,Q;
int e[110],s[110];
long long dist[110][110];
long double d1[110][110];
int u[110],v[110];

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d",&N,&Q);
		for(int i=1;i<=N;i++)
			scanf("%d%d",e+i,s+i);

		for(int i=1;i<=N;i++)
			for(int j=1;j<=N;j++)
			{
				scanf("%I64d",&dist[i][j]);
				if(dist[i][j]==-1)
					dist[i][j]=(long long)1000000000LL*1000000000LL;
			}
		for(int k=1;k<=N;k++)
			for(int i=1;i<=N;i++)
				for(int j=1;j<=N;j++)
					if(dist[i][k]+dist[k][j]<dist[i][j])
						dist[i][j]=dist[i][k]+dist[k][j];

		for(int i=1;i<=N;i++)
			for(int j=1;j<=N;j++)
			{
				if(dist[i][j]<=e[i])
					d1[i][j]=(long double)dist[i][j]/s[i];
				else
					d1[i][j]=(long double)1e10*(long double)1e10;
			}

		for(int k=1;k<=N;k++)
			for(int i=1;i<=N;i++)
				for(int j=1;j<=N;j++)
					if(d1[i][k]+d1[k][j]<d1[i][j])
						d1[i][j]=(double)d1[i][k]+d1[k][j];

		for(int i=1;i<=Q;i++)
			scanf("%d%d",u+i,v+i);

		printf("Case #%d:",tt);
		for(int i=1;i<=Q;i++)
			printf(" %.10f",(double)d1[u[i]][v[i]]);
		printf("\n");
	}
	return 0;
}
/*
1
4 3
30 60
10 1000
12 5
20 1
-1 10 -1 31
10 -1 10 -1
-1 -1 -1 10
15 6 -1 -1
2 4
3 1
3 2
*/