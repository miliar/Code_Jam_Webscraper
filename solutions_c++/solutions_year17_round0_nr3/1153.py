#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

LL arr[333][2];

int main()
{
	int T, ind, len;
	LL N, K, cnt, x, x2;

	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%lld%lld", &N, &K);

		memset(arr, 0, sizeof(arr));

		arr[0][0] = N;
		arr[0][1] = 1;
		len = 1;

		cnt = 0;
		ind = 0;
		while (cnt < K)
		{
			x = arr[ind][0];
			cnt += arr[ind][1];
			if (cnt >= K)
			{
				printf("Case #%d: %lld %lld\n", t, x >> 1, (x - 1) >> 1);
				break;
			}
			
			x2 = x >> 1;
			if (arr[len - 1][0] == x2)
				arr[len - 1][1] += arr[ind][1];
			else
			{
				arr[len][0] = x2;
				arr[len][1] = arr[ind][1];
				len++;
			}
			
			x2 = (x - 1) >> 1;
			if (arr[len - 1][0] == x2)
				arr[len - 1][1] += arr[ind][1];
			else
			{
				arr[len][0] = x2;
				arr[len][1] = arr[ind][1];
				len++;
			}
			ind++;
		}
	}

	return 0;
}