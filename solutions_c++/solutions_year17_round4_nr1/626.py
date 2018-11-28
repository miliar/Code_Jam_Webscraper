#include <cstdio>
#include <cstring>

const int MAXN = 110;
const int P = 4;

int n, p;
int a[MAXN];
int dp[MAXN][MAXN][MAXN][4];

int max(int a, int b){ return a > b ? a : b;}


int get(int g1, int g2, int g3, int r)
{
	if (g1 + g2 + g3 == 0) return 0;
	if (dp[g1][g2][g3][r] < 0)
	{
		if (r == 0) dp[g1][g2][g3][r] = 1;
		else dp[g1][g2][g3][r] = 0;
		int tmp = 0;
		if (g1 > 0) tmp = max(get(g1 - 1, g2, g3, (r + 1) % P), tmp);
		if (g2 > 0) tmp = max(get(g1, g2 - 1, g3, (r + 2) % P), tmp);
		if (g3 > 0) tmp = max(get(g1, g2, g3 - 1, (r + 3) % P), tmp);
		//printf("%d %d %d: %d\n", g1, g2, g3, tmp);
		dp[g1][g2][g3][r] += tmp;
	}
	return dp[g1][g2][g3][r];
}


void init()
{
	scanf("%d %d", &n, &p);
	memset(a, 0, sizeof(a));
	for (int i = 0; i < n; ++i)
	{
		int t;
		scanf("%d", &t);
		++a[t % p];
	}
}

void solve()
{
	if (p == 2)
	{
		printf("%d\n", a[0] + (a[1] + 1) / 2);
	}
	else if (p == 3)
	{
		int t;
		if (a[1] < a[2]) t = a[1];
		else t = a[2];
		a[1] -= t;
		a[2] -= t;
		printf("%d\n", a[0] + t + (a[1] + a[2] + 2) / 3);
	}
	else if (p == 4)
	{
		printf("%d\n", a[0] + get(a[1], a[2], a[3], 0));
	}
}


int main()
{
	//freopen("a.in", "r", stdin);
	memset(dp, 0xff, sizeof(dp));
	int tt;
	scanf("%d", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		init();
		printf("Case #%d: ", ii);
		solve();
	}
	return 0;
}