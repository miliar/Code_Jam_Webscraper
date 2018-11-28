#include <bits/stdc++.h>
using namespace std;
const int INF = 1<<30;
struct Solver {
	int Hd, Ad, Hk, Ak, B, D;
	Solver() {
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
	}
	int ans;
	void run() {
		ans = e(Hd, Ad, Hk, Ak);
	}
	int e(int hd, int ad, int hk, int ak) {
		int res = INF;
		int t = 0;
		for (int i = 0; i <= 101; ++ i) {
			int r = f(hd, ad, hk, ak);
			res = min(res, t + r);
			if (ak == 0 || D == 0) return res;
			if (hd - max(0, ak-D) <= 0) {
				hd = Hd - ak;
				++ t;
				if (hd <= 0) return res;
			}
			ak = max(0, ak-D);
			hd -= ak;
			++ t;
			if (hd <= 0) return res;
		}
		return res;
	}
	int f(int hd, int ad, int hk, int ak) {
		int res = INF;
		int t = 0;
		for (int i = 0; i <= 101; ++ i) {
			int r = g(hd, ad, hk, ak);
			res = min(res, t + r);
			if (B == 0) return res;
			if (hd - ak <= 0) {
				hd = Hd - ak;
				++ t;
				if (hd <= 0) return res;
			}
			ad += B;
			hd -= ak;
			++ t;
			if (hd <= 0) return res;
		}
		return res;
	}
	int g(int hd, int ad, int hk, int ak) {
		//cerr << hd << " " << ad << " " << hk << " " << ak << endl;
		bool cure = false;
		for (int t = 1; ; ++ t) {
			if (hk <= ad) return t;
			if (hd - ak <= 0) {
				if (cure) return INF;
				hd = Hd - ak;
				cure = true;
			} else {
				hk -= ad;
				hd -= ak;
				cure = false;
			}
			if (hd <= 0) return INF;
		}
	}
	int tt_;
	void output() {
		cout << "Case #" << tt_ << ": ";
		if (ans == INF) cout << "IMPOSSIBLE" << endl;
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
