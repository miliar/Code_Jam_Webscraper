#include <bits/stdc++.h>

using namespace std;

#define REP(i, a, b) for (int i = (a), i##_end_ = (b); i < i##_end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

typedef long long LL;

const int oo = 0x3f3f3f3f;

const int maxn = 110;

int n;

int e[maxn + 5], s[maxn + 5];

int dis[maxn + 5][maxn + 5];
double f[maxn + 5][maxn + 5];

int main()
{
#ifdef matthew99
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int case_cnt;
	scanf("%d", &case_cnt);
	for (int case_id = 1; case_id <= case_cnt; ++case_id)
	{
		printf("Case #%d: ", case_id);
		int qn;
		scanf("%d%d", &n, &qn);
		REP(i, 0, n) scanf("%d%d", e + i, s + i);
		REP(i, 0, n) REP(j, 0, n) 
		{
			scanf("%d", dis[i] + j);
			if (!~dis[i][j]) dis[i][j] = oo;
		}
		REP(k, 0, n) REP(i, 0, n) REP(j, 0, n) chkmin(dis[i][j], dis[i][k] + dis[k][j]);
		REP(i, 0, n) REP(j, 0, n) 
			if (dis[i][j] <= e[i]) f[i][j] = (double)dis[i][j] / s[i];
			else f[i][j] = 1e100;
		REP(k, 0, n) REP(i, 0, n) REP(j, 0, n) chkmin(f[i][j], f[i][k] + f[k][j]);
		REP(i, 0, qn)
		{
			int u, v;
			scanf("%d%d", &u, &v), --u, --v;
			printf("%.15f ", f[u][v]);
		}
		printf("\n");
	}
	return 0;
}
