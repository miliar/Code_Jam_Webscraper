#include <bits/stdc++.h>
using namespace std;

struct Solver {
	int R, C;
	vector<string> A;
	Solver() {
		cin >> R >> C;
		A.resize(R);
		for (auto& x : A) cin >> x;
	}
	vector<string> ans;
	void run() {
		ans = A;
		for (int i = 0; i < R; ++ i) for (int j = 1; j < C; ++ j) {
			if (ans[i][j] == '?') ans[i][j] = ans[i][j-1];
		}
		for (int i = 0; i < R; ++ i) for (int j = C-2; j >= 0; -- j) {
			if (ans[i][j] == '?') ans[i][j] = ans[i][j+1];
		}
		for (int j = 0; j < C; ++ j) for (int i = 1; i < R; ++ i) {
			if (ans[i][j] == '?') ans[i][j] = ans[i-1][j];
		}
		for (int j = 0; j < C; ++ j) for (int i = R-2; i >= 0; -- i) {
			if (ans[i][j] == '?') ans[i][j] = ans[i+1][j];
		}
	}
	int tt_;
	void output() {
		cout << "Case #" << tt_ << ": " << endl;
		for (auto x : ans) cout << x << endl;
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
