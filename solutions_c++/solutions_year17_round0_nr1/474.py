#include <iostream>
#include <string>

using namespace std;

int main() {
	int T; cin >> T;
	for (int test = 1; test <= T; ++test) {
		string s; cin >> s;
		int k; cin >> k;

		bool success = true;
		int flips = 0;
		for (int i = 0; i < s.size() && success; ++i) {
			if (s[i] == '-') {
				if (i + k - 1 < s.size()) {
					flips++;
					for (int j = 0; j < k; ++j) {
						if (s[i+j] == '-') s[i+j] = '+';
						else if (s[i+j] == '+') s[i+j] = '-';
					}
				} else {
					success = false;
				}
			}
		}

		cout << "Case #" << test << ": ";
		if (success) cout << flips;
		else cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}