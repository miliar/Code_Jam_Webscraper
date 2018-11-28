#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
struct Solver {
	ll D, N;
	vector<ll> K, S;
	Solver() {
		cin >> D >> N;
		K.resize(N);
		S.resize(N);
		for (int i = 0; i < N; ++ i) cin >> K[i] >> S[i];
	}
	double ans = 1e+300;
	void run() {
		for (int i = 0; i < N; ++ i) {
			auto k = K[i];
			auto s = S[i];
			ans = min(ans, D / ((double)(D - k) / s));
		}
	}
	int tt_;
	void output() {
		char buf[100];
		sprintf(buf, "%f", ans);
		cout << "Case #" << tt_ << ": " << buf << endl;
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
