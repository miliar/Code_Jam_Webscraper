#include <bits/stdc++.h>
using ll = long long;
using ld = long double;
using namespace std;


const int MAXN = 1001;
int a[MAXN];	
int b[MAXN];
int n, m, c;

void Solve() {
	memset(a, 0, sizeof(a));
	memset(b, 0, sizeof(b));
	cin >> n >> c >> m;
	for (int i = 0; i < m; i++) {
		int x, y;
		cin >> x >> y;
		a[x]++;
		b[y]++;
	}
	int ans = 0, sum = 0;
	for (int i = 1; i <= n; i++) {
		sum += a[i];
		ans = max(ans, (sum - 1) / i + 1);
	}
	for (int i = 1; i <= c; i++) {
		ans = max(ans, b[i]);
	}

	int ans2 = 0;

	for (int i = n; i >= 1; i--) {
		ans2 += max(0, a[i] - ans);
	}

	cout << ans << " " << ans2 << "\n";
}

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(false); cout.setf(ios::fixed); cout.precision(20);
	int tests;
	cin >> tests;
	for (int i = 1; i <= tests; i++) {
		cout << "Case #" << i << ": ";
		Solve();
	}
	return 0;
}