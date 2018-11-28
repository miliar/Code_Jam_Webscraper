#include<bits/stdc++.h>
using namespace std;


int main() {
	int T, n, q;
	long D[128][128], E[128], S[128];
	const long inf = 1e16;
	cin >> T;
	cout.precision(16);
	double d[128][128];
	for(int _ = 1; _ <= T; ++_) {
		cin >> n >> q;
		for(int i = 1; i <= n; ++i)
			cin >> E[i] >> S[i];
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= n; ++j) {
				cin >> D[i][j];
				if(D[i][j] < 0)
					D[i][j] = inf;
			}

		for(int k = 1; k <= n; ++k)
			for(int i = 1; i <= n; ++i)
				for(int j = 1; j <= n; ++j)
					D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= n; ++j)
				d[i][j] = D[i][j] <= E[i] ? double(D[i][j]) / S[i] : 1e18;
		for(int k = 1; k <= n; ++k)
			for(int i = 1; i <= n; ++i)
				for(int j = 1; j <= n; ++j)
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
		cout << "Case #" << _ << ":";
		for(int u, v; q--; ) {
			cin >> u >> v;
			cout << " " << d[u][v];
		}
		cout << endl;
	}
}
