#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int, int> pii;

const LL MOD = 1000000007LL;

int arr[111], mcnt[111];

int main()
{
	int T, N, P;

	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d%d", &N, &P);
		memset(mcnt, 0, sizeof(mcnt));
		for (int i = 0; i < N; i++)
		{
			scanf("%d", arr + i);
			mcnt[arr[i] % P]++;
		}
		int ans = 0;
		if (P == 2)
		{
			ans = mcnt[0] + (mcnt[1] + 1) / 2;
		}
		if (P == 3)
		{
			ans = mcnt[0];
			
			int tmp = min(mcnt[1], mcnt[2]);
			ans += tmp;
			mcnt[1] -= tmp;
			mcnt[2] -= tmp;
			
			ans += (mcnt[1] + 2) / 3;
			ans += (mcnt[2] + 2) / 3;
		}
		if (P == 4)
		{
			ans = mcnt[0];
			
			int tmp = mcnt[2] / 2;
			ans += tmp;
			mcnt[2] -= 2 * tmp;
			
			tmp = min(mcnt[1], mcnt[3]);
			ans += tmp;
			mcnt[1] -= tmp;
			mcnt[3] -= tmp;

			tmp = mcnt[1] / 3;
			ans += tmp;
			mcnt[1] -= 3 * tmp;

			tmp = mcnt[3] / 3;
			ans += tmp;
			mcnt[3] -= 3 * tmp;

			if (mcnt[2] > 0)
			{
				if (mcnt[1] >= 2)
				{
					ans++;
					mcnt[1] -= 2;
					mcnt[2]--;
				}
				if (mcnt[3] >= 2)
				{
					ans++;
					mcnt[3] -= 2;
					mcnt[2]--;
				}
			}

			if (mcnt[1] + mcnt[2] + mcnt[3] > 0)
				ans++;
		}
		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}