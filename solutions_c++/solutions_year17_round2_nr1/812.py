#include<cstdio> 

int T, D, n, k, s;
double ans;

int main()
{
//	freopen("A.in", "r", stdin);
//	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (int I = 1; I <= T; I++)
	{
		ans = -1;
		scanf("%d%d", &D, &n);
		for (int i = 1; i <= n; i++)
		{
			scanf("%d%d", &k, &s);
			double temp = 1.0 * (D - k) / s ;
			temp = 1.0 * D / temp;
			if (ans == -1 || (ans != -1 && ans > temp)) ans = temp;
		}
		printf("Case #%d: %lf\n", I, ans);
	}
	return 0;
}
