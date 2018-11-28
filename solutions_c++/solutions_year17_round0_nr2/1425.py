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
const int N = 1010, M = 0, Z = 1e9 + 7, inf = 0x3f3f3f3f;
template <class T1, class T2>inline void gadd(T1 &a, T2 b) { a = (a + b) % Z; }
int casenum, casei;
char s[N], t[N];
int main()
{
	fre();
	scanf("%d", &casenum);
	for (casei = 1; casei <= casenum; ++casei)
	{
		scanf("%s", s + 1);
		int n = strlen(s + 1); s[0] = 0;
		LL ans = 0;
		for (int i = 1; i <= n; ++i)
		{
			if (s[i] < s[i - 1])break;
			if (s[i] > s[i - 1])
			{
				strcpy(t + 1, s + 1);
				--t[i]; for (int j = i + 1; j <= n; ++j)t[j] = '9';
				LL x; sscanf(t + 1, "%lld", &x); gmax(ans, x);
			}
			if (i == n)
			{
				LL x; sscanf(s + 1, "%lld", &x); gmax(ans, x);
			}
		}
		printf("Case #%d: %lld\n", casei, ans);
	}
	return 0;
}
/*
【trick&&吐槽】


【题意】


【分析】


【时间复杂度&&优化】


*/