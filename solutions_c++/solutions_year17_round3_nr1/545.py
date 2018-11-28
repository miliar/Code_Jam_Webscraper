#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<algorithm>
#include<cstdlib>
using namespace std;

typedef long long LL;
typedef double DB;

const DB PI = 3.1415926535898;
const int MAXN = 1005;

struct cake
{
	LL r;
	LL h;
}a[MAXN];

int T;
int K;
int N;
int kase;

DB f[MAXN][MAXN];

LL ans;
LL tans = 0;

inline LL Max(LL a, LL b)
{
	return a > b ? a : b;
}

inline DB Max(DB a, DB b)
{
	return a > b ? a : b;
}


inline bool cmp(const cake& a, const cake& b)
{
	return 2 * a.r * a.h > 2 * b.r * b.h;
}


inline void case_init()
{
	ans = 0;
	printf("Case #%d: ", ++kase);
	scanf("%d%d", &N,&K);
	for (int i = 1; i <= N; ++i)
		scanf("%lld%lld", &a[i].r, &a[i].h);
	sort(a + 1, a + 1 + N, cmp);
}

inline void case_proc(int k)
{

	int tk = K - 1;;
	for (int i = 1; i <= N; ++i)
	{
		if (tk <= 0) break;
		if (i == k) continue;
		if (a[i].r > a[k].r) continue;
		tans += 2 * a[i].r * a[i].h;
		--tk;
	}
	if (tk == 0) ans = Max(ans, tans);
}

inline void case_solve()
{
	for (int i = 1; i <= N; ++i)
	{
		tans = a[i].r * a[i].r;
		tans += 2 * a[i].r * a[i].h;
		case_proc(i);
	}
	printf("%.8f\n", (DB)ans*PI);
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