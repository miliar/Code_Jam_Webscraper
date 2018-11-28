#include <bits/stdc++.h>

using namespace std;

bool is_tidy(string& s) {
	for (int i = 1; i < s.size(); ++ i) {
		if (s[i] < s[i - 1]) {
			return false;
		}
	}
	return true;
}

int main() {
	int tes;

	cin >> tes;
	for (int tcase = 1; tcase <= tes; ++ tcase) {
		string s;
		cin >> s;

		cout << "Case #" << tcase << ": ";
		if (is_tidy(s)) {
			cout << s << "\n";
			continue;
		}

		int err;
		for (err = 1; err < s.size(); ++ err) {
			if (s[err] < s[err - 1]) {
				break;
			}
		}

		char val = s[err - 1];
		int i;
		for (i = err - 1; i >= 0 && s[i] == val; -- i) {
			s[i] = '9';
		}
		s[i + 1] = val - 1;


		for (int i = err; i < s.size(); ++ i) {
			s[i] = '9';
		}

		if (s[0] == '0') {
			s.erase(s.begin());
		}

		for (int i = 0; i < s.size() && s[i] == '0'; ++ i) {
			s[i] = '9';
		}

		cout << s << "\n";
	}

	return 0;
}