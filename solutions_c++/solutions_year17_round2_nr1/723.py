#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int main() {
	int T; cin >> T;
	for (int No = 1; No <= T; No++) {
		int D, N; cin >> D >> N;
		vector<int> K(N), S(N);
		for (int i = 0; i < N; i++) {
			cin >> K[i] >> S[i];
		}
		double ans = 1e99;
		for (int i = 0; i < N; i++) {
			double spd = D / ((D - K[i]) * 1.0 / S[i]);
			ans = min(ans, spd);
		}
		printf("Case #%d: %.6f\n", No, ans);
	}
	return 0;
}
