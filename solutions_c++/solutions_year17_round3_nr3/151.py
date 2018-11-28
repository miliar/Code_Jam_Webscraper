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
const int N = 60, M = 0, Z = 1e9 + 7, inf = 0x3f3f3f3f;
template <class T1, class T2>inline void gadd(T1 &a, T2 b) { a = (a + b) % Z; }
int casenum, casei;
int n, K;
double U;
double p[N];
void fre()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
}
long double solve()
{
	long double l = 0;
	long double r = 1;
	for (int tim = 1; tim <= 200; ++tim)
	{
		long double mid = (l + r) / 2;
		long double sum = 0;
		for (int i = 1; i <= n; ++i)
		{
			if (p[i] < mid)sum += mid - p[i];
		}
		if (sum <= U)l = mid;
		else r = mid;
	}
	long double ans = 1;
	for (int i = 1; i <= n; ++i)
	{
		if (p[i] < l)ans *= l;
		else ans *= p[i];
	}
	return ans;
}
int main()
{
	fre();
	scanf("%d", &casenum);
	for (casei = 1; casei <= casenum; ++casei)
	{
		scanf("%d%d", &n, &K);
		scanf("%lf", &U);
		for (int i = 1; i <= n; ++i)scanf("%lf", &p[i]);
		sort(p + 1, p + n + 1);
		printf("Case #%d: %.10f\n", casei, (double)solve());
	}
	return 0;
}
/*
【trick&&吐槽】


【题意】


【分析】


【时间复杂度&&优化】

*/