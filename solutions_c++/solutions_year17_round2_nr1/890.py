#include <bits/stdc++.h>
using namespace std;


double solve() {
	double D, N, m = 0;
	double  K, S;
	cin >> D >> N;
    for (int i = 0; i < N; i++) {
		cin >> K >> S;
		m = max(m, (D-K)/S);
	}
	return D / m;
}


int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		printf("%.8f\n", solve());
	}
	return 0;
}

