#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <set>
#include <cmath>
#include <vector>
using namespace std;

#define FOR(a,b,c) for (int (a)=(b);(a)<(c);++(a))
#define FORN(a,b,c) for (int (a)=(b);(a)<=(c);++(a))
#define MAX(a,b) a = max(a,b)
#define MIN(a,b) a = min(a,b)
#define SIZE(v) (int)v.size()

inline void OPEN(string s) {
	freopen((s + ".in").c_str(), "r", stdin);
	freopen((s + ".out").c_str(), "w", stdout);
}

void PrintRet(long long num)
{
	if (num & 1)
	{
		if (num == 1)
			printf("0 0\n");
		else
			printf("%lld %lld\n", (num - 1) / 2, (num - 1) / 2);
	}
	else
	{
		if (num == 0)
			printf("0 0\n");
		else
			printf("%lld %lld\n", num / 2, num / 2 - 1);
	}
}

int main()
{
	OPEN("C-small-2-attempt0");
	int T;
	long long N, K;

	scanf("%d", &T);
	
	FORN(i, 1, T)
	{
		printf("Case #%d: ", i);
		scanf("%lld %lld", &N, &K);
		int sLevel = log2(K);
		long long y;
		long long z;
		long long resN = N - pow(2, sLevel) + 1;
		long long resK = K - pow(2, sLevel) + 1;
		long long lPow = pow(2, sLevel);

		long long lFirst = N / lPow;
		long long th = lPow - ((lFirst * lPow) - resN);

		if (resK <= th)
		{
			PrintRet(lFirst);
		}
		else
		{
			PrintRet(lFirst - 1);
		}
	}
	return 0;
}

