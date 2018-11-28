#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
using namespace std;

int	Hd, Ad, Hk, Ak, B, D;

long long Calc(int b, int d)
{
	long long result = 0;
	int hd = Hd, ad = Ad, hk = Hk, ak = Ak;
	bool cured = false;
	while (true)
	{
		++result;
		if (hk > ad && hd <= ak - D * (d > 0))
		{
			if (cured)
				return -1;
			cured = true;
			hd = Hd;
		}
		else
		{
			cured = false;
			if (d > 0)
			{
				ak -= D;
				--d;
				if (ak < 0)
				{
					ak = 0;
					d = 0;
				}
			}
			else if (b > 0)
			{
				ad += B;
				--b;
			}
			else
			{
				hk -= ad;
				if (hk <= 0)
					return result;
			}
		}
		hd -= ak;
		if (hd <= 0)
			return -1;
	}
}

long long Solve()
{
	scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
	long long min = -1;
	for (int b = 0; b < 100; ++b)
	{
		for (int d = 0; d < 100; ++d)
		{
			long long curr = Calc(b, d);
			if (curr == -1)
				continue;
			if (min == -1 || min > curr)
				min = curr;
		}
	}
	return min;
}


int main()
{
	int i, t;
	scanf("%d", &t);
	for (i = 0; i < t; ++i)
	{
		long long result = Solve();
		printf("Case #%d: ", i + 1);
		if (result != -1)
			printf("%I64d\n", result);
		else
			puts("IMPOSSIBLE");
	}
	return 0;
}
