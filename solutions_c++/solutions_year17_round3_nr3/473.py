#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <iomanip>

using namespace std;

const long double eps = 0.000000001;

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N, K;
		cin >> N >> K;
		long double U;
		cin >> U;

		vector<long double> cs;
		for (int i = 0; i < N; i++) {
			long double P;
			cin >> P;
			cs.push_back(P);
		}

		sort(cs.begin(), cs.end());
		int i = 0;
		while (U > 0.0) {
			while (i < N - 1 && abs(cs[i] - cs[i + 1]) < eps) {
				i++;
			}

			if (i == N - 1) {
				cs[i] += U / (long double)(i + 1);
				U = 0;
			} else if (U >= (cs[i + 1] - cs[i]) * (long double)(i + 1)) {
				U -= (cs[i + 1] - cs[i]) * (long double)(i + 1);
				cs[i] = cs[i + 1];
			} else {
				cs[i] += U / (long double)(i + 1);
				U = 0;
			}
		}

		for (int j = 0; j < i; j++) {
			cs[j] = cs[i];
		}

		long double ans = 1.0;
		for (int j = 0; j < N; j++) {
			ans *= cs[j];
		}

		cout << "Case #" << t << ": " << setprecision(20) << ans << endl;
	}

	return 0;
}