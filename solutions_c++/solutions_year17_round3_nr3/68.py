#include <bits/stdc++.h>

#define ll long long
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define ld double

using namespace std;

const int nm = 60;

int n, m;
ld s, a[nm];

void solve(int test) {
	cout << "Case #" << test << ": ";
	cin >> n >> m >> s;
	for (int i = 1; i <= n; ++i) {
		cin >> a[i];
	}
	sort(a + 1, a + n + 1);
	a[n + 1] = 1.0;
	for (int i = 1; i <= n; ++i) {
		ld tmp = min(s / i, min(a[i + 1] - a[i], 1.0 - a[i]));
		for (int j = 1; j <= i; ++j)
			a[j] += tmp;
		s -= tmp * i;
	}
	ld res = 1.0;
	for (int i = 1; i <= n; ++i)
		res *= a[i];
	cout << setprecision(6) << fixed << res << "\n";
}

int main() {
#ifdef LOCAL
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
//	freopen("input.txt", "r", stdin);
#endif
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		solve(i);
}
