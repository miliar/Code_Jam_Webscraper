#include <bits/stdc++.h>
using namespace std;

int T;
long long n, K, num1, num2, sum1, sum2, now;

int main()
{
	
	freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);
	
	scanf("%d", &T);
	for (int Case = 1; Case <= T; ++ Case)
	{
		printf("Case #%d: ", Case);
		scanf("%lld%lld", &n, &K);
		if (K == 1)
		{
			printf("%lld %lld\n", n / 2, (n - 1) / 2);
		} else {
			sum1 = (n - 1) / 2;
			sum2 = n / 2;
			num1 = num2 = 1;
			now = 1;
			while (now < K)
			{
				if (now + num2 >= K)
				{
					printf("%lld %lld\n", sum2 / 2, (sum2 - 1) / 2);
					break;
				}
				if (now + num1 + num2 >= K)
				{
					printf("%lld %lld\n", sum1 / 2, (sum1 - 1) / 2);
					break;
				}
				now += num1 + num2;
				long long tmp1, tmp2, tnum1, tnum2;
				tmp1 = (sum1 - 1) / 2; tnum1 = num1;
				tmp2 = sum2 / 2; tnum2 = num2;
				if ((sum2 - 1) / 2 == tmp1) tnum1 += num2;
				else tnum2 += num2;
				if (sum1 / 2 == tmp1) tnum1 += num1;
				else tnum2 += num1;
				sum1 = tmp1; sum2 = tmp2; num1 = tnum1; num2 = tnum2;
			}
		}
	}
	return 0;
}

