#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int T;
char c[10000];

void Solve()
{
	char temp;
	scanf("%c", &temp);
	int n = 0, ans = 0, k;
	while (temp != ' ')
	{
		c[n++] = temp;
		scanf("%c", &temp);
	}
	scanf("%d\n", &k);
	for (int i = 0; i < n-k + 1; i++)
	{
		if (c[i] == '-')
		{
			for (int j = i; j < i + k; j++)
				c[j] = (c[j] == '+') ? '-' : '+';
			ans++;
		}
	}
	for (int i = 0; i < n; i++)
		if (c[i] == '-')
		{
			printf("IMPOSSIBLE\n");
			return;
		}
	printf("%d\n", ans);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d\n", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
}