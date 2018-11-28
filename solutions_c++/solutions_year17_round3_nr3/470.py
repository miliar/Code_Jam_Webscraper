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
		int N, K; cin >> N >> K;
		double U; cin >> U;
		priority_queue<pair<double, int>, vector<pair<double, int>>, greater<pair<double, int>>> que;
		map<double, int> mp;
		rep(i, N) {
			double p; cin >> p;
			mp[p]++;
		}
		for (auto p : mp) {
			que.push(p);
		}
		const double eps = 0.000000001;
		while (U > eps) {
			double x; int num;
			tie(x, num) = que.top(); que.pop();
			double sa;
			if (!que.empty()) sa = que.top().first - x;
			else sa = 1;
			if (sa * num <= U) {
				U -= sa * num;
				pair<double, int> t;
				if (!que.empty()) { t = que.top(); que.pop(); }
				else t = make_pair(1.0, 0);
				que.push(make_pair(t.first, t.second + num));
				if (que.size() == 1 && que.top().first + eps > 1) break;
			} else {
				que.push(make_pair(U / num + x, num));
				U = 0;
			}
		}
		double ans = 1;
		while (!que.empty()) {
			ans *= pow(que.top().first, que.top().second);
			que.pop();
		}
		printf("%.8lf\n", ans);
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