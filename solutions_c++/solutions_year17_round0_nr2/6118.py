#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;
const ll inf = 1e18;

int cnt;
int a[20];
ll p10[20];

void init()
{
	p10[0] = 1;
	for (int i = 1; i <= 18; ++i)
		p10[i] = p10[i-1] * 10;
}

void factor(ll n)
{
	for (cnt = 0; n; n /= 10)
		a[++cnt] = n % 10;
	reverse(a + 1, a + cnt + 1);
}

ll dfs(int dep, bool lim, int mn)
{
	if (dep > cnt) return 0;
	if (!lim) return p10[cnt - dep + 1] - 1;
	ll ans = -inf;
	for (int i = mn; i <= a[dep]; ++i)
	{
		ll t = i * p10[cnt - dep];
		ans = max(ans, t + dfs(dep + 1, i == a[dep], i));
	}
	return ans;
}

ll solve(ll n)
{
	factor(n);
	return dfs(1, 1, 0);
}

int main()
{
	init();
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas)
	{
		ll n;
		scanf("%lld", &n);
		printf("Case #%d: %lld\n", cas, solve(n));
	}
	return 0;
}
