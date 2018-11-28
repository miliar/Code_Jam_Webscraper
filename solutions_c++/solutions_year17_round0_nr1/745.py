#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int No = 1; No <= T; No++) {
		string S;
		int K;
		cin >> S >> K;
		int ans = 0;
		for (int i = 0; i < S.length() - K + 1; i++) {
			if (S[i] == '-') {
				for (int j = 0; j < K; j++) {
					S[i+j] = S[i+j] == '-' ? '+' : '-';
				}
				ans += 1;
			}
		}
		for (int i = S.length() - K + 1; i < S.length(); i++) {
			if (S[i] == '-') {
				ans = -1;
				break;
			}
		}
		cout << "Case #" << No << ": ";
		if (ans == -1) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << ans << endl;
		}
	}
	return 0;
}
