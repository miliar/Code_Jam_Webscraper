#include <iostream>
#include <string.h>
#include <vector>
#include <string>
#include <limits.h>
#include <stdint.h>
#include <algorithm>
#include <tuple>
#include <iomanip>
using namespace std;

int main(int argc, char* argv[])
{
	if (argc >= 2) {
		FILE* fp = freopen(argv[1], "r", stdin);
	}

	int T;
	cin >> T;

	auto find_minmax = [](int* st, int N, int j, int& minval_, int& maxval_) {
		int L = 0;
		int R = 0;
		for (int i = j + 1; i < N; i++) {
			if (st[i] != 0) {
				R = i - j - 1;
				break;
			}
		}
		for (int i = j - 1; i >= 0; i--) {
			if (st[i] != 0) {
				L = j - i - 1;
				break;
			}
		}
		int minval = min(L, R);
		int maxval = min(L, R);
		if ((minval > minval_) || (minval == minval_ && maxval > maxval_)) {
			minval_ = minval;
			maxval_ = maxval;
		}
	};

	auto find = [&](int* st, int N) {

	};

	for (int i = 1; i <= T; i++) {
		int D, N;
		cin >> D >> N;
		double max_time = 0;
		while (N--) {
			int K, S;
			cin >> K >> S;
			double time = (double) (D - K) / S;
			max_time = std::max(max_time, time);
		}

		double result = D / max_time;
		//cout << setprecision(7) << "Case #" << i << ": " << result << endl;
		printf("Case #%d: %.7f\n", i, result);
	}

	return 0;
}
