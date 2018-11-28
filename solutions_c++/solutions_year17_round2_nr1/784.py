#include <bits/stdc++.h>

using namespace std;

#define MAXN 1050

int N, D;
int P[MAXN], S[MAXN];

double solve() {
	double maxTime = 0.0;
	for (int i = 0; i < N; i++) {
		double crtTime = (double) (D - P[i]) / S[i];
		maxTime = max(maxTime, crtTime);
	}
	double ret = (double) D / maxTime;
	return ret;
}

int main() {
	assert(freopen("A.in", "r", stdin));
	assert(freopen("A.out", "w", stdout));
	cin.sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		cin >> D >> N;
		for (int i = 0; i < N; i++) {
			cin >> P[i] >> S[i];
		}

		double ans = solve();
		cout << fixed << setprecision(6) << ans << '\n';
		
		cerr << t << endl;
	}

	return 0;
}
