#include <bits/stdc++.h>
using namespace std;

const int N = 101;
int f[2][N][N][N][4];
int ans;

int a[4];
int n, k;
int nc;

void mxm(int &x, int y) { x = max(x, y); }

void solve() {
	cin >> n >> k;
	ans = 0;
	memset(a, 0, sizeof a);
	for (int i = 1; i <= n; ++i) { int x; cin >> x; a[x % k]++; }

	for(int i = 0; i <= 1; ++i) for (int j0 = 0; j0 <= a[0]; ++j0) for (int j1 = 0; j1 <= a[1]; ++j1) for (int j2 = 0; j2 <= a[2]; ++j2) for (int md = 0; md < k; ++md) f[i][j0][j1][j2][md] = -1e9;
	f[0][0][0][0][0] = 0;
	for (int i = 1; i <= n; ++i) {
		for (int j0 = 0; j0 <= a[0]; ++j0) for (int j1 = 0; j1 <= a[1]; ++j1) for (int j2 = 0; j2 <= a[2]; ++j2) for (int md = 0; md < k; ++md) if (j0 + j1 + j2 <= i - 1) {
			if (f[0][j0][j1][j2][md] == -1e9) continue;
			int j3 = i - 1 - j0 - j1 - j2;
			int add = (md == 0);
			if (j0 + 1 <= a[0]) {
				mxm(f[1][j0+1][j1][j2][md], f[0][j0][j1][j2][md] + add);
			}
			if (j1 + 1 <= a[1]) {
				mxm(f[1][j0][j1+1][j2][(md+1) % k], f[0][j0][j1][j2][md] + add);
			}
			if (j2 + 1 <= a[2]) {
				mxm(f[1][j0][j1][j2+1][(md+2) % k], f[0][j0][j1][j2][md] + add);
			}
			if (j3 + 1 <= a[3]) {
				mxm(f[1][j0][j1][j2][(md+3) % k], f[0][j0][j1][j2][md] + add);
			}
			//cerr << i << ' ' << j0 << ' ' << j1 << ' ' << j2 << ' ' << md << ' ' << f[0][j0][j1][j2][md] << endl;
		}

		for (int j0 = 0; j0 <= a[0]; ++j0) for (int j1 = 0; j1 <= a[1]; ++j1) for (int j2 = 0; j2 <= a[2]; ++j2) for (int md = 0; md < k; ++md) ans = max(ans, f[1][j0][j1][j2][md]), f[0][j0][j1][j2][md] = f[1][j0][j1][j2][md], f[1][j0][j1][j2][md] = -1e9;
	}

	printf("Case #%d: %d\n", ++nc, ans);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	ios_base::sync_with_stdio(false); cin.tie(0);
	int t; cin >> t;
	while(t--) solve();
}