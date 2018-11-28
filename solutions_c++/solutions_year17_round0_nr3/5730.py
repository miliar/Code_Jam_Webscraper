#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int MAXN = 1000005;
int a[MAXN];
int n, k;
int ckL(int x)
{
	int i;
	for (i = 0;; i++)
	{
		if (a[x-i-1]) break;
	}
	return i;
}
int ckR(int x)
{
	int i;
	for (i = 0;; i++)
	{
		if (a[x+i+1]) break;	
	}
	return i;
}
int GetX()
{
	int x, mi = 0, mx = 0;
	for (int i = 1; i <= n; i++)
	{
		if (!a[i])
		{
			int tmp = min(ckL(i), ckR(i));
			int tmp2 = max(ckL(i), ckR(i));
			if (tmp > mi || tmp == mi && tmp2 > mx)
			{
				x = i;
				mi = tmp;
				mx = tmp2;
			}
		}
	}
	if (mx == 0)
	{
		for (int i = 1; i <= n; i++)
			if (!a[i]) return i;
	}
	return x;
}
int t;
int main()
{
//	freopen("C-small-1-attempt0.in", "r", stdin);
//	freopen("C-small-1-attempt0.out", "w", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		memset(a, 0, sizeof(a));
		scanf("%d%d", &n, &k);
		a[0] = a[n+1] = 1;
		for (int i = 1; i < k; i++)
		{
			int x = GetX();
	//		cout << x << endl;
			a[x] = 1;
		}
		int x = GetX();
//		cout << x << endl;
		int lx = ckL(x);
		int rx = ckR(x);
		printf("Case #%d: %d %d\n", tt, max(lx, rx), min(lx, rx));
	}
}
/*
5
4 2
5 2
6 2
1000 1000
1000 1
*/
