#include <cstdio>

int T,d,n,k,s,i,cas;
double mxt;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	for (cas=1; cas<=T; ++cas)
	{
		scanf("%d%d", &d, &n);
		mxt = 0;
		for (i=1; i<=n; ++i)
		{
			scanf("%d%d", &k, &s);
			if (double(d-k)/s > mxt) mxt = double(d-k)/s;
		}
		printf("Case #%d: %.6lf\n", cas, d/mxt+1e-8);
	}
	return 0;
}
			
