#include <bits/stdc++.h>
using namespace std;

struct Solver {
	string S;
	int K;
	Solver() {
		cin >> S >> K;
	}
	int ans = 0;
	void run() {
		int N = S.length();
		vector<bool> a(N);
		for (int i = 0; i < N; ++ i) a[i] = (S[i] == '+');
		for (int i = 0; i < N; ++ i) {
			if (!a[i]) {
				if (i+K > N) {
					ans = -1;
					break;
				}
				for (int j = 0; j < K; ++ j) a[i+j] = !a[i+j];
				++ ans;
			}
		}
	}
	int tt_;
	void output() {
		cout << "Case #" << tt_ << ": ";
		if (ans < 0) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
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
