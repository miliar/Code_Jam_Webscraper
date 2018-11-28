#include <bits/stdc++.h>
using namespace std;

struct Solver {
	int N, P;
	vector<int> R;
	vector<vector<int>> Q;
	Solver() {
		cin >> N >> P;
		R.resize(N);
		for (auto& x : R) cin >> x;
		Q.resize(N, vector<int>(P));
		for (auto& y : Q) for (auto& x : y) cin >> x;
	}
	int ans;
	void run() {
		if (N > 2 || P > 8) ans = -1;
		else if (N == 1) {
			for (int i = 0; i < P; ++ i) {
				if (f(Q[0][i])) ++ ans;
			}
		} else if (N == 2) {
			vector<int> a(P);
			for (int i = 0; i < P; ++ i) a[i] = i;
			ans = 0;
			do {
				int r = 0;
				for (int i = 0; i < P; ++ i) {
					if (g(Q[0][i], Q[1][a[i]])) ++ r;
				}
				ans = max(ans, r);
			} while (next_permutation(a.begin(), a.end()));
		} else {
			throw 1;
		}
	}
	pair<int,int> h(int r, int q) {
		int x = (100 * q + 110 * r - 1) / (110 * r);
		int y = (100 * q) / (90 * r);
		// cerr << r << " " << q << " " << x << " " << y << " " << (double)q/r/x << " " << (double)q/r/y << endl;
		return {max(1,x), y};
	}
	bool f(int q0) {
		auto x0 = h(R[0], q0);
		if (x0.first > x0.second) return false;
		return true;
	}
	bool g(int q0, int q1) {
		auto x0 = h(R[0], q0);
		auto x1 = h(R[1], q1);
		if (x0.first > x0.second) return false;
		if (x1.first > x1.second) return false;
		if (x0.first <= x1.first && x1.first <= x0.second) return true;
		if (x0.first <= x1.second && x1.second <= x0.second) return true;
		if (x1.first <= x0.first && x0.first <= x1.second) return true;
		if (x1.first <= x0.second && x0.second <= x1.second) return true;
		// cerr << x0.first << " " << x0.second << " " << x1.first << " " << x1.second << endl;
		return false;
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
