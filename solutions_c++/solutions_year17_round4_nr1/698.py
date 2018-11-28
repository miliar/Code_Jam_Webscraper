#include <bits/stdc++.h>
using namespace std;
int t; 
int main()
{
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		int n, p;
		scanf("%d%d", &n, &p);
		int d[5];
		fill_n(d, 5, 0);
		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			int a;
			scanf("%d", &a);
			d[a%p]++;
		}
		if (p == 2)
		{
			ans = d[0];
			ans+=d[1]/2;
			if (d[1] % 2) ans++;
		}
		else
		{
			ans = d[0];
			int am = min(d[1], d[2]);
			ans+=am;
			d[1]-=am;
			d[2]-=am;
			ans += d[1]/3;
			if (d[1] % 3) ans++;
			ans += d[2]/3;
			if (d[2] % 3) ans++;
		}
		printf("Case #%d: %d\n", i, ans);

	}
}