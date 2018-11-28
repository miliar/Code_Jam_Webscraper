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
	const double pi = 3.141592653;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		int N, K; cin >> N >> K;
		vector<vector<double>> dp(N + 1, vector<double>(K + 1, -(1ll << 60)));
		vector<P> v(N);
		rep(i, N) cin >> v[i].first >> v[i].second;
		sort(all(v));
		reverse(all(v));

		rep(i, N) dp[i][0] = 0;
		rep(i, N) rep(j, K) {
			double r = v[i].first;
			double tmp = 0;
			if (j == 0) {
				tmp = r * r * pi;
			}
			tmp += 2 * r * v[i].second * pi;
			dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i][j] + tmp);
			dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);
		}
		//cout << dp[N][K] << endl;
		printf("%.7lf\n", dp[N][K]);
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