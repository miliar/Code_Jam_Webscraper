#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<cstring>
#include<iostream>

using namespace std;

const int MAXN = 50;

char a[MAXN][MAXN];
int n, m;
int T;
int kase = 0;

inline char get_ch()
{
	char t = getchar();
	while ((t<'A' || t>'Z') && t != '?') 
		t = getchar();
	return t;
}
inline void print()
{
	for (int i = 1; i <= n; ++i, putchar('\n'))
		for (int j = 1; j <= m; ++j)
			putchar(a[i][j]);
}
inline void case_init()
{
	printf("Case #%d:\n", ++kase);
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j)
			a[i][j] = get_ch();
//	print();
}
inline bool empty_row(int k)
{
	for (int i = 1; i <= m; ++i)
		if (a[k][i] != '?') return false;
	return true;
}
inline void row_copy(int i, int j)
{
	for (int k = 1; k <= m; ++k) a[j][k] = a[i][k];
}
inline void case_solve()
{
	int i, j, k;
	for (i = 1; i <= n; ++i)
	{
		if (empty_row(i)) continue;
		for (j = 1; j <= m; ++j)
		{
			if (a[i][j] != '?')
			{
				for (k = j + 1; k <= m&&a[i][k] == '?'; ++k) a[i][k] = a[i][j];
				//j = k;
			}
		}
		for (j = 1; j <= m; ++j)
			if (a[i][j] != '?') break;
		for (k = 1; k<j; ++k)
			a[i][k] = a[i][j];
	}
	for (i = 1; i <= n; ++i)
	{
		if (!empty_row(i))
		{
			for (j = i + 1; j <= n&&empty_row(j); ++j) row_copy(i, j);
		}
	}
	for (i = 1; i <= n; ++i) if (!empty_row(i)) break;
	for (k = 1; k<i; ++k) row_copy(i, k);
	for (int i = 1; i <= n; ++i, putchar('\n'))
		for (int j = 1; j <= m; ++j)
			putchar(a[i][j]);
	return;
}
int main()
{
	freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);
	for (scanf("%d", &T); T; --T)
	{
		case_init();
		case_solve();
	}
	return 0;
}
