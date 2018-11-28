#include <bits/stdc++.h>

using namespace std;

int n, p;
int r[55];
int q[55][55];
int pos[55];
bool used[55][55];

int bs(int i, int mx) {
	int lo = 0, hi = p - 1, ans = -1;
	while (lo <= hi) {
		int mid = (lo + hi) >> 1;
		if (q[i][mid] <= mx) {
			ans = mid;
			lo = mid + 1;
		} else {
			hi = mid - 1;
		}
	}
	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc) {
		scanf("%d %d", &n, &p);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &r[i]);
		}
		int mx = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < p; ++j) {
				scanf("%d", &q[i][j]);
				used[i][j] = 0;
			}
			sort(q[i], q[i] + p);
			mx = max(mx, 2 * q[i][p - 1] / r[i]);
		}
		int ans = 0;
		for (int x = mx; x; --x) {
			bool can = true;
			while (can) {
				for (int i = 0; can && i < n; ++i) {
					int lo = 9 * x * r[i] / 10, hi = 11 * x * r[i] / 10;
					int k = bs(i, hi);
					can = false;
					for (int j = k; !can && j >= 0; --j) {
						if (!used[i][j] && lo <= q[i][j] && q[i][j] <= hi) {
							pos[i] = j;
							can = true;
						}
					}
				}
				if (can) {
					++ans;
					for (int i = 0; i < n; ++i) {
						used[i][pos[i]] = 1;
					}
				}
			}
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}