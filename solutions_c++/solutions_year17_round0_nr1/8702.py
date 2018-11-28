#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cstdlib>
#include <cstdio>
#include <queue>

using namespace std;

char str[1010];
int k;

char used[1 << 11];
int d[1 << 11];

void solve(int test)
{
	for (int i = 0; i < (1 << 11); i++)
	{
		used[i] = false;
		d[i] = -1;
	}
	int len = strlen(str);
	int state = 0;
	for (int i = 0; i < len; i++)
		state |= (str[i] == '+' ? (1 << i) : 0);
	queue<int> q;
	q.push(state);
	used[state] = true;
	d[state] = 0;
	while (!q.empty())
	{
		int cur = q.front();
		q.pop();
		for (int i = 0; i < len - k + 1; i++)
		{
			int tmp = cur;
			for (int j = 0; j < k; j++)
				tmp = tmp ^ (1 << (i + j));
			if (!used[tmp])
			{
				used[tmp] = true;
				d[tmp] = d[cur] + 1;
				q.push(tmp);
			}
		}
	}
	if (d[(1 << len) - 1] != -1)
		printf("Case #%d: %d\n", test, d[(1 << len) - 1]);
	else
		printf("Case #%d: IMPOSSIBLE\n", test);
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		scanf("%s%d", str, &k);
		solve(i + 1);
	}
	return 0;
}