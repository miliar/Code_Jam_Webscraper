#include <bits/stdc++.h>
using namespace std;

const double INF = 1e15;

int N;
int E[200];
double S[200];

int D[200][200];

double dist[200][200];

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		int Q;
		cin >> N >> Q;
		
		for (int i = 1; i <= N; i++) {
			cin >> E[i] >> S[i];
			S[i] = 1.0/S[i];
		}
		
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				cin >> dist[i][j];
				if (dist[i][j] < 0) dist[i][j] = INF;
			}
		}
		
		// floyd warshall
		for (int k = 1; k <= N; k++) {
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					if (dist[i][j] > dist[i][k] + dist[k][j]) {
						dist[i][j] = dist[i][k] + dist[k][j];
					} 
				}
			}
		}
		
		cout << "Case #" << icase << ":";
		
		int u, v;
		
		for (int q = 0; q < Q; q++) {
			cin >> u >> v;
			
			// go from u to v;
			
			double dp[200];
			for (int i = 1; i <= N; i++) {
				dp[i] = INF;
			}
			dp[u] = 0;
			
			for (int kk = 1; kk <= N; kk++) {
				for (int k = 1; k <= N; k++) {
					for (int i = 1; i <= N; i++) {
						// see if k improves dp[i]
						// u -> k -> i
						if (dist[k][i] <= E[k]) {
							double t = dp[k] + dist[k][i] * S[k];
							dp[i] = min(dp[i], t);
							//cout << "j= " <<j << endl;
							//cout << m << endl;
						}
					}
				}
			}
			
			double ans = dp[v];
			
			cout << fixed << setprecision(9) << " " << ans;
		}
		
		cout << endl;
	}
	return 0;
}
