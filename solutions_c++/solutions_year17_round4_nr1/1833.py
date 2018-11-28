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

void calc() {
	int T; cin >> T;
	for (int i = 1; i <= T; i++) {
		int N, P; cin >> N >> P;
		V v(P);
		rep(i, N) {
			int g; cin >> g;
			v[g % P]++;
		}
		int numg = 0;
		int ans = v[0];
		numg = v[0];
		if (P == 2) {
			ans += v[1] / 2;
			numg += v[1] - v[1] % 2;
		} else if (P == 3) {
			int m = min(v[1], v[2]);
			ans += m;
			numg += 2 * m;
			v[1] -= m;
			v[2] -= m;
			ans += v[1] / 3 + v[2] / 3;
			numg += (v[1] / 3 + v[2] / 3) * 3;
		} else if (P == 4) {
			int a = v[2] / 2;
			v[2] -= a;
			ans += a;
			int b = min(v[1], v[3]);
			ans += b;
			numg += a * 2 + b * 2;
			v[1] -= b; v[3] -= b;
			ans += (v[1] + v[2] + v[3]) / 3;
			numg += ((v[1] + v[2] + v[3]) / 3) * 3;
		}
		ans += numg != N;
		cout << "Case #" << i << ": ";
		cout << ans << endl;
	}
}

signed main() {
	//cin.tie(0);
	//ios::sync_with_stdio(false);
	calc();
#ifdef _DEBUG
	system("pause");
#endif
}