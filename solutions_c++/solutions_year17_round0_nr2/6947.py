#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

#define FOR(a,b,c) for (int (a)=(b);(a)<(c);++(a))
#define FORN(a,b,c) for (int (a)=(b);(a)<=(c);++(a))
#define FORD(a,b,c) for (int (a)=(b);(a)>=(c);--(a))
#define MAX(a,b) a = max(a,b)
#define MIN(a,b) a = min(a,b)
#define SIZE(v) (int)v.size()

inline void OPEN(string s) 
{
	freopen((s + ".in").c_str(), "r", stdin);
	freopen((s + ".out").c_str(), "w", stdout);
}

int digits[19];

int num2digit(long long num)
{
	int len = 0;
	while (num >= 10)
	{
		digits[len++] = num % 10;
		num /= 10;
	}
	digits[len++] = num;

	return len;
}

int main()
{
	OPEN("B-large");
	int T;
	long long N;

	scanf("%d", &T);
	FORN(i, 1, T)
	{
		printf("Case #%d: ", i);
		scanf("%lld", &N);
		memset(digits, 0, sizeof(digits));
		int len = num2digit(N);

		FORN(j, 0, len - 1)
		{
			if (digits[j] < digits[j + 1])
			{
				FORN(k, 0, j)
					digits[k] = 9;

				digits[j + 1] -= 1;
			}
		}

		if (digits[len - 1] > 0)
			printf("%d", digits[len - 1]);

		FORD(j, len - 2, 0)
		{
			printf("%d", digits[j]);
		}

		printf("\n");
	}
	return 0;
}
