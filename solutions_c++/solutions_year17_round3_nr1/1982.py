#include <bits/stdc++.h>
#define ll long long
#define rep(i,to) for(int i=0;i<(to);i++)
#define rep1(i,to) for(int i=1;i<=(to);i++)
#define ms(x, v) memset(x, v, sizeof(x))
using namespace std;
const int N = 1005;
const double PI = acos(-1.0);
ll n, k, id[N];
ll r[N], h[N];
bool cmp(const int &i, const int &j)
{
	return r[i] * h[i] > r[j] * h[j];
}
bool vis[N];
int main()
{
#ifdef LOCAL
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	ios::sync_with_stdio(0), cin.tie(0);
	cout << setiosflags(ios::fixed) << setprecision(10);
	int T, cas = 0;
	cin >> T;
	while (T--)
	{
		ms(vis, 0);
		cin >> n >> k;
		rep1(i, n) cin >> r[i] >> h[i];
		rep1(i, n) id[i] = i;
		sort(id + 1, id + n + 1, cmp);
		ll sum = 0, ans = 0, mx = 0;
		rep1(i, k - 1) sum += 2 * r[id[i]] * h[id[i]], vis[id[i]] = 1, mx = max(mx, r[id[i]]);
		rep1(i, n)
		{
			if (!vis[i])
			{
				ll x = max(mx, r[i]);
				ans = max(ans, sum + x * x + 2 * r[i] * h[i]);
			}
		}
		cout << "Case #" << ++cas << ": " << PI * ans << endl;
	}
	return 0;
}