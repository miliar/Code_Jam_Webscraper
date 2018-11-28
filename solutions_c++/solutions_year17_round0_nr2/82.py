#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int T;
char c[100];

void Solve()
{
	char temp;
	scanf("%c", &temp);
	int n = 0; bool flag = false;
	while (temp != '\n')
	{
		c[n++] = temp;
		scanf("%c", &temp);
	}
	for (int i = n - 1; i > 0; i--)
	{
		if (c[i] < c[i - 1])
		{
			c[i - 1] = c[i - 1] - 1;
			for (int j = i; j < n; j++)
				c[j] = '9';
		}
	}
	int i = 0;
	while (c[i] == '0') i++;
	for (; i < n; i++)
		printf("%c", c[i]);
	printf("\n");
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d\n", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
}