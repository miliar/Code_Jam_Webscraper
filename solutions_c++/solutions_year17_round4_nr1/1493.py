#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int cases;
	scanf("%d", &cases);
	for (int _case = 0; _case < cases; _case++)
	{
		int n, p;
		scanf("%d %d", &n, &p);
		vector<int> g(n);
		for (int i = 0; i < n; i++)
			scanf("%d", &g[i]);

		vector<int> cnt(p, 0);
		for (int i = 0; i < n; i++)
			cnt[g[i] % p]++;

		int ans = 0;
		if (p == 2)
		{
			ans = cnt[0] + (cnt[1] + 1) / 2;
		}
		else if (p == 3)
		{
			ans = cnt[0];
			if (cnt[1] > cnt[2])
				ans += cnt[2] + (cnt[1] - cnt[2] + 2) / 3;
			else
				ans += cnt[1] + (cnt[2] - cnt[1] + 2) / 3;
		}
		else
		{
			ans = cnt[0] + cnt[2] / 2;
			cnt[2] %= 2;
			int i = cnt[1] > cnt[3] ? 1 : 3;
			ans += cnt[4 - i];
			cnt[i] -= cnt[4 - i];
			if (cnt[2])
				cnt[i] += 2;
			ans += (cnt[i] + 3) / 4;
		}

		printf("Case #%d: %d\n", _case + 1, ans);
	}
	
	return 0;
}