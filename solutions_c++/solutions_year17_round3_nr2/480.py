#define _CRT_SECURE_NO_WARNINGS
#include "bits/stdc++.h"
using namespace std;

#define int long long

#define rep(i, n) for (signed i = 0; i < signed(n); i++)

#define all(c) begin(c), end(c)
template<typename T>bool maxup(T& a, const T&& b) { if (a < b) { a = b; return true; }; }
template<typename T>bool maxup(T& a, const T& b) { if (a < b) { a = b; return true; }; }
template<typename T>bool minup(T& a, const T&& b) { if (a > b) { a = b; return true; }; }
template<typename T>bool minup(T& a, const T& b) { if (a > b) { a = b; return true; }; }

#define X first
#define Y second

using VVV = vector<vector<vector<int>>>;
using VV = vector<vector<int>>;
using V = vector<int>;
using P = pair<int, int>;
using IP = pair<int, P>;

template<typename T>
inline void input(vector<T>& v) { for (auto& x : v) cin >> x; }

void calc() {
	int T; cin >> T;
	const double pi = 3.141592653;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		int C, J; cin >> C >> J;
		vector<int> v(1440, -1);
		rep(i, C) {
			int from, to; cin >> from >> to;
			for (int t = from; t < to; t++) {
				v[t] = 0;
			}
		}
		rep(i, J) {
			int from, to; cin >> from >> to;
			for (int t = from; t < to; t++) {
				v[t] = 1;
			}
		}
		// cameron == 0, jamie == 1
		vector<VVV> dp(1441, VVV(721, VV(2, V(2, (1ll << 60)))));
		dp[0][0][0][0] = 0;
		dp[0][0][1][1] = 0;
		int ans = 1ll << 60;
		rep(t, 1440) {
			rep(c, 721) {
				int came = c, jami = t - c;
				//cameron can be baby
				if (v[t] != 0 && came < 720) {
					rep(p, 2) {
						dp[t + 1][c + 1][0][p] = min({ dp[t + 1][c + 1][0][p], dp[t][c][0][p], dp[t][c][1][p] + 1 });
						if (t + 1 == 1440) {
							ans = min(ans, dp[t + 1][c + 1][0][p] + (p != 0));
						}
					}
				}
				//jamie can be baby
				if (v[t] != 1 && jami < 720) {
					rep(p, 2) {
						dp[t + 1][c][1][p] = min({ dp[t + 1][c][1][p], dp[t][c][1][p], dp[t][c][0][p] + 1 });
						if (t + 1 == 1440) {
							ans = min(ans, dp[t + 1][c][1][p] + (p != 1));
						}
					}
				}
			}
		}
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