#include <bits/stdc++.h>
using namespace std;
struct Solver {
	int N;
	vector<int> A;
	Solver() {
		cin >> N;
		A.resize(6);
		for (auto& x: A) cin >> x;
	}
	string ans;
	void run() {
		ans = "IMPOSSIBLE";
		if (A[1] || A[3] || A[5]) return;
		if (2*A[0] <= N && 2*A[2] <= N && 2*A[4] <= N) {
			string r;
			if (A[0] >= A[2] && A[0] >= A[4]) r = string(A[0], 'R') + string(A[2], 'Y') + string(A[4], 'B');
			else if (A[2] >= A[0] && A[2] >= A[4]) r = string(A[2], 'Y') + string(A[0], 'R') + string(A[4], 'B');
			else r = string(A[4], 'B') + string(A[0], 'R') + string(A[2], 'Y');
			int p = 0;
			ans = string(N, '-');
			for (int i = 0; i < N; i += 2) ans[i] = r[p++];
			for (int i = 1; i < N; i += 2) ans[i] = r[p++];
		}
	}
	int tt_;
	void output() {
		cout << "Case #" << tt_ << ": " << ans << endl;
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
