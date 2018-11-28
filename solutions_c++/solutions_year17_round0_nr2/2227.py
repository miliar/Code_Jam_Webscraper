#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int test, a[21], m;
long long n;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &test);
	for (int uu = 1; uu <= test; uu++)
	{
		scanf("%lld", &n);
		++n; m = 0;
		for (; n; n /= 10)
			a[++m] = n % 10;
		for (int i = 1, j = m; i < j; ++i, --j)
			swap(a[i], a[j]);
		long long ans = 0, pre = 0;
		int L = 0;
		for (int i = 1; i <= m; i++)
		{
			if (a[i] - 1 >= L) 
			{
				long long tmp = pre;
				tmp *= 10; tmp += a[i] - 1;
				for (int j = i + 1; j <= m; j++)
					tmp *= 10, tmp += 9;
				ans = max(ans, tmp);
			}
			if (a[i] >= L)
			{
				L = a[i];
				pre = pre * 10 + a[i];
			}
			else
				break;
		}
		printf("Case #%d: %lld\n", uu, ans);
	}
}
