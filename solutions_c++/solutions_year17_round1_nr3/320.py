#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>

using namespace std;

int solve() {
	struct state {
		int turn;
		int Hd, Ad, Hk, Ak;

		bool operator<(const state &s) const {
			if (Hd != s.Hd) return Hd < s.Hd;
			if (Ad != s.Ad) return Ad < s.Ad;
			if (Hk != s.Hk) return Hk < s.Hk;
			return Ak < s.Ak;
		}
	};

	int Hd, Ad, Hk, Ak, B, D;
	cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

	queue<state> q;
	q.push({0, Hd, Ad, Hk, Ak});

	set<state> used;
	used.insert({ 0, Hd, Ad, Hk, Ak });

	auto enqueue = [&](state st) {
		if (st.Hd > 0 && used.count(st) == 0) {
			used.insert(st);
			q.push(st);
		}
	};

	while (!q.empty()) {
		state st = q.front();
		q.pop();

		// attack
		if (st.Hk - st.Ad <= 0) {
			return st.turn + 1;
		}
		enqueue({ st.turn + 1, st.Hd - st.Ak, st.Ad, st.Hk - st.Ad, st.Ak });
		
		// buff
		enqueue({ st.turn + 1, st.Hd - st.Ak, min(st.Ad + B, st.Hk), st.Hk, st.Ak });
		
		// cure
		enqueue({ st.turn + 1, Hd - st.Ak, st.Ad, st.Hk, st.Ak });
		
		// debuff
		enqueue({ st.turn + 1, st.Hd - max(0, st.Ak - D), st.Ad, st.Hk, max(0, st.Ak - D) });
	}

	return -1;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "case #" << i << ": ";
		int ans = solve();
		if (ans == -1) {
			cout << "Impossible" << endl;
		} else {
			cout << ans << endl;
		}
	}
}