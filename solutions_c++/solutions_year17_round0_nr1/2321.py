#include <stdio.h>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
int i, j, t, n, m, l, r, k, z, y, x;
char a[1005];
inline void change(char& c)
{
	if (c == '-') c = '+';
	else if (c == '+') c = '-';
}
int main()
{
	int T;
	scanf("%d", &T);
	for (int I = 1; I <= T; I++)
	{
		scanf("%s", a);
		scanf("%d", &k);
		printf("Case #%d: ", I);
		n = strlen(a);
		z = 0;
		for (i = 0; i <= n - k; i++) if (a[i] == '-')
			{
				for (j = 0; j < k; j++) change(a[i + j]);
				z++;
			}
		for (i = n - k + 1; i < n; i++) if (a[i] == '-') break;
		if (i >= n) printf("%d\n", z);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
