#define _CRT_SECURE_NO_WARNINGS
#include "bits/stdc++.h"
using namespace std;

#define int long long

#define CHOOSE(a) CHOOSE2 a
#define CHOOSE2(a0,a1,a2,a3,x,...) x
#define REP1(i, s, cond, cal) for (signed i = signed(s); i cond; i cal)
#define REP2(i, s, n) REP1(i, s, < signed(n), ++)
#define REP3(i, n) REP2(i, 0, n)
#define rep(...) CHOOSE((__VA_ARGS__,REP1,REP2,REP3))(__VA_ARGS__)
#define rrep(i, s) rep(i, s, >= 0, --)

#define all(c) begin(c), end(c)
template<typename T>bool maxup(T& a, const T&& b) { if (a < b) { a = b; return true; }; }
template<typename T>bool maxup(T& a, const T& b) { if (a < b) { a = b; return true; }; }
template<typename T>bool minup(T& a, const T&& b) { if (a > b) { a = b; return true; }; }
template<typename T>bool minup(T& a, const T& b) { if (a > b) { a = b; return true; }; }

#define X first
#define Y second

using VV = vector<vector<int>>;
using V = vector<int>;
using P = pair<int, int>;
using IP = pair<int, P>;

template<typename T>
inline void input(vector<T>& v) { for (auto& x : v) cin >> x; }

#define REP(i, s, n) for (signed i = signed(s); i < signed(n); i++)
#define rrep(i, s) for (signed i = s - 1; i >= 0; i--)
#define rep(i, n) for (signed i = 0; i < signed(n); i++)

void calc() {

	int T; cin >> T;
	for (int times = 1; times <= T; times++) {
		cout << "Case #" << times << ":" << endl;
		int r, c; cin >> r >> c;
		vector<string> v(r);
		rep(i, r) cin >> v[i];
		REP(i, 1, r) rep(j, c) if (v[i][j] == '?') {
			v[i][j] = v[i - 1][j];
		}
		rrep(i, r - 1) rep(j, c) if (v[i][j] == '?') {
			v[i][j] = v[i + 1][j];
		}

		rep(i, r) REP(j, 1, c) if (v[i][j] == '?') {
			v[i][j] = v[i][j - 1];
		}

		rep(i, r) rrep(j, c - 1) if (v[i][j] == '?') {
			v[i][j] = v[i][j + 1];
		}

		rep(i, r) cout << v[i] << endl;
	}
}

signed main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	calc();
#ifdef _DEBUG
	system("pause");
#endif
}