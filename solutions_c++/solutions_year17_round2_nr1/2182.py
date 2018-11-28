#include <iostream>
#include <cstdio>
using namespace std;

inline double GetMaxSpeed(int d, int k, int s) {
	return (double)d * s / (d - k);
}

int main(void) {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		int D, N;
		cin >> D >> N;
		double maxSpeed = 1000000000000000LL;
		for (int n = 0; n < N; n++) {
			int K, S;
			cin >> K >> S;
			double cur = GetMaxSpeed(D, K, S);
			if (cur < maxSpeed) {
				maxSpeed = cur;
			}
		}
		printf("Case #%d: %f\n", tc, maxSpeed);
	}
}