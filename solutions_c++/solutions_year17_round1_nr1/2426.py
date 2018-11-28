#include <stdio.h>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
int i, j, t, n, m, l, r, k, z, y, x;
int c;
char a[35][35];
bool b[35];
int main()
{
	int T;
	scanf("%d", &T);
	for (int I = 1; I <= T; I++)
	{
		memset(b, false, sizeof(b));
		scanf("%d%d", &r, &c);
		for (i = 0; i < r; i++)
		{
			scanf("%s", a[i]);
			for (j = 0; j < c; j++) if (a[i][j] != '?') break;
			if (j >= c) b[i] = true;
		}
		for (i = 0; i < r; i++) if (!b[i]) break;
		if (i > 0) for (j = i - 1; j >= 0; j--) memcpy(a[j], a[i], c);
		for (i += 1; i < r; i++) if (b[i]) memcpy(a[i], a[i - 1], c);
		for (i = 0; i < r; i++)
		{
			for (j = 0; j < c; j++) if (a[i][j] != '?') break;
			for (k = 0; k < j; k++) a[i][k] = a[i][j];
			for (j += 1; j < c; j++) if (a[i][j] == '?') a[i][j] = a[i][j - 1];
		}
		printf("Case #%d:\n", I);
		for (i = 0; i < r; i++) printf("%s\n", a[i]);
	}
	return 0;
}
