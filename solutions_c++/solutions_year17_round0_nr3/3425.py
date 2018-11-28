#include <cmath>
#include <iostream>
using namespace std;

class C {
public:
	pair<long, long> stall(long N, long K) {
		long M = log2(K) + 2;
		long occupy = pow(2, M - 2) - 1;
		long index = K - occupy;
		long divisor = pow(2, M - 1);
		long space = N - divisor + 1;
		long max, min;
		long remainder = space % divisor;
		if (remainder >= divisor / 2) {
			max = space / divisor + 1;
			if (index <= remainder - divisor / 2) {
				min = max;
			} else {
				min = max - 1;
			}
		} else {
			min = space / divisor;
			if (index <= remainder) {
				max = min + 1;
			} else {
				max = min;
			}
		}
		return {max, min};
	}
};

int main() {
	int t;
	long N, K;
	C C1;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> N >> K;
		pair<long, long> res = C1.stall(N, K);
		cout << "Case #" << i << ": " << res.first << " " << res.second << endl;
	}
}
