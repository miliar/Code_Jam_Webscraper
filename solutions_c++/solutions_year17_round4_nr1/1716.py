#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <memory.h>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <stack>

void solve()
{
	int n, p;

	scanf("%d %d", &n, &p);

	int count = 0;
	int num[5] = { 0, };

	for (int i = 0; i < n; i++)
	{
		int g;
		scanf("%d", &g);

		if (g % p == 0)
			count++;
		else
			num[g % p]++;
	}

	if (p == 2)
	{
		count += (num[1] + 1) / 2;
	}
	else if (p == 3)
	{
		int min12 = std::min(num[1], num[2]);
		count += min12;

		num[1] -= min12;
		num[2] -= min12;
		count += (num[1] + 2) / 3;
		count += (num[2] + 2) / 3;
	}
	else if (p == 4)
	{
	}

	printf("%d\n", count);
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