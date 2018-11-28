#include <iostream>
#include <cstdio>
using namespace std;

#define MAXN 1000
long long K[MAXN] = {0};
long long S[MAXN] = {0};

void solve() {
	long long D, N;
	cin >> D >> N;
	for (int i = 0; i < N; i++) {
		cin >> K[i] >> S[i];
	}
	double ans = -1;
	for (int a = 0; a < N; a++) {
		bool ok = true;
		for (int i = 0; i < N; i++) {
			long long denom = D*S[a] - D*S[i] + K[a]*S[i];
			if (denom <= 0) {
				continue;
			}
			if (denom <= K[i]*S[a]) {
				continue;
			}
			ok = false;
			break;
		}
		double v = D*S[a]*1.0/(D-K[a]);
		if (ok && v > ans) {
			ans = v;
		}
	}
	//cout << ans << endl;
	printf("%.7f\n", ans);
}

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cout << "Case #" << (t+1) << ": ";
		solve();
	}
	return 0;
}
