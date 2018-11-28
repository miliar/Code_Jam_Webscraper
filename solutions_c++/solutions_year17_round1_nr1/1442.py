#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<ctype.h>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<bitset>
#include<algorithm>
#include<time.h>
using namespace std;
#define MS(x, y) memset(x, y, sizeof(x))
#define ls o<<1
#define rs o<<1|1
typedef long long LL;
typedef unsigned long long UL;
typedef unsigned int UI;
template <class T1, class T2>inline void gmax(T1 &a, T2 b) { if (b > a)a = b; }
template <class T1, class T2>inline void gmin(T1 &a, T2 b) { if (b < a)a = b; }
const int N = 30, M = 0, Z = 1e9 + 7, inf = 0x3f3f3f3f;
template <class T1, class T2>inline void gadd(T1 &a, T2 b) { a = (a + b) % Z; }
int casenum, casei; 
void fre() 
{ 
	freopen("D://english program//My programs//Project1//Project1//input.in", "r", stdin); 
	freopen("D://english program//My programs//Project1//Project1//output.out", "w", stdout); 
}
int n, m;
char s[N][N];
int line[N][N];
int sum[N][N];
int val(int y1, int x1, int y2, int x2)
{
	return sum[y2][x2] + sum[y1 - 1][x1 - 1] - sum[y1 - 1][x2] - sum[y2][x1 - 1];
}
void print(int y1, int x1, int y2, int x2)
{
	char ch = 0;
	for (int i = y1; i <= y2; ++i)
	{
		for (int j = x1; j <= x2; ++j) if (s[i][j] != '?')
		{
			if (ch) { puts("Error"); while (1); }
			ch = s[i][j];
		}
	}
	for (int i = y1; i <= y2; ++i)
	{
		for (int j = x1; j <= x2; ++j)s[i][j] = ch;
	}
}
int main()
{
	fre();
	scanf("%d", &casenum);
	for (casei = 1; casei <= casenum; ++casei)
	{
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; ++i)
		{
			scanf("%s", s[i] + 1);
		}
		for (int i = 1; i <= n; ++i)
		{
			for (int j = 1; j <= m; ++j)
			{
				line[i][j] = line[i][j - 1] + (s[i][j] != '?');
				sum[i][j] = sum[i - 1][j] + line[i][j];
			}
		}
		int r = 1;
		for (int l = 1; l <= m; )
		{
			while (val(1, l, n, r) == 0 || r < m && val(1, l, n, r + 1) == val(1, l, n, r))++r;
			
			int j = 1;
			for (int i = 1; i <= n; )
			{
				while (val(i, l, j, r) == 0 || j < n && val(i, l, j + 1, r) == val(i, l, j, r))++j;
				print(i, l, j, r);
				i = ++j;
			}
			l = ++r;
		}
		printf("Case #%d:\n", casei);
		for (int i = 1; i <= n; ++i)puts(s[i] + 1);
	}
	return 0;
}
/*
【trick&&吐槽】


【题意】


【分析】


【时间复杂度&&优化】


*/