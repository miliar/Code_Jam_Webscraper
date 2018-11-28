#include <iostream>
#include <string>

using namespace std;

string ans(string s) {
	if (s.length() == 1) {
		return s;
	}
	for (int i = 0; i < s.length() - 1; i++) {
		if (s[i] > s[i + 1]) {
			// cout << "first index " << i << endl;
			int j = i;
			while (j >= 0 && s[j] > s[j + 1]) {
				// cout << j << endl;
				s[j]--;
				j--;
			}
			j += 2;
			// cout << s << endl;
			for (; j < s.length(); j++) {
				s[j] = '9';
			}
			if (s[0] == '0') {
				s = s.substr(1);
			}
			return s;
		}
	}
	return s;
}

string file_name = "B-large";

int main() {
	if (fopen("B-large.in", "r")) {
		freopen("B-large.in", "r", stdin);
		freopen("B-large.out", "w", stdout);
	}
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		string s; cin >> s;
		cout << "Case #" << t << ": " << ans(s) << endl;
	}
	// cout << ans("980") << endl;
	// for (int i = 1; i <= 1000; i++) {
	// 	cout << i << " " << ans(to_string(i)) << endl;
	// }
	return 0;
}

// 991 -> 989 -> 899