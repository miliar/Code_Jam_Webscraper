#include <stdio.h>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
int i, j, t, n, m, l, r, k;
long double z, y, x;
int d;
struct horse
{
	int k, s;
	bool operator <(const horse& tmp) const
	{
		return (k == tmp.k) ? s < tmp.s : k < tmp.k;
	}
} a[1005];
int main()
{
	int T;
	scanf("%d", &T);
	for (int I = 1; I <= T; I++)
	{
		scanf("%d%d", &d, &n);
		for (i = 1; i <= n; i++)
		{
			scanf("%d%d", &a[i].k, &a[i].s);
			if (i == 1) x = (long double)a[1].s * a[1].k / (d - a[1].k) + a[1].s;
			x = min(x, (long double)a[i].s * a[i].k / (d - a[i].k) + a[i].s);
		}
		printf("Case #%d: %.7Lf\n", I, x);
	}
	return 0;
}
