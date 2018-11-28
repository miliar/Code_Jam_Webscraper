#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

#define SZ(a) (int)(a).size()
typedef long long ll;

const double eps = 1e-10;
const int oo = (int)1e9;
int itc;

void solve() {
	int n, m;
	cin >> n >> m;
	vector<int> a(n);
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	vector<vector<pair<int, int>>> b(n, vector<pair<int, int>>(m));
	for (int i = 0; i < n; i++) {
		auto& c = b[i];
		for (int j = 0; j < m; j++) {
			double x;
			cin >> x;
			int mn = ceil(x/1.1/a[i]-eps);
			int mx = floor(x/0.9/a[i]+eps);
			c[j] = {mn, mx};
		}
		sort(begin(c), end(c));
	}
	int ans = 0;
	vector<int> c(n, 0);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (b[i][j].second == 0) {
				c[i]++;
			}
		}
	}
	bool flg = false;
	for (; ; ) {
		for (int i = 0; i < n; i++) {
			// printf("%d ", c[i]);
			if (c[i] >= m) {
				flg = true;
				break;
			}
		}
		if (flg) {
			break;
		}
		int mn = 0;
		int mx = oo;
		for (int i = 0; i < n; i++) {
			mn = max(mn, b[i][c[i]].first);
			mx = min(mx, b[i][c[i]].second);
			// auto tmp = b[i][c[i]];
			// printf("%d mn = %d, mx = %d\n", i, tmp.first, tmp.second);
		}
		// printf("g mn = %d, mx = %d\n", mn, mx);
		if (mn > mx) {
			for (int i = 0; i < n; i++) {
				if (b[i][c[i]].second == mx) {
					c[i]++;
				}
			}
		}
		else {
			ans++;
			for (int i = 0; i < n; i++) {
				c[i]++;
			}
		}
	}
	printf("%d\n", ans);
}

int main() {
	cin.sync_with_stdio(false);
	int ntc;
	cin >> ntc;
	for (itc = 1; itc <= ntc; itc++) {
		printf("Case #%d: ", itc);
		solve();
	}
}
