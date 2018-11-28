#include <algorithm>
#include <iostream>
#include <climits>
#include <cfloat>
#include <cstdio>

using namespace std;

typedef long long LL;
typedef long double db;

const db FINF=DBL_MAX/3;
const LL INF=LLONG_MAX/3;
const int N=105;

int e[N],s[N];
int n,q,T;
LL dist[N][N];
db f[N][N];

template <typename tp>
void floyd(tp *d)
{
	for (int k=1;k<=n;++k)
		for (int i=1;i<=n;++i)
			if (i!=k)
				for (int j=1;j<=n;++j)
					if (i!=j&&j!=k)
						d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
}

int main()
{
	freopen("express.in","r",stdin),freopen("express.out","w",stdout);
	int cnt=0;
	for (scanf("%d",&T);T--;printf("\n"))
	{
		printf("Case #%d: ",++cnt);
		scanf("%d%d",&n,&q);
		for (int i=1;i<=n;++i) scanf("%d%d",&e[i],&s[i]);
		for (int i=1;i<=n;++i)
			for (int j=1;j<=n;++j)
			{
				scanf("%lld",&dist[i][j]);
				if (dist[i][j]==-1) dist[i][j]=INF;
			}
		floyd(dist);
		for (int i=1;i<=n;++i)
			for (int j=1;j<=n;++j)
				if (dist[i][j]<=e[i]) f[i][j]=(1.*dist[i][j])/(1.*s[i]);
				else f[i][j]=FINF;
		floyd(f);
		for (int x,y;q--;printf("%.9lf ",(double)f[x][y])) scanf("%d%d",&x,&y);
	}
	fclose(stdin),fclose(stdout);
	return 0;
}