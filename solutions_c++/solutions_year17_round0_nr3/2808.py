#include <iostream>
using namespace std;

int main(void)
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		long long N, K;
		cin >> N >> K;
		long long numN = 1;
		long long numNPlusOne = 0;
		long long k;
		for (k = 2; k <= K; k *= 2) {
			long long oldNumN = numN;
			long long oldNumNPlusOne = numNPlusOne;
			if (N % 2 == 1) {
				N = (N-1) / 2;  // 7 => 3
				// 7 => 3,3
				// 8 => 3,4
				numN = 2 * oldNumN + oldNumNPlusOne;
				numNPlusOne = oldNumNPlusOne;
			} else {
				N = (N-2) / 2;  // 8 => 3
				// 8 => 3,4
				// 9 => 4,4
				numN = oldNumN;
				numNPlusOne = oldNumN + 2 * oldNumNPlusOne;
			}
		}
		k /= 2;
		long long left = K - k + 1;
		long long retN;
		if (left <= numNPlusOne) {
			retN = N + 1;
		} else {
			retN = N;
		}
		cout << "Case #" << (t+1) << ": " << (retN / 2) << " " << ((retN - 1) / 2) << endl;
	}
	return 0;
}
