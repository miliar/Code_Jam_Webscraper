#include <iostream>
#include <vector>
#include <stdio.h>


using namespace std;

int main() {
	int t, T;
	cin >> T;
	for (t = 0; t < T; ++t) {
		uint64_t D;
		int N;
		cin >> D >> N;
		vector<uint64_t> K(N);
		vector<uint64_t> S(N);
		for (int i = 0; i < N; ++i) {
			cin >> K[i] >> S[i];
		}

		vector<double> ft(N);
		
		for (int i = 0; i < N; ++i) {
			double t = ((double)(D - K[i])) / ((double)S[i]);
			if ((i > 0) && (t < ft[i - 1])) {
				t = ft[i - 1];
			}
			ft[i] = t;
		}

		printf("Case #%d: %.6lf\n", t + 1, D / ft[N-1]);
	}
	return 0;
}