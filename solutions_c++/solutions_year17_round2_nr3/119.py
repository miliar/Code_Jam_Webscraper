#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;
typedef long long int Z;

Z N, Q;

Z D[128][128];
double D2[128][128];
Z E[128];
Z S[128];

int main() {
	cin.sync_with_stdio(false);
	cin.tie(nullptr);
	
	Z tc;
	cin >> tc;
	for(Z ti = 1; ti <= tc; ++ti) {
		cin >> N >> Q;
		for(Z i = 0; i < N; ++i) {
			cin >> E[i] >> S[i];
		}
		for(Z i = 0; i < N; ++i) {
			for(Z j = 0; j < N; ++j) {
				cin >> D[i][j];
			}
		}
		
		for(Z s = 0; s < N; ++s) {
			double* dist = D2[s];
			fill(dist, dist + 128, -1.0);
			priority_queue<pair<Z, Z>> Q;
			Q.emplace(0, s);
			while(!Q.empty()) {
				auto p = Q.top();
				Q.pop();
				Z v = p.second;
				if(-p.first > E[s]) continue;
				if(dist[v] != -1.0) continue;
				dist[v] = -(double)p.first / (double)S[s];
				for(Z x = 0; x < N; ++x) {
					if(D[v][x] == -1) continue;
					Q.emplace(p.first - D[v][x], x);
				}
			}
		}
		
		for(Z k = 0; k < N; ++k) {
			for(Z i = 0; i < N; ++i) {
				for(Z j = 0; j < N; ++j) {
					if(D2[i][k] == -1.0 || D2[k][j] == -1.0) continue;
					double nd = D2[i][k] + D2[k][j];
					if(D2[i][j] == -1.0 || nd < D2[i][j]) {
						D2[i][j] = nd;
					}
				}
			}
		}
		
		cout << "Case #" << ti << ":";
		for(Z i = 0; i < Q; ++i) {
			Z u, v;
			cin >> u >> v;
			--u;
			--v;
			cout << ' ' << setprecision(20) << D2[u][v];
		}
		cout << '\n';
	}
	
	return 0;
}
