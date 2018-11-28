#include <iostream>
using namespace std;

int main(void)
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		long long N;
		cin >> N;
		int d[32];  // Least significant first, which should be the largest digit
		for (int i = 0; i < 32; ++i) {
			d[i] = N % 10;
			N /= 10;
		}
		for (int i = 0; i < 30; ++i) {
			if (d[i] < d[i+1]) {
				for (int j = 0; j <= i; ++j) {
					d[j] = 9;
				}
				d[i+1] -= 1;
			}
		}
		long long ret = 0;
		for (int i = 31; i >= 0; --i) {
			ret *= 10;
			ret += d[i];
		}
		cout << "Case #" << (t+1) << ": " << ret << endl;
	}
	return 0;
}
