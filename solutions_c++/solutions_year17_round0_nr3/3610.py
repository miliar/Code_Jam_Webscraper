#include <bits/stdc++.h>
using namespace std;
typedef int ll;

struct Solver {
	ll N, K;
	Solver() {
		cin >> N >> K;
	}
	ll ans1 = 0, ans2 = 0;
	void run() {
		priority_queue<ll> a;
		a.push(N);
		for (ll i = 0; i < K; ++ i) {
			ll n = a.top(); a.pop();
			ans1 = n / 2;
			ans2 = (n-1) / 2;
			if (ans1 > 0) a.push(ans1);
			if (ans2 > 0) a.push(ans2);
		}
	}
	int tt_;
	void output() {
		cout << "Case #" << tt_ << ": " << ans1 << " " << ans2 << endl;
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
