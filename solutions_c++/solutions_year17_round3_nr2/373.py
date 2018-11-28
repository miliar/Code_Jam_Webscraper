#include <bits/stdc++.h>

using namespace std;

typedef int64_t i64;
typedef long double ld;

template <typename T>
using V = vector<T>;

V<int> Bc, Bj;

V<V<int>> dptc, dptj;

bool cstart;

int dpfj(int tc, int tj);
int dpfc(int tc, int tj) {
	if (tc < 0 || tj < 0) return 1e9;
	int t = tc+tj;
	if (t == 0) return cstart ? 0 : 1;
	if (dptc[tc][tj] != -1) return dptc[tc][tj];
	int best = 1e9;
	if (Bc[t-1]) best = min(best, dpfc(tc-1, tj));
	if (Bj[t-1]) best = min(best, dpfj(tc, tj-1)+1);
	return dptc[tc][tj] = best;
}

int dpfj(int tc, int tj) {
	if (tc < 0 || tj < 0) return 1e9;
	int t = tc+tj;
	if (t == 0) return cstart ? 1 : 0;
	if (dptj[tc][tj] != -1) return dptj[tc][tj];
	int best = 1e9;
	if (Bc[t-1]) best = min(best, dpfc(tc-1, tj)+1);
	if (Bj[t-1]) best = min(best, dpfj(tc, tj-1));
	return dptj[tc][tj] = best;
}

void solve() {
	int Ac, Aj;
	cin >> Ac >> Aj;
	Bc.assign(1440, 1); Bj.assign(1440, 1);
	for (int i = 0; i < Ac; ++i) {
		int C, D;
		cin >> C >> D;
		for (int t = C; t < D; ++t) {
			Bc[t] = 0;
		}
	}
	for (int i = 0; i < Aj; ++i) {
		int C, D;
		cin >> C >> D;
		for (int t = C; t < D; ++t) {
			Bj[t] = 0;
		}
	}
	int best = 1e9;
	cstart = true;
	dptc.assign(721, V<int>(721, -1)); dptj.assign(721, V<int>(721, -1));
	best = min(best, dpfc(720, 720));
	cstart = false;
	dptc.assign(721, V<int>(721, -1)); dptj.assign(721, V<int>(721, -1));
	best = min(best, dpfj(720, 720));
	cout << best << endl;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		solve();
	}
}