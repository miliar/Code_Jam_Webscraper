#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

typedef pair<double, int> P;

void dijk(int n, int s, const vector<int>& E, const vector<int>&S,
	const vector<vector<int>>& D, vector<double>& DD)
{

	priority_queue<P, vector<P>, greater<P>> que;
	vector<double> d(n, HUGE_VAL);
	d[s] = 0.0;
	que.push(P(0, s));

	while (!que.empty()) {
		auto p = que.top(); que.pop();
		auto v = p.second;
		if (d[v] < p.first) continue;
		for (int j = 0; j < n; j++) {
			if (D[v][j] < 0) continue;
			if (d[j] > d[v] + D[v][j]) {
				d[j] = d[v] + D[v][j];
				que.push(P(d[j], j));
			}
		}
	}

	for (int i = 0; i < n; i++) {
		if (d[i] <= E[s])
			DD[i] = d[i] / S[s];
	}
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int N, Q;
		cin >> N >> Q;
		vector<int> E(N), S(N);
		for (int i = 0; i < N; i++) {
			cin >> E[i] >> S[i];
		}
		vector<vector<int>> D(N, vector<int>(N));
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> D[i][j];
			}
		}

		vector<vector<double>> DD(N, vector<double>(N, HUGE_VAL));
		for (int i = 0; i < N; i++) {
			dijk(N, i, E, S, D, DD[i]);
		}

		printf("Case #%d: ", t + 1);
		vector<int> U(Q), V(Q);
		for (int i = 0; i < Q; i++) {
			cin >> U[i] >> V[i];
			U[i]--;
			V[i]--;
			priority_queue<P, vector<P>, greater<P>> que;
			vector<double> d(N, HUGE_VAL);
			d[U[i]] = 0.0;
			que.push(P(0, U[i]));

			while (!que.empty()) {
				auto p = que.top(); que.pop();
				auto v = p.second;
				if (d[v] < p.first) continue;
				for (int j = 0; j < N; j++) {
					if (DD[v][j] < 0) continue;
					if (d[j] > d[v] + DD[v][j]) {
						d[j] = d[v] + DD[v][j];
						que.push(P(d[j], j));
					}
				}
			}
			printf("%.10f ", d[V[i]]);
		}
		puts("");
	}
	return 0;
}
