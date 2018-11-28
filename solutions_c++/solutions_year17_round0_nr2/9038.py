#pragma warning(disable : 4996)
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

typedef long long LL;

LL N;

LL operate(LL n)
{
	LL std = 1, ret = n;
	while (std <= n)
		std *= 10;

	std /= 10;

	while (std / 10 != 0)
	{
		int a, b;
		a = (n / std) % 10;
		b = (n / (std / 10)) % 10;

		if (a > b)
		{
			ret = ((n / std) - 1) * std + (std - 1);
			break;
		}

		std /= 10;
	}
	return ret;
}

void solve()
{
	scanf("%lld", &N);
	LL n, ret = N;

	do {
		n = ret;
		ret = operate(ret);
	} while (ret != n);
	
	printf("%lld\n", n);
}

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}