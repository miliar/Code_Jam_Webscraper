#include <bits/stdc++.h>
using namespace std;
struct Solver {
	int N, C, M;
	vector<int> P, B;
	Solver() {
		cin >> N >> C >> M;
		P.resize(M);
		B.resize(M);
		for (int i = 0; i < M; ++ i) cin >> P[i] >> B[i];
	}
	pair<int,int> ans;
	void run() {
		vector<vector<int>> a(C);
		for (int i = 0; i < M; ++ i) {
			a[B[i]-1].push_back(P[i]);
		}

		if (C != 2) {
			ans = {-1,-1};
			return;
		}

		vector<int> b(4);
		for (auto x : a[0]) ++b[x==1 ? 2 : 0];
		for (auto x : a[1]) ++b[x==1 ? 3 : 1];
		ans.first = b[2] + b[3] + max(max(0, b[0] - b[3]), max(0, b[1] - b[2]));

		map<int,pair<int,int>> c;
		for (auto x : a[0]) c[x].first++;
		for (auto x : a[1]) c[x].second++;
		for (auto p : c) if (p.first != 1) {
			auto q = p.second;
			int x = ans.first - max(q.first, q.second);
			int y = min(q.first, q.second);
			if (y-x > 0) {
				ans.second = y-x;
			}
		}
	}
	int tt_;
	void output() {
		cout << "Case #" << tt_ << ": " << ans.first << " " << ans.second << endl;
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
