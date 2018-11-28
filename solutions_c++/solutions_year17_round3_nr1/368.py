#include <bits/stdc++.h>

using namespace std;

typedef int64_t i64;
typedef long double ld; 

template <typename T>
using V = vector<T>;

const ld pi = 3.14159265359l;

void solve() {
	int K, N;
	cin >> N >> K;
	V<pair<i64, i64>> P(N);
	for (auto& p : P)
		cin >> p.first >> p.second;
	sort(P.begin(), P.end());
	ld best = 0;
	while (P.size() >= K) {
		ld alt = pi * P.back().first * P.back().first + 2*pi*P.back().first*P.back().second;
		P.pop_back();
		auto cpy = P;
		sort(cpy.begin(), cpy.end(), [](pair<i64, i64> lhs, pair<i64, i64> rhs){return lhs.first*lhs.second < rhs.first*rhs.second;});
		for (int k = 0; k < K-1; ++k) {
			auto p = cpy[cpy.size()-1-k];
			alt += 2*pi*p.first*p.second;
		}
		best = max(best, alt);
	}
	cout << setprecision(20) << fixed << best << endl;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		solve();
	}
}