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
	for(int times = 1; times <= T; times++) {
		int n, k; cin >> n >> k;
		map<int, int> mp;
		mp[n] = 1;
		for (int b = 1; k - b > 0; b <<= 1) {
			k -= b;
			map<int, int> next;
			for (auto p : mp) {
				int key, num;
				tie(key, num) = p;
				next[key / 2] += num;
				next[(key - 1) / 2] += num;
			}
			mp = next;
		}
		int ans = (--mp.end())->second >= k ? (--mp.end())->first : mp.begin()->first;
		cout << "Case #" << times << ": " << ans / 2 << " " << (ans - 1) / 2 << endl;
	}
}

signed main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	calc();
#ifdef _MSC_VER
	//system("pause");
#endif
}