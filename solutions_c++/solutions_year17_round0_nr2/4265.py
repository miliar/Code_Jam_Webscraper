#include <iostream>

using namespace std;

string ans(string s) {
	int cmp = 0;
	while (cmp != -1) {
		cmp = -1;
		for (int i = 1; i < s.size(); ++i) {
			if (s[i] < s[i - 1]) {
				cmp = i - 1;
				break;
			}
		}
		if (cmp == -1) {
			return s;
		}
		s[cmp] = char(s[cmp] - 1);
		for (int i = cmp + 1; i < s.size(); ++i) {
			s[i] = '9';
		}
		while (s[0] == '0') {
			s.erase(0,1);
		}
	}
	return s;
}

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		string s;
		cin >> s;
		string res = ans(s);
		cout << "Case #" << t + 1 << ": " << res << "\n";
	}
	return 0;
}