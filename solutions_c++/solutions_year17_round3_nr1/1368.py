#include <bits/stdc++.h>

using namespace std;

const int maxn = 2000;

struct cylinder {
	int r, h;
};

bool cmp(cylinder a, cylinder b) {
	return a.r > b.r;
}

cylinder a[maxn];
long double d[maxn][maxn];

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(0);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	cin >> t;
	for (int z = 0; z < t; ++z) {
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; ++i) {
			cin >> a[i].r >> a[i].h;
		}
		sort(a, a + n, cmp);
		d[0][0] = M_PI * a[0].r * a[0].r + 2 * M_PI * a[0].r * a[0].h;
		for (int i = 1; i < n; i++) {
			d[i][0] = max(d[i - 1][0], (long double)M_PI * a[i].r * a[i].r + 2 * M_PI * a[i].r * a[i].h);
			for (int j = 1; j < min(k, i + 1); ++j) {
				d[i][j] = max(d[i - 1][j], d[i - 1][j - 1] + 2 * M_PI * a[i].r * a[i].h);
			}
		}
		cout.precision(20);
		cout << "Case #" << z + 1 << ": " << d[n - 1][k - 1] << "\n";
	}

	return 0;

}
