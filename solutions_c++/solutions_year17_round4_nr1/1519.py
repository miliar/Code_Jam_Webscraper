#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;
int a[8];
int main()
{
	//freopen("aL.in", "r", stdin);
	//freopen("aL.out", "w", stdout);
	int T, N, P, x;
	cin >> T;
	for (int cs = 1; cs <= T; cs++)
	{
		memset(a, 0, sizeof a);
		cin >> N >> P;
		for (int i = 0; i < N; i++)
		{
			scanf("%d", &x);
			x %= P;
			a[x]++;
		}
		
		
		/*for (int i = 0; i < P; i++)
			printf(" %d", a[i]);
		printf("\n");*/
		
		int ans = a[0];
		
		if (P == 2)
		{
			ans += a[1] / 2;
			if (a[1] % 2 != 0)
				ans++;
		}
		else if (P == 3)
		{
			int p = min(a[1], a[2]), q = max(a[1], a[2]);
			ans += p + (q - p) / 3;
			if ((q - p) % 3 != 0)
				ans++;
		}
		else if (P == 4)
		{
			int p = min(a[1], a[3]), q = max(a[1], a[3]);
			ans += a[2] / 2 + p;
			if (a[2] % 2 == 1 && q - p >= 2)
			{
				a[2]--;
				q -= 2;
				ans++;
			}
			ans += (q - p) / 4;
			if (a[2] % 2 != 0 || (q - p) % 4 != 0)
				ans++;
		}
		printf("Case #%d: %d\n", cs, ans);
	}
	return 0;
}

