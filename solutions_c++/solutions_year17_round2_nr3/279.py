#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <deque>
#include <queue>
#include <algorithm>
#include <utility>
#include <cstring>
using namespace std;

void buildG(const vector<vector<int>>& D, vector<double>& G, int v, int64_t e, int s)
{
	int N = D.size();
	vector<char> visited(N);
	using pp = pair<int64_t, int>;
	priority_queue<pp, vector<pp>, greater<pp>> Q;
	Q.emplace(0.0, v);
	while (!Q.empty()) {
		auto p = Q.top();
		Q.pop();
		int u = p.second;
		if (!visited[u]) {
			//printf("------ u:%d, d:%lld\n", u, p.first);
			visited[u] = true;
			if (p.first <= e) {
				//printf("v:%d u:%d d:%lld e:%lld\n", v, u, p.first, e);
				G[u] = double(p.first) / s;
			}
			for (int w = 0; w < N; ++w) {
				if (!visited[w] && D[u][w] != -1) {
					//printf("-- v:%d u:%d w:%d d:%lld\n", v, u, w, p.first + D[u][w]);
					Q.emplace(p.first + D[u][w], w);
				}
			}
		}
	}
}

int main(int argc, char** argv)
{
	if (argc > 1) {
		freopen(argv[1], "rb", stdin);
	}
	int t;
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		int N, Q;
		scanf("%d%d", &N, &Q);
		vector<int> E(N), S(N);
		for (int i = 0; i < N; ++i) {
			scanf("%d%d", &E[i], &S[i]);
		}
		vector<vector<int>> D(N, vector<int>(N));
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				scanf("%d", &D[i][j]);
			}
		}
		vector<int> U(Q), V(Q);
		for (int i = 0; i < Q; ++i) {
			scanf("%d%d", &U[i], &V[i]);
		}
		vector<vector<double>> G(N, vector<double>(N, 10e100));
		for (int f = 0; f < N; ++f) {
			buildG(D, G[f], f, E[f], S[f]);
		}
//		for (int j = 0; j < N; ++j) {
//			for (int i = 0; i < N; ++i) {
//				printf("%.6g ", G[j][i]);
//			}
//			printf("\n");
//		}
		for (int w = 0; w < N; ++w) {
			for (int u = 0; u < N; ++u) {
				for (int v = 0; v < N; ++v) {
					if (G[u][v] > G[u][w] + G[w][v]) {
						G[u][v] = G[u][w] + G[w][v];
					}
				}
			}
		}
		printf("Case #%d:", ti+1);
		for (int i = 0; i < Q; ++i) {
			printf(" %.9f", G[U[i]-1][V[i]-1]);
		}
		printf("\n");
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
