#include <iostream>
using namespace std;

int main() {
	int T; cin >> T;
	for (int No = 1; No <= T; No++) {
		long long N, K; cin >> N >> K;
		int a;
		for (int i = 63; i >= 0; i--) {
			if ((K >> i) & 1) {
				a = i;
				break;
			}
		}
		long long a2 = 1LL << a;
		long long n = (N - a2 + 1 + (a2 * 2 - 1 - K)) / a2;
		cout << "Case #" << No << ": " << n / 2 << " " << (n-1) / 2 << endl;
	}
	return 0;
}
