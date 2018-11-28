#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <set>

using namespace std;

using ll = long long;

const double INF = 1e30;

ll D[150][150];
ll E[150];
ll S[150];

double dist[150];
using pdi = pair<double, int>;

double find(int N, int from, int to) {
	for (int i = 0; i < N; ++i) {
		dist[i] = INF;
	}
	dist[from] = 0;
	set<pdi> Q;
	Q.insert(pdi(0, from));
	while (Q.size() > 0) {
		int pos = Q.begin()->second;
		Q.erase(Q.begin());
		for (int nxt = 0; nxt < N; ++nxt) {
			if (pos != nxt && D[pos][nxt] != -1 && D[pos][nxt] <= E[pos]) {
				double delta = 1.*D[pos][nxt] / S[pos];
				if (dist[nxt] > dist[pos] + delta) {
					dist[nxt] = dist[pos] + delta;
					Q.insert(pdi(dist[nxt], nxt));
				}
			}
		}
	}
	return dist[to];
}

void solve() {
	int N, Q;
	scanf("%d%d", &N, &Q);
	for (int i = 0; i < N; ++i) {
		scanf("%lld%lld", &E[i], &S[i]);
	}
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			scanf("%lld", &D[i][j]);
		}
		D[i][i] = 0;
	}
	for (int k = 0; k < N; ++k) {
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				if (D[i][k] == -1 || D[k][j] == -1) {
					continue;
				}
				ll dist = D[i][k] + D[k][j];
				if (D[i][j] == -1 || D[i][j] > dist) {
					D[i][j] = dist;
				}
			}
		}
	}
	for (int i = 0; i < Q; ++i) {
		int a, b;
		scanf("%d%d", &a, &b);
		printf(" %.9lf", find(N, a - 1, b - 1));
	}
	puts("");
}

int main() {
	freopen("cin.txt", "r", stdin);
	freopen("cout.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		fprintf(stderr, "%d\n", i + 1);
		printf("Case #%d:", i + 1);
		solve();
	}
	return 0;
}