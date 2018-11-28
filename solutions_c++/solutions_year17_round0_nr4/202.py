#include <bits/stdc++.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
	for (int j = 0; j < (int) w[i].size(); j++) {
		if (w[i][j] && !seen[j]) {
			seen[j] = true;
			if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)) {
				mr[i] = j;
				mc[j] = i;
				return true;
			}
		}
	}
	return false;
}

int BipartiteMatching(const VVI &w, VI &mr, VI &mc) {
	mr = VI(w.size(), -1);
	mc = VI(w[0].size(), -1);

	int ct = 0;
	for (int i = 0; i < (int) w.size(); i++) {
		VI seen(w[0].size());
		if (FindMatch(i, w, mr, mc, seen)) ct++;
	}
	return ct;
}

void run(int tc) {
	int n, m; cin >> n >> m;
	set<int> col, row, pdia, mdia;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			col.insert(j);
			row.insert(i);
			pdia.insert(i + j);
			mdia.insert(i - j);
		}
	}
	int score = 0;
	map<pair<int, int>, int> init;
	for (int i = 0; i < m; ++i) {
		char type; int x, y; cin >> type >> x >> y; --x; --y;
		if (type == 'x' || type == 'o') {
			col.erase(y);
			row.erase(x);
		}
		if (type == '+' || type == 'o') {
			pdia.erase(x + y);
			mdia.erase(x - y);
		}
		score += type == 'o' ? 2 : 1;
		++init[make_pair(x, y)];
	}
	map<pair<int, int>, string> change;
	for (auto x = row.begin(), y = col.begin(); x != row.end() && y != col.end(); ++x, ++y) {
		change[make_pair(*x, *y)] += 'x';
		++score;
	}
	if (!pdia.empty() || !mdia.empty()) {
		vector<int> vpdia (pdia.begin(), pdia.end());
		vector<int> vmdia (mdia.begin(), mdia.end());
		VVI w (vpdia.size(), VI(vmdia.size()));
		for (int i = 0; i < (int) vpdia.size(); ++i) {
			for (int j = 0; j < (int) vmdia.size(); ++j) {
				int a = vpdia[i], b = vmdia[j];
				if ((a + b) % 2 == 0
						&& (a + b) / 2 >= 0
						&& (a + b) / 2 < n
						&& (a - b) / 2 >= 0
						&& (a - b) / 2 < n) w[i][j] = 1;
			}
		}
		vector<int> mr, mc;
		score += BipartiteMatching(w, mr, mc);
		for (int i = 0; i < (int) mr.size(); ++i) if (mr[i] != -1) {
			int a = vpdia[i], b = vmdia[mr[i]];
			int x = (a + b) / 2;
			int y = (a - b) / 2;
			change[make_pair(x, y)] += '+';
		}
	}
// 	for (auto md = mdia.begin(), pd = pdia.begin(); md != mdia.end() && pd != pdia.end(); ++md, ++pd) {
// 		int x = (*pd + *md) / 2;
// 		int y = (*pd - *md) / 2;
// 		++score;
// 	}
	cout << "Case #" << tc << ": " << score << ' ' << change.size() << '\n';
	for (auto foo : change) {
		auto key = foo.first;
		cout << (init[key] + foo.second.size() == 2 ? "o" : foo.second) << ' ' << key.first + 1 << ' ' << key.second + 1 << '\n';
	}
}

int main() {
	int nt; cin >> nt;
	for (int tc = 1; tc <= nt; ++tc) run(tc);
	return 0;
}
