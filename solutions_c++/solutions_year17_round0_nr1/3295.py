#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	int C = 1;
	cin >> T;
	while (T--) {
		string s;
		cin >> s;
		int K;
		cin >> K;
		int ans = 0;
		for (int i = 0; i <= s.length()-K; i++) {
			string newS = s;
			if (s[i] == '-') {
				for (int j = i; j < i+K; j++) {
					if (s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';

				}
				ans++;
			}
		}
		bool good = true;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '-') {
				good = false;
			}
		}
		if (good) {
			cout << "Case #" << C++ << ": " << ans << endl;
		} else {
			cout << "Case #" << C++ << ": IMPOSSIBLE" << endl;
		}
	}
}