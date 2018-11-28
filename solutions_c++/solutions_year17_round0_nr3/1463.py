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
void fre() { freopen("c://test//input.in", "r", stdin); freopen("c://test//output.out", "w", stdout); }
#define MS(x, y) memset(x, y, sizeof(x))
#define ls o<<1
#define rs o<<1|1
typedef long long LL;
typedef unsigned long long UL;
typedef unsigned int UI;
template <class T1, class T2>inline void gmax(T1 &a, T2 b) { if (b > a)a = b; }
template <class T1, class T2>inline void gmin(T1 &a, T2 b) { if (b < a)a = b; }
const int N = 0, M = 0, Z = 1e9 + 7, inf = 0x3f3f3f3f;
template <class T1, class T2>inline void gadd(T1 &a, T2 b) { a = (a + b) % Z; }
int casenum, casei;
map<LL, LL>mop;
LL n, m;
int main()
{
	fre();
	scanf("%d", &casenum);
	for (casei = 1; casei <= casenum; ++casei)
	{
		scanf("%lld%lld", &n, &m);
		mop.clear(); mop[n] = 1;
		while (1)
		{
			LL len = (--mop.end())->first;
			LL num = (--mop.end())->second;
			mop.erase(--mop.end());
			LL big = len / 2;
			LL sml = (len - 1) / 2;
			if (num >= m)
			{
				printf("Case #%d: %lld %lld\n", casei, big, sml);
				break;
			}
			m -= num;
			mop[big] += num;
			mop[sml] += num;
		}
	}
	return 0;
}
/*
【trick&&吐槽】


【题意】


【分析】


【时间复杂度&&优化】


*/