// IOI 2018
#include <bits/stdc++.h>
using namespace std;

const int MAX = 110;

int a[MAX][MAX];
long long d[MAX][MAX];
long double f[MAX][MAX];
int N, Q, E[MAX], S[MAX];
int nc;

void solve() {
	cin >> N >> Q;
	for (int i = 1; i <= N; ++i) cin >> E[i] >> S[i];
	for (int i = 1; i <= N; ++i) for (int j = 1; j <= N; ++j) cin >> a[i][j];
	
	for (int i = 1; i <= N; ++i) for (int j = 1; j <= N; ++j) if (i == j) f[i][j] = 0, d[i][j] = 0; else f[i][j] = 1e18, d[i][j] = 1e18;
	for (int i = 1; i <= N; ++i) for (int j = 1; j <= N; ++j) if (a[i][j] != -1) d[i][j] = a[i][j];
	for (int k = 1; k <= N; ++k) for (int i = 1; i <= N; ++i) for (int j = 1; j <= N; ++j) d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

	for (int i = 1; i <= N; ++i) for (int j = 1; j <= N; ++j) if (E[i] >= d[i][j]) f[i][j] = (double)d[i][j] / S[i];

	for (int k = 1; k <= N; ++k) for (int i = 1; i <= N; ++i) for (int j = 1; j <= N; ++j) {
		//if (E[i] >= d[i][k]) {
			f[i][j] = min(f[i][j], f[i][k] + f[k][j]);
		//}
	}
	//for (int i = 1; i <= N; ++i) for (int j = i+1; j <= N; ++j) cerr << i << ' ' << j << ' ' << f[i][j] << endl;

	cout << "Case #" << ++nc << ": ";

	while(Q--) {
		int u, v; cin >> u >> v;
		cout << setprecision(6) << fixed << f[u][v] << ' ';
	}
	cout << endl;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);
	ios_base::sync_with_stdio(false); cin.tie(0);
	int T; cin >> T;
	while(T--) solve();
}