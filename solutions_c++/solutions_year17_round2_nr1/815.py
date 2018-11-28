#include <iostream>
#include <vector>

using namespace std;

int main() {
	int nTests;
	cin >> nTests;
	for (int test = 1; test <= nTests; ++test) {
		int D, N;
		cin >> D >> N;
		vector<int> K(N), S(N);
		for (int i = 0; i < N; ++i) {
			cin >> K[i] >> S[i];
		}
		double ans = -1;
		for (int i = 0; i < N; ++i) {
			double tmp = D / ((D - K[i])/(1.0 * S[i]));
			if (ans < 0 || ans > tmp) {
				ans = tmp;
			}
		}
		cout << "Case #" << test << ": ";
		printf("%.6lf\n", ans);
	}
	return 0;
}
