#include <bits/stdc++.h>

using namespace std;

int n, pm, T;
int r[60];
int p[60][60];
int c[60];
int ans;

void solve() {
	while (true) {
		int lo = 1, hi = 1<<30;
		bool good = true;
		for (int i = 0; i < n; i++) {
			if (c[i] >= pm) return;
			int clo = ((p[i][c[i]] * 10 + 10) / 11 + r[i]-1) / r[i];
			int chi = ((p[i][c[i]] * 10) / 9 / r[i]);
			if (clo > chi || chi < lo || clo > hi) {
				good = false;
				break;
			}
			lo = max(lo, clo);
			hi = min(hi, chi);
		}
		if (good) {
			ans++;
			for (int i = 0; i < n; i++) {
				c[i]++;
			}
		} else {
			int mhi = 1<<30;
			int mhid = -1;
			for (int i = 0; i < n; i++) {
				if (c[i] >= pm) return;
				int chi = ((p[i][c[i]] * 10) / 9 / r[i]);
				if (chi < mhi) {
					mhi = chi;
					mhid = i;
				}
			}
			c[mhid]++;
		}
	}
}

int main()
{
	cin >> T;
	for (int C = 1; C <= T; C++) {
		cin >> n >> pm;
		for (int i = 0; i < n; i++) cin >> r[i];
		for (int i = 0; i < n; i++)
			for (int j = 0; j < pm; j++)
				cin >> p[i][j];
		for (int i = 0; i < n; i++) sort(p[i], p[i] + pm);
		for (int i = 0; i < n; i++) c[i] = 0;
		ans = 0;
		solve();
		cout << "Case #" << C << ": " << ans << '\n';
	}
	return 0;
}
