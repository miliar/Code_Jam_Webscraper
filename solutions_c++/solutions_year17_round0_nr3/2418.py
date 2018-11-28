#include <bits/stdc++.h>
#define ll long long
#define rep(i,to) for(int i=0;i<(to);i++)
#define rep1(i,to) for(int i=1;i<=(to);i++)
#define ms(x, v) memset(x, v, sizeof(x))
using namespace std;
const int N = 105;
ll dfs(ll n, ll k)
{
	if (k == 0 || k == 1) return n - 1;
	--k;
	if (n & 1)
	{
		if (k & 1) return dfs(n / 2, k - k / 2);
		else return dfs(n / 2, k - k / 2);
	} else
	{
		if (k & 1) return dfs(n / 2, k - k / 2);
		else return dfs( (n - 1 ) / 2, k - k / 2);
	}
}
int main()
{
#ifdef LOCAL
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	ios::sync_with_stdio(0);
	int T, cas = 0;
	cin >> T;
	while (T--)
	{
		ll n, k;
		cin >> n >> k;
		ll ans = dfs(n, k);
		printf("Case #%d: ", ++cas);
		printf("%lld %lld\n", ans - ans / 2, ans / 2);
	}
	return 0;
}