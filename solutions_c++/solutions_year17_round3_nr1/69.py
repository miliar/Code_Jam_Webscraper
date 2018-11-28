#include <bits/stdc++.h>

#define ll long long
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define ld double

using namespace std;

const int nm = 1010;
const ld pi = acos(-1.0);

int n, m;
ll r[nm], h[nm];
ll g[nm][nm];

void solve(int test) {
	cout << "Case #" << test << ": ";
	cin >> n >> m;
	for (int i = 1; i <= n; ++i) {
		cin >> r[i] >> h[i];
	}
	for (int i = 1; i < n; ++i) {
		for (int j = i + 1; j <= n; ++j) {
			if (r[j] < r[i]) {
				swap(r[i], r[j]);
				swap(h[i], h[j]);
			}
		}
	}
	for (int i = 0; i <= n; ++i)
		g[i][0] = 0;
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= i && j <= m; ++j) {
			g[i][j] = max(g[i - 1][j], g[i - 1][j - 1] + 2ll * r[i] * h[i]);
		}
	}
	ll res = 0;
	for (int i = m; i <= n; ++i) {
		res = max(res, g[i - 1][m - 1] + 2ll * r[i] * h[i] + r[i] * r[i]);
	}
//	cout << res << "\n";
	cout << setprecision(9) << fixed << pi * res << "\n";
}

int main() {
#ifdef LOCAL
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		solve(i);
}
