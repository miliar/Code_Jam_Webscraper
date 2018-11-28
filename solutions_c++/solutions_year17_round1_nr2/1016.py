#include <bits/stdc++.h>

using namespace std;

struct range {
	int n;
	int l, u;
	range() : n(0), l(0), u(0) {}
	range(int n, int l, int u) : n(n), l(l), u(u) {}
	bool operator<(const range& rhs) const { return u < rhs.u; }
};

struct event {
	int t;
	range r;
	event() : t(0), r() {}
	event(int t, range r) : t(t), r(r) {}
	bool operator<(const event& rhs) const { return t < rhs.t; }
};

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N, P;
		cin >> N >> P;
		vector<int> R(N);
		for (auto& r : R)
			cin >> r;
		vector<event> eq;
		for (int n = 0; n < N; ++n) {
			for (int p = 0; p < P; ++p) {
				int q;
				cin >> q;
				int ur = (10 * q) / (9 * R[n]) + 1;
				int lr = (10 * q + 11 * R[n] - 1) / (11 * R[n]);
				if (lr < 1) lr = 1;
				if (ur == lr) continue;
				range r(n, lr, ur);
				eq.push_back(event(lr, r));
				eq.push_back(event(ur, r));
			}
		}
		sort(eq.begin(), eq.end());
		int total = 0;
		vector<multiset<range>> viable(N);
		auto it = eq.begin();
		while (it != eq.end()) {
			event e;
			do {
				e = *it++;
				if (e.t == e.r.l) viable[e.r.n].insert(e.r);
				else viable[e.r.n].erase(e.r);
			} while (it != eq.end() && it->t == e.t);
			// cerr << "At t = " << e.t << ":" << endl;
			// for (int n = 0; n < N; ++n) {
			// 	cerr << n << ":";
			// 	for (auto& r : viable[n]) {
			// 		cerr << "\t[" << r.l << "," << r.u << ")";
			// 	}
			// 	cerr << endl;
			// }
			int usable = viable.front().size();
			for (auto& s : viable)
				usable = min(usable, (int) s.size());
			for (int i = 0; i < usable; ++i)
				for (auto& s : viable)
					s.erase(s.begin());
			total += usable;
		}
		cout << "Case #" << t << ": " << total << endl;
	}
}