#define _CRT_SECURE_NO_WARNINGS

#include<algorithm>
#include<cstdlib>
#include<cstdio>

using namespace std;

const int MAXN = 100;
typedef double DB;
int T;
int N;
int K;
int kase;
DB P[MAXN];
DB U;
DB ans;
const DB EPS = 1e-10;

inline int DBcmp(DB a, DB b)
{
	if (a - b > EPS) return 1;
	if (b - a > EPS) return -1;
	return 0;
}
inline void case_init()
{
	printf("Case #%d: ", ++kase);
	scanf("%d%d%lf", &N, &K, &U);
	for (int i = 1; i <= N; ++i) scanf("%lf", &P[i]);
	P[N + 1] = 100000;
	ans = 1;
}
inline void case_solve()
{
	sort(P + 1, P + N + 1);
	for (int i = 1; i <= N; ++i)
	{
		if (DBcmp(P[i], P[i + 1]) == 0) continue;
		if (DBcmp(U, (P[i + 1] - P[i])*(DB)i) >= 0)
		{
			U -= (P[i + 1] - P[i])*(DB)i;
			for (int j = 1; j <= i; ++j) P[j] = P[i + 1];
		}
		else
		{
			U /= i;
			for (int j = 1; j <= i; ++j) P[j] += U;
			break;
		}
	}
	for (int i = 1; i <= N; ++i) ans *= P[i];
	if (DBcmp(ans, 1) > 0) ans = 1;
	printf("%.6f\n", ans);
}
int main()
{
	freopen("C.in", "r", stdin);
	freopen("c.out", "w", stdout);
	for (scanf("%d", &T); T; --T)
	{
		case_init();
		case_solve();
	}
	return 0;
}