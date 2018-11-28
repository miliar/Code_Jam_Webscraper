#include <iostream>

using namespace std;

long long exp10[20];

inline int digit(long long N, int pos) {
	return (N / exp10[pos]) % 10;
}

long long solve(long long N) {
	int ld = 0;
	long long n = 0;
	for (int i = 18; i >= 0; i--) {
		int d = digit(N, i);
		if (d < ld) {
			return solve(n - 1);
		}
		n += exp10[i] * d;
		ld = d;
	}
	return N;
}

int main() {
	ios::sync_with_stdio(false);

	exp10[0] = 1;
	for (int i = 1; i < 20; i++) {
		exp10[i] = exp10[i - 1] * 10;
	}

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		long long N;
		cin >> N;

		long long res = solve(N);

		cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
