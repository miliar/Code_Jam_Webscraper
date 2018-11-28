#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
struct Solver {
	ll N, Q;
	vector<ll> E, S, U, V;
	vector<vector<ll>> D;
	Solver() {
		cin >> N >> Q;
		E.resize(N);
		S.resize(N);
		for (int i = 0; i < N; ++ i) cin >> E[i] >> S[i];
		D.resize(N, vector<ll>(N));
		for (int i = 0; i < N; ++ i) for (int j = 0; j < N; ++ j) cin >> D[i][j];
		U.resize(Q);
		V.resize(Q);
		for (int i = 0; i < Q; ++ i) cin >> U[i] >> V[i];
	}
	vector<double> ans;
	void run() {
		const ll inf = 1LL<<50;
		vector<vector<ll>> dd(N, vector<ll>(N, inf));
		for (int i = 0; i < N; ++ i) for (int j = 0; j < N; ++ j) if (D[i][j] > 0) dd[i][j] = D[i][j];
		for (int i = 0; i < N; ++ i) dd[i][i] = 0;
		for (int k = 0; k < N; ++ k) for (int i = 0; i < N; ++ i) for (int j = 0; j < N; ++ j) {
			dd[i][j] = min(dd[i][j], dd[i][k] + dd[k][j]);
		}

		ans.resize(Q, -1);
		for (int i = 0; i < Q; ++ i) {
			if (ans[i] >= 0) continue;
			vector<double> dist(N, 1e+300);
			priority_queue<pair<double,int>> qu;
			dist[U[i]-1] = 0;
			qu.push({0,(int)U[i]-1});
			while (!qu.empty()) {
				auto d0 = -qu.top().first;
				int p = qu.top().second;
				qu.pop();
				if (dist[p] != d0) continue;
				for (int q = 0; q < N; ++ q) if (p != q && dd[p][q] <= E[p]) {
					auto d = d0 + (double)dd[p][q] / S[p];
					if (d < dist[q]) {
						dist[q] = d;
						qu.push({-d,q});
					}
				}
			}
			for (int j = i; j < Q; ++ j) {
				if (U[j] == U[i]) ans[j] = dist[V[j]-1];
			}
		}
	}
	int tt_;
	void output() {
		cout << "Case #" << tt_ << ":";
		for (auto x : ans) {
			char buf[1000];
			sprintf(buf, " %.7f", x);
			cout << buf;
		}
		cout << endl;
	}
};

int main() {
	int T;
	cin >> T;
	vector<future<Solver*>> results;
	for (int tt = 1; tt <= T; ++ tt) {
		auto a = new Solver;
		a->tt_ = tt;
		results.push_back(async(
			launch::async, // async or deferred
			[](Solver* solver) {
				solver->run();
				return solver;
			},
			a
		));
	}
	for (auto& x : results) {
		auto a = x.get();
		a->output();
		delete a;
	}
}
