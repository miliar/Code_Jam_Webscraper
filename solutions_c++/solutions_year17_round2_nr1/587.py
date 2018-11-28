#include <bits/stdc++.h>

using namespace std;

#define error(x) cout << #x << " = " << x << "\n"
#define sz(a) int(a.size())

typedef long long int64;
typedef pair<int64, int64> ii;

const double EPS = 1e-9;

int D, N;
int k[1005], s[1005];

double findPos(double v, int i) {
	if (v <= s[i]) return 2e9;
	double t = k[i] / (v - s[i]);
	return v * t;
}

double solve() {
	double L = 0, R = 2e13, mid, res = 1;
	for (int i = 0; i < 100; i++) {
		mid = (L + R) / 2;
		bool ok = 1;
		for (int j = 0; j < N && ok; j++) {
			double x = findPos(mid, j);
			if (x + EPS < D) ok = 0;
		}
		if (ok) res = mid, L = mid;
		else R = mid;
	}
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(0);
	int T; cin >> T;
	for (int te = 1; te <= T; te++) {
		cin >> D >> N;
		for (int i = 0; i < N; i++)
			cin >> k[i] >> s[i];
		cout << fixed << setprecision(6) << "Case #" << te << ": " << solve() << "\n";
	}

	return 0;
}