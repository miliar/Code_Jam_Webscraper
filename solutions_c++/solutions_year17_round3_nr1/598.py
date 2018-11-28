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

#define PI 3.1415926535897932384626433832795028841971L

struct Pancake
{
	long long int r;
	long long int h;
};

std::vector<Pancake> pancakes;

void solve()
{
	int n, k;

	scanf("%d %d", &n, &k);

	pancakes.clear();

	for (int i = 0; i < n; i++)
	{
		Pancake pancake;

		scanf("%lld %lld", &pancake.r, &pancake.h);

		pancakes.push_back(pancake);
	}

	std::sort(pancakes.begin(), pancakes.end(), [](const Pancake& l, const Pancake& r)
	{
		return r.h * r.r * 2 < l.h * l.r * 2;
	});
	
	long long int max = 0;

	for (int i = 0; i < n; i++)
	{
		int nk = 1;
		long long int res = pancakes[i].r * pancakes[i].r + pancakes[i].r * pancakes[i].h * 2LL;

		for (int j = 0; j < n; j++)
		{
			if (i == j || pancakes[i].r < pancakes[j].r)
				continue;

			if (nk == k)
				break;

			res += pancakes[j].h * pancakes[j].r * 2LL;

			nk++;
		}

		max = std::max(res, max);
	}

	long double d = PI;
	d *= max;

	printf("%.10lF\n", d);
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