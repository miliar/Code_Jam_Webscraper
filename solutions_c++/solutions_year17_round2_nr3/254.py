#include <cstdio>

#define INF 100000000000000000LL

int T,cas,n,Q,i,j,k,bg,ed,s[111];
long long d[111][111],e[111];
double f[111][111],min;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	for (cas=1; cas<=T; ++cas)
	{
		scanf("%d%d", &n, &Q);
		for (i=1; i<=n; ++i) scanf("%lld%d", &e[i], &s[i]);
		for (i=1; i<=n; ++i)
		for (j=1; j<=n; ++j)
		{
			scanf("%lld", &d[i][j]);
			if (d[i][j] == -1) d[i][j] = INF;
			if (i==j) d[i][j] = 0;
		}
		for (k=1; k<=n; ++k)
		for (i=1; i<=n; ++i)
		for (j=1; j<=n; ++j)
		if (d[i][k]+d[k][j] < d[i][j]) d[i][j] = d[i][k]+d[k][j];
		printf("Case #%d:", cas);
		while (Q--)
		{
			scanf("%d%d", &bg, &ed);
			for (i=0; i<=n; ++i)
			for (j=1; j<=n; ++j) f[i][j] = INF;
			f[0][bg] = 0;
			for (i=0; i<n; ++i)
			for (j=1; j<=n; ++j)
			{
				for (k=1; k<=n; ++k)
				if (d[j][k] <= e[j])
				if (f[i][j]+d[j][k]*1.0/s[j] < f[i+1][k]) f[i+1][k] = f[i][j]+d[j][k]*1.0/s[j];
			}
			min = INF;
			for (i=0; i<=n; ++i)
			if (f[i][ed] < min) min = f[i][ed];
			printf(" %.6lf", min+1e-8);
		}
		printf("\n");
	}
	return 0;
}
			
