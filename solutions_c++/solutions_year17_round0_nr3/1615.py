#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
int T;
LL n, K, num1, num2, sum1, sum2, cnt;

int main()
{
	freopen("C3.in", "r", stdin);
	freopen("C3.out", "w", stdout);
	scanf("%d", &T);
	for (int _cas = 1; _cas <= T; _cas++){
		printf("Case #%d: ", _cas);
		scanf("%lld%lld", &n, &K);
		if (K == 1) printf("%lld %lld\n", n / 2, (n - 1) / 2);
		else {
			sum1 = (n - 1) / 2;
			sum2 = n / 2;
			num1 = num2 = 1;
			cnt = 1;
			while (cnt < K) {
				if (cnt + num2 >= K) {
					printf("%lld %lld\n", sum2 / 2, (sum2 - 1) / 2);
					break;
				}
				else if (cnt + num1 + num2 >= K) {
					printf("%lld %lld\n", sum1 / 2, (sum1 - 1) / 2);
					break;
				}
				cnt += num1 + num2;
				LL tmp1, tmp2, tnum1, tnum2;
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
