#include <cstdio>

#define inf 1000000007

int T,cas,s[6],i,j,k,g,p,t,ans,n,f[111][111][111][4];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (cas=1; cas<=T; ++cas)
	{
		scanf("%d%d", &n, &p);
		s[0] = s[1] = s[2] = s[3] = 0;
		for (i=1; i<=n; ++i)
		{
			scanf("%d", &g);
			s[g%p]++;
		}
		for (i=0; i<=s[1]; ++i)
		for (j=0; j<=s[2]; ++j)
		for (k=0; k<=s[3]; ++k)
		for (t=0; t<p; ++t) f[i][j][k][t] = -inf;
		f[s[1]][s[2]][s[3]][0] = 0;
		for (i=s[1]; i>=0; --i)
		for (j=s[2]; j>=0; --j)
		for (k=s[3]; k>=0; --k)
		for (t=0; t<p; ++t)
		{
			if (i > 0)
			{
				if (f[i][j][k][t]+(!t) > f[i-1][j][k][(t+p-1)%p]) f[i-1][j][k][(t+p-1)%p] = f[i][j][k][t]+(!t);
			}
			if (j > 0)
			{
				if (f[i][j][k][t]+(!t) > f[i][j-1][k][(t+p-2)%p]) f[i][j-1][k][(t+p-2)%p] = f[i][j][k][t]+(!t);
			}
			if (k > 0)
			{
				if (f[i][j][k][t]+(!t) > f[i][j][k-1][(t+p-3)%p]) f[i][j][k-1][(t+p-3)%p] = f[i][j][k][t]+(!t);
			}
		}
		ans = -inf;
		for (t=0; t<p; ++t)
		if (f[0][0][0][t] > ans) ans = f[0][0][0][t];
		printf("Case #%d: %d\n", cas, ans+s[0]);
	}
	return 0;
}

