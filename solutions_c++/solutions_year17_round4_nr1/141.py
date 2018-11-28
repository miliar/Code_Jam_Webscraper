#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define mp(a, b) make_pair(a, b)
#define fi first
#define se second
#define re return
#define forn(i, n) for (int i = 1; i <= n; i++)
int cnt[5];
int dp[107][107][107][4];
const int INF = 1000 * 1000 * 1000 + 7;
void solve(int tt)
{
	int n, m;
	scanf("%d %d", &n, &m);
	memset(cnt, 0, sizeof(cnt));
	for (int i = 1; i <= n; i++)
	{
		int x;
		scanf("%d", &x);
		cnt[x % m]++;
	}
	for (int i = 0; i <= n; i++)
	{
		for (int j = 0; j <= n; j++)
		{
			for (int k = 0; k <= n; k++)
			{
				for (int p = 0; p < 4; p++)
				{
					dp[i][j][k][p] = 0;
				}
			}
		}
	}
	dp[0][0][0][0] = 0;
	for (int i = 0; i <= n; i++)
	{
		for (int j = 0; j <= n; j++)
		{
			for (int k = 0; k <= n; k++)
			{
				for (int p = 0; p <= 3; p++)
				{
					int cost = 0;
					if (p == 0) cost = 1;
					dp[i + 1][j][k][(p - 1 + m) % m] = max(dp[i + 1][j][k][(p - 1 + m) % m], dp[i][j][k][p] + cost);					
					dp[i][j + 1][k][(p - 2 + m) % m] = max(dp[i][j + 1][k][(p - 2 + m) % m], dp[i][j][k][p] + cost);
					dp[i][j][k + 1][(p - 3 + m + m) % m] = max(dp[i][j][k + 1][(p - 3 + m + m) % m], dp[i][j][k][p] + cost);
				}
			}
		}
	}
	int res = 0;
	for (int i = 0; i < 4; i++) res = max(res, dp[cnt[1]][cnt[2]][cnt[3]][i]);
	res += cnt[0];
	printf("Case #%d: %d\n", tt, res);
}
int main()
{
#ifdef LOCAL
//	freopen("input.txt", "r", stdin);
#endif
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		double t1 = 1.0 * clock() / CLOCKS_PER_SEC;
		solve(tt);
		double t2 = 1.0 * clock() / CLOCKS_PER_SEC;
		cerr << tt << endl;
//		printf("Solved case %d, time = %.10lf, total time = %.10lf\n", tt, t2 - t1, t2);
	}
	return 0;
}

