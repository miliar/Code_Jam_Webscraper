#include<iostream>
#include<cstdio>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cstring>
#include<string>
#include<vector>
#include<iomanip>
//#include<unordered_set>
//#include<unordered_map>
#include<cmath>
#include<list>
#include<bitset>
using namespace std;
#define _____ ios::sync_with_stdio(false); cin.tie(0);
#define ull unsigned long long
#define ll long long
#define lson l,mid,id<<1
#define rson mid+1,r,id<<1|1

typedef pair<int, int>pii;
typedef pair<ll, ll>pll;
typedef pair<double, double>pdd;
const double eps = 1e-6;
const int MAXN = 10005;
const int MAXM = 5005;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const int INF = 0x3f3f3f3f;
const double FINF = 10000000;
const ll MOD = 123456789;
const double PI = acos(-1);

struct lx {
	ll r, h;
}tmp[1005];
int cmp(lx a, lx b) {
	return a.r > b.r;
}
double dp[1005][1005];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, n, k, cas = 0;
	scanf("%d", &t);
	while (t--)
	{
		memset(dp, 0, sizeof(dp));
		scanf("%d%d", &n, &k);
		for (int i = 1; i <= n; ++i)scanf("%lld%lld", &tmp[i].r, &tmp[i].h);
		sort(tmp + 1, tmp + n + 1, cmp);
		dp[1][1] = tmp[1].r*tmp[1].r*PI + tmp[1].r * 2 * PI*tmp[1].h;
		for (int i = 2; i <= n; ++i)
		{
			for (int j = 1; j <= k; ++j)
			{
				if (j == 1)dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + tmp[i].r * 2 * PI*tmp[i].h + tmp[i].r*tmp[i].r*PI);
				else dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + tmp[i].r * 2 * PI*tmp[i].h);
			}
		}
		printf("Case #%d: %.10lf\n",++cas, dp[n][k]);
	}
}