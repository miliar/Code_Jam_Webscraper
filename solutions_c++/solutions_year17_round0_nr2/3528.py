#include <iostream>
#include <string>
using namespace std;

const int N = 19;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cout << "Case #" << t + 1 << ": ";

		int64_t n;
		cin >> n;
		int64_t g = -1;
		int64_t e = -1;
		int r = 9;
		for (int64_t i = 1; i <= n; i *= 10) {
			int l = n % (i * 10) / i;
			if (l > r) {
				g = i;
				e = i;
			} else if (l == r && i == e * 10) {
				e = i;
			}
			r = l;
		}
		if (e != -1) {
			for (int64_t i = 1; i < e; i *= 10) {
				int a = n % (i * 10) / i;
				if (a != 9) {
					n -= (a + 1) * i;
				}
			}
		}
		cout << n << endl;
	}
	return 0;
}
