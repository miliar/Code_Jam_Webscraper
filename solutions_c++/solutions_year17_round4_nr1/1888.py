#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <cmath>
#include <map>
#include <queue>

using namespace std;
const int maxn = 110;
int test, n, p, d[5], ans, d1, d2;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &test);
	for (int t = 1; t <= test; ++t)
	{
		ans = n;
		memset(d, 0, sizeof(d));
		d1 = 0;
		d2 = 0;
		scanf("%d%d", &n, &p);
		for (int i = 1; i <= n; ++i) 
			{
				int x;
				scanf("%d", &x);
				if (x == 1) ++d1;
				else 
					if (x == 2) ++d2;
					else ++d[x % p];
				//printf("%d\n", x % p);
			}
		if (p == 2)
		{
			d[0] += d2;
			d[1] += d1;
			ans = d[0] + d[1] / 2 + d[1] % 2;
		}
		if (p == 3)
		{
			d[2] += d2;
			int x = min(d1 , d[2]);
			ans = d[0] + x;
			d1 -= x;
			d[2] -= x;
			x = min (d[1], d[2]);
			ans += x;
			d[1] -= x;
			d[2] -= x;
			ans += d[1] / 3;
			d[1] %= 3;
			ans += d[2] / 3;
			d[2] %= 3;
			ans += min(1,max(d[2],max(d1,d[1])));
		}
		if (p == 4)
		{
			ans = d[0];
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}