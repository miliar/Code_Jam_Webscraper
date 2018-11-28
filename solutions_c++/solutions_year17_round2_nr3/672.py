#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;
#define int long long

const long double INF = 1e18;

void sol() {
	int n, q;
	cin >> n >> q;
	vector <vector <int> > G(n, vector <int> (n));
	vector <long double> E(n), S(n);
	for (int i = 0; i < n; i++) {
		cin >> E[i] >> S[i];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			int tmp;
			cin >> tmp;
			if (tmp == -1) {
				G[i][j] = INF;
			} else {
				G[i][j] = tmp;
			}
		}
	}
	for (int k = 0; k < n; k++) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				G[i][j] = min(G[i][j], G[i][k] + G[k][j]);
			}
		}
	}
	cout << fixed << setprecision(10);
	for (int _q = 0; _q < q; _q++) {
		int V, U;
		cin >> V >> U;
		V--; U--;
		vector <long double> dist(n, INF);
		vector <bool> ans_calc(n, false);
		dist[V] = 0;
		for (int i = 0; i < n; i++) {
			bool flag = false;
			int id;
			for (int j = 0; j < n; j++) {
				if (!ans_calc[j]) {
					if (!flag) {
						flag = true;
						id = j;
					} else {
						if (dist[id] > dist[j]) {
							id = j;
						}
					}
				}
			}
			ans_calc[id] = true;
			for (int j = 0; j < n; j++) {
				if (G[id][j] <= E[id]) {
					dist[j] = min(dist[j], dist[id] + G[id][j] / S[id]);
				}
			}
		}
		cout << dist[U] << " ";
	}
	cout << endl;
}

// void sol1() {
// 	int n, q;
// 	cin >> n >> q;
// 	vector <vector <int> > G(n, vector <int> (n));
// 	vector <long double> E(n), S(n);
// 	for (int i = 0; i < n; i++) {
// 		cin >> E[i] >> S[i];
// 	}
// 	for (int i = 0; i < n; i++) {
// 		for (int j = 0; j < n; j++) {
// 			int tmp;
// 			cin >> tmp;
// 			if (tmp == -1) {
// 				G[i][j] = INF;
// 			} else {
// 				G[i][j] = tmp;
// 			}
// 		}
// 	}
// 	int v, u;
// 	cin >> v >> u;
// 	cout << fixed << setprecision(10);

// 	vector <long double> dp(n, INF);
// 	dp[n - 1] = 0;
// 	for (int i = n - 2; i >= 0; i--) {
// 		for (int j = i + 1; j < n; j++) {
// 			long double leng = 0;
// 			for (int t = i; t < j; t++) {
// 				leng += G[t][t + 1];
// 			}
// 			if (leng <= E[i]) {
// 				dp[i] = min(dp[i], dp[j] + leng / S[i]);
// 			}
// 		}
// 	}
// 	cout << dp[0] << " \n";
// }


signed main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		sol();
	}

	fclose(stdin);
	fclose(stdout);
}