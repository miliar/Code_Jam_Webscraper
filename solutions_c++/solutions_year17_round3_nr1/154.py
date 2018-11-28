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
const int N = 1010, M = 0, Z = 1e9 + 7, inf = 0x3f3f3f3f;
const long double PI = acos(-1.0);
template <class T1, class T2>inline void gadd(T1 &a, T2 b) { a = (a + b) % Z; }
int casenum, casei; 
int n, K;
void fre() 
{ 
	freopen("input.in", "r", stdin); 
	freopen("output.out", "w", stdout); 
}
long double CE(long double R, long double H)
{
	return 2 * PI * R * H;
}
struct A
{
	int r, h;
	long double ce;
	bool operator < (const A & b)const
	{
		return ce > b.ce;
	}
}a[N];
long double sum[N];
long double solve()
{
	for (int i = 1; i <= n; ++i)
	{
		scanf("%d%d", &a[i].r, &a[i].h);
		a[i].ce = CE(a[i].r, a[i].h);
	}
	sort(a + 1, a + n + 1);
	for (int i = 1; i <= n; ++i)
	{
		sum[i] = sum[i - 1] + a[i].ce;
	}
	long double ans = 0;
	for (int i = 1; i <= n; ++i)
	{
		if (i <= K)
		{
			gmax(ans, PI * a[i].r * a[i].r + sum[K]);
		}
		else
		{
			gmax(ans, PI * a[i].r * a[i].r + sum[K - 1] + a[i].ce);
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
		scanf("%d%d", &n, &K);
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