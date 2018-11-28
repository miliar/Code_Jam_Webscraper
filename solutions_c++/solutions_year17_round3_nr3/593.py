#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <stack>
#define _USE_MATH_DEFINES
#include <math.h>
#include <memory.h>
#include <queue>

void solve()
{
	int n, k;

	scanf("%d %d", &n, &k);

	long double u;

	scanf("%Lf", &u);

	std::vector<long double> unit;

	for (int i = 0; i < n; i++)
	{
		long double un;
		scanf("%Lf", &un);
		unit.push_back(un);
	}

	unit.push_back(1.0);

	std::sort(unit.begin(), unit.end());

	long double nowVal = unit[0];

	for (int i = 1; i < unit.size(); i++)
	{
		if ((unit[i] - nowVal) * i < u)
		{
			u -= (unit[i] - nowVal) *i;

			for (int j = 0; j <= i; j++)
				unit[j] = unit[i];

			nowVal = unit[i];
		}
		else
		{
			for (int j = 0; j < i; j++)
			{
				unit[j] += u / i;
			}

			break;
		}
	}

	long double prior = 1;

	for (int i = 0; i < unit.size() - 1; i++)
		prior *= unit[i];

	printf("%Lf\n",prior);
}

int main()
{
	int T;

	scanf("%d", &T);

	for (int i = 1; i <= T; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}