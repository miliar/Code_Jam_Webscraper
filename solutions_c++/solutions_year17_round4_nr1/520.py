#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);

	int n, p, g, mod[4], ans, tmp, stuff;
	for (int tt = 1; tt <= t; tt++)
	{
		scanf("%d %d", &n, &p);
		for (int i = 0; i < 4; i++)
		{
			mod[i] = 0;
		}
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &g);
			mod[g % p]++;
		}
		ans = mod[0];
		if (p == 2)
		{
			ans += (mod[1] + 1) / 2;
		}
		else if (p == 3)
		{
			tmp = min(mod[1], mod[2]);
			mod[1] -= tmp;
			mod[2] -= tmp;
			ans += tmp;
			ans += (mod[1] + 2) / 3;
			ans += (mod[2] + 2) / 3;
		}
		else if (p == 4)
		{
			tmp = min(mod[1], mod[3]);
			mod[1] -= tmp;
			mod[3] -= tmp;
			ans += tmp;
			ans += (mod[2] + 1) / 2;
			stuff = mod[1] + mod[3];
			if (mod[2] % 2 == 1)
			{
				ans += (stuff + 1) / 4;
			}
			else
			{
				ans += (stuff + 3) / 4;
			}
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}
