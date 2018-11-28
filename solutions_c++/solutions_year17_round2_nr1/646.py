#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	int n , d;
	scanf("%d", &T);
	for (int z = 1; z <= T; z++)
	{
		scanf("%d %d ", &d, &n);
		double mxT = 0;
		for (int i = 0; i < n; i++)
		{
			int k, s;
			scanf("%d %d", &k, &s);
			mxT = max(mxT, (d - 1.0*k) / s);
		}
		printf("Case #%d: %.8lf\n", z, d / mxT);
	}
}