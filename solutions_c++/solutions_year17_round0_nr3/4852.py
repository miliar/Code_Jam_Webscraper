#include <iostream>

using namespace std;

int main() {
	long long N, K, T;
	unsigned long long s[61], s1[61];
	s[0] = 1;
	s1[0] = 1;
	for (int i = 1; i < 61; i++) {
		s[i] = s[i - 1] * 2;
		s1[i] = s1[i - 1] + s[i];
		//cout << seka[i] << " " << seka1[i] << endl;
	}
	cin >> T;
	for (int p = 1; p <= T; p++) {
		cin >> N >> K;
		long long gaps, sitting = 0;
		for (int i = 0; i < 61; i++) {
			if (K <= s1[i]) {
				gaps = s[i];
				if (i != 0) {
					sitting = s1[i - 1];
				}
				break;
			}
		}
		long long K1 = K - sitting;
		sitting = N - sitting;
		long long gap = sitting / gaps, extended = sitting % gaps;
		if (K1 <= extended) {
			gap++;
		}
		long long min = gap / 2, max = min - !(gap % 2);
		cout << "Case #" << p << ": " << min << " " << max << endl;
	}
	return 0;
}