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
const int N = 1440, M = 0, Z = 1e9 + 7, inf = 0x3f3f3f3f;
const long double PI = acos(-1.0);
template <class T1, class T2>inline void gadd(T1 &a, T2 b) { a = (a + b) % Z; }
int casenum, casei;
int n, K;
void fre()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
}
int g0, g1;
struct A
{
	int st;
	int who;
};
bool d0[N + 10], d1[N + 10];
int f[N + 10][N + 10][2][2];
int solve()
{
	MS(f, 63); f[0][0][0][0] = 1; f[0][0][1][1] = 1;
	for (int i = 0; i < N; ++i)
	{
		int top = min(i, 720);
		for (int j = top; j >= 0; --j)
		{
			for (int k = 0; k < 2; ++k)
			{
				for (int u = 0; u < 2; ++u)if (f[i][j][k][u] <= 1000)
				{
					if (d0[i])//可以照顾孩子
					{
						gmin(f[i + 1][j + 1][0][u], f[i][j][k][u] + (k != 0));
					}
					if (d1[i])//可以照顾孩子
					{
						gmin(f[i + 1][j][1][u], f[i][j][k][u] + (k != 1));
					}
				}
			}
		}
	}
	int ans = inf;
	for (int i = 0; i < 2; ++i)
	{
		for (int j = 0; j < 2; ++j)
		{
			gmin(ans, f[1440][720][i][j] - (i == j));
		}
	}
	return ans;
}
int main()
{
	fre();
	scanf("%d", &casenum);
	for (casei = 1; casei <= casenum; ++casei)
	{
		for (int i = 0; i < N; ++i)
		{
			d0[i] = d1[i] = 1;
		}
		scanf("%d%d", &g0, &g1);
		for (int i = 1; i <= g0; ++i)
		{
			int l, r; scanf("%d%d", &l, &r);
			//vt[r].push_back({ l, 0 });
			for (int j = l; j < r; ++j)d0[j] = 0;
		}
		for (int i = 1; i <= g1; ++i)
		{
			int l, r; scanf("%d%d", &l, &r);
			//vt[r].push_back({ l, 1 });
			for (int j = l; j < r; ++j)d1[j] = 0;
		}
		printf("Case #%d: %d\n", casei, solve());
	}
	return 0;
}
/*
【trick&&吐槽】


【题意】


【分析】
给出的是工作时间
如果一个人在一段时间都工作
那么，只能另外一个人做。

如果没有人在该段时间工作
那么，都可以做

【时间复杂度&&优化】
5
1 1
540 600
840 900

2 0
900 1260
180 540

1 1
1439 1440
0 1

2 2
0 1
1439 1440
1438 1439
1 2

3 4
0 10
1420 1440
90 100
550 600
900 950
100 150
1050 1400

*/