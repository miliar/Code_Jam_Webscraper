#include <bits/stdc++.h>
using namespace std;
struct Solver {
	int N, P;
	vector<int> G;
	Solver() {
		cin >> N >> P;
		G.resize(N);
		for (auto& x : G) cin >> x;
	}
	int ans;
	void run() {
		vector<int> a(P);
		for (auto x : G) a[x%P]++;

		if (P == 2) {
			ans = a[0] + (a[1]+1)/2;
		} else if (P == 3) {
			ans = a[0];
			ans += min(a[1], a[2]);
			ans += (max(a[1], a[2])-min(a[1], a[2])+2)/3;
		} else {
			ans = 1<<30;
			int x = min(a[1], a[3]);
			int y = max(a[1], a[3]) - min(a[1], a[3]);
			for (int i = 0; i <= a[2]; ++ i) {
				int r = a[0] + x + (a[2]-i+1)/2 + i + (max(0, y - 2*i)+3)/4;
				ans = min(ans, r);
			}
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
