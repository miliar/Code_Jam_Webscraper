#include <bits/stdc++.h>
using namespace std;

int T;

int main() {
	cin >> T;
	for (int t=1; t<=T; t++) {
		double ans, finish = 0;
		int D, N, K, S;
		cin >> D >> N;
		for (int i = 0; i < N; i++) {
			cin >> K >> S;
			double tm = (double)(D-K) / S;
			finish = max(finish, tm);
		}

		printf("Case #%d: %.9f\n", t, D/finish);
	}
}
