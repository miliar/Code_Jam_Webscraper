#include <bits/stdc++.h>

#define ll long long
#define mp make_pair
#define fi first
#define se second

using namespace std;

int m, n;

void solve(int test) {
	cout << "Case #" << test << ": ";
	cin >> m >> n;
	priority_queue<pair<ll, ll> > q;
	q.push(mp(m, -1));
	for (int i = 1; i < n; ++i) {
		ll l = q.top().fi, vt = -q.top().se;
		q.pop();
		ll mid = vt + (l - 1) / 2;
		q.push(mp(mid - vt, -vt));
		q.push(mp(vt + l - (mid + 1), mid + 1));
	}
	ll l = q.top().fi, vt = -q.top().se;
	ll mid = vt + (l - 1) / 2;
	ll dl = mid - vt, dr = vt + l - (mid + 1);
	cout << max(dl, dr) << " " << min(dl, dr) << "\n";
}

int main()
{
#ifdef LOCAL
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		solve(i);
}









