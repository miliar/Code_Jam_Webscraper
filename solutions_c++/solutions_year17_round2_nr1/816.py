#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <stack>
#include <math.h>
#include <memory.h>
#include <queue>

void solve()
{
	int d, n;
	//first = Ki, second = Si
	std::vector<std::pair<int, int>> values;

	scanf("%d %d", &d, &n);

	float maxHour = 0;

	for (int i = 0; i < n; i++)
	{
		std::pair<int, int> value;
		scanf("%d %d", &value.first, &value.second);
		values.push_back(value);
		maxHour = std::max(maxHour, (d - value.first) / (float)value.second);
	}

	std::sort(values.begin(), values.end(), [](auto& a, auto& b)
	{
		return a.first < b.first;
	});

	printf("%f\n", d / maxHour);
}

int main()
{
	int t;

	scanf("%d", &t);

	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
}