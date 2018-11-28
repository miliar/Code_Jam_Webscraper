#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <stack>
#include <math.h>
#include <memory.h>
#include <queue>

int n, q;
int edge[101][101];
int total[101];
int speed[101];
bool visited[101];
double min = DBL_MAX;

double minTime(int now, int goal, int horse, int remain, double nowVal)
{
	if (now == goal)
	{
		min = std::min(min, nowVal);
		return min;
	}

	if (nowVal >= min)
		return DBL_MAX;

	for (int i = 1; i <= n; i++)
	{
		if (visited[i])
			continue;

		if (edge[now][i] == -1)
		{
			continue;
		}

		visited[i] = true;
		if (remain >= edge[now][i])
		{
			double time = (double)edge[now][i] / speed[horse];
			minTime(i, goal, horse, remain - edge[now][i], nowVal + time);
		}

		if (now != horse && total[now] >= edge[now][i])
		{
			double time = (double)edge[now][i] / speed[now];
			minTime(i, goal, now, total[now] - edge[now][i], nowVal + time);
		}

		visited[i] = false;
	}

	return min;
}

void solve(int c)
{
	scanf("%d %d", &n, &q);

	for (int i = 1; i <= n; i++)
	{
		scanf("%d %d", &total[i], &speed[i]);
	}

	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			scanf("%d", &edge[i][j]);
		}
	}

	for (int i = 0; i < q; i++)
	{
		int s, e;

		scanf("%d %d", &s, &e);

		memset(visited, 0, sizeof(visited));
		min = DBL_MAX;

		printf("%lf ", minTime(s, e, s, total[s], 0.0));
	}

	printf("\n");
}

int main()
{
	int t;

	scanf("%d", &t);

	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve(i);
	}
}