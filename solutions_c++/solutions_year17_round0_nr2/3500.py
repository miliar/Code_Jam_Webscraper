#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
typedef boost::multiprecision::int128_t ll;

struct Solver {
	ll N;
	Solver() {
		cin >> N;
	}
	ll ans = 0;
	void f(int n, ll m) {
		for (int i = n; i <= 9 && 10*m+i <= N; ++ i) {
			ans = max(ans, 10*m+i);
			f(i, 10*m+i);
		}
	}
	void run() {
		f(1, 0);	
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
