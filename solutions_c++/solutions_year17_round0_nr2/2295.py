#include <stdio.h>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
int i, j, t, n, m, l, r, k, z, y, x;
char a[105];
int main()
{
	int T;
	scanf("%d", &T);
	for (int I = 1; I <= T; I++)
	{
		scanf("%s", a);
		printf("Case #%d: ", I);
		n = strlen(a);
		x = n;
		for (i = n - 2; i >= 0; i--) if (a[i] > a[i + 1])
			{
				a[i] -= 1;
				x = i + 1;
			}
		if (a[0] == '0')
		{
			for (i = 0; i < n - 1; i++) printf("9");
			printf("\n");
		}
		else
		{
			for (i = 0; i < x; i++) printf("%c", a[i]);
			for (i = x; i < n; i++) printf("9");
			printf("\n");
		}
	}
	return 0;
}
