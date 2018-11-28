#include <bits/stdc++.h>

using namespace std;

typedef int64_t i64;
typedef long double ld;

template <typename T>
using V = vector<T>;

void solve() {
	int N, K;
	cin >> N >> K;
	ld U;
	cin >> U;
	V<ld> P(N);
	for (auto& p : P)
		cin >> p;
	P.push_back(1);
	sort(P.begin(), P.end());
	int i = 0;
	while (i+1 < P.size()) {
		ld diff = P[i+1] - P[i];
		if (U - 1e-8 > (i+1) * diff) {
			U -= (i+1) * diff;
			++i;
		} else {
			P[i] += U/(i+1);
			U = 0;
			break;
		}
	}
	for (int j = 0; j < i; ++j)
		P[j] = P[i];
	ld res = 1;
	for (ld p : P)
		res *= p;
	cout << setprecision(20) << fixed << res << endl;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		solve();
	}
}