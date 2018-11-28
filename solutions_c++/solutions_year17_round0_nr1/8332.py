#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main(void) {
	int T;
	cin >> T;
	for (int cc = 1; cc <= T; cc++) {
		int ans = 0;
		string input;
		int k;

		cin >> input >> k;

		int len = input.length();
		int inputN[len];
		for (int c = 0; c < len; c++) {
			if (input[c] == '+') {
				inputN[c] = 1;
			} else {
				inputN[c] = 0;
			}
		}

		for (int c = 0; c < len - k + 1; c++) {
			if (inputN[c] == 0) {
				ans++;
				for (int d = c; d < c+k; d++) {
					inputN[d] ^= 1;
				}
			}
		}

		for (int c = 0; c < len; c++) {
			if (inputN[c] != 1) {
				ans = -1;
			}
		}

		cout << "Case #" << cc << ": ";
		if (ans >= 0) {
			 cout << ans;
		}
		else {
			cout << "IMPOSSIBLE";	
		}
		cout << endl;
	}


	return 0;
}