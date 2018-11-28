#include <bits/stdc++.h>

#define ff first
#define ss second
#define pii pair < int, int >
#define puba push_back

using namespace std;

typedef long long LL;

const int MAXN = 110;

const LL INF = (LL) 1e18;
LL mat[MAXN][MAXN], e[MAXN];
double s[MAXN];
double g[MAXN][MAXN];


int main() {
	int t;
	cin >> t;
	for (int q = 1; q <= t; ++q) {
		cout << "Case #" << q << ": ";

		int n, m;
		cin >> n >> m;

		for (int i = 0; i < n; ++i) {
			cin >> e[i] >> s[i];
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				cin >> mat[i][j];
				if (mat[i][j] == -1) mat[i][j] = INF;
			}
		}

		for (int k = 0; k < n; ++k) {
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < n; ++j) {
					mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j]);
				}
			}
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				g[i][j] = INF;
				if (mat[i][j] <= e[i]) {
					g[i][j] = (double) mat[i][j] / s[i];
				}
			}
		}

		for (int k = 0; k < n; ++k) {
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < n; ++j) {
					g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
				}
			}
		}

		for (int i = 0; i < m; ++i) {
			int u, v;
			cin >> u >> v;
			--u, --v;

			printf("%.13lf ", g[u][v]);
		}
		cout << endl;
	}
	return 0;
}