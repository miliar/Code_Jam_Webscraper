#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cout << "Case #" << t + 1 << ": ";

		int64_t n, k;
		cin >> n >> k;
		int64_t a, b;
		for (int i = 0; ; i++) {
			if (k > 1 << i) {
				n -= 1 << i;
				k -= 1 << i;
			} else {
				a = k;
				b = 1 << i;
				break;
			}
		}
		int64_t r = n - n / b * b;
		int64_t w = n / b + (a <= r ? 1 : 0);
		cout << w / 2 << ' ' << (w - 1) / 2 << endl;
	}
	return 0;
}
