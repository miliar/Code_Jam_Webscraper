#include <iostream>

using namespace std;

int main() {
	int tt; cin >> tt;
	for (int t = 1; t <= tt; t++) {
		string s; cin >> s; string ss = s;
		bool firstc = false;
		for (int i = (int)s.size()-1; i > 0; i--) {
			if (s[i] < s[i-1]) {
				for (int j = i; j < (int)s.size(); j++) {
					s[j] = '9';
				}
				s[i-1]--;
				if (i-1 == 0) firstc = true;
			}
		}
		if (firstc) {
			cout << "Case #" << t << ": ";
			if (s[0] != '0') cout << s[0];
			for (int i = 0; i < (int)s.size()-1; i++) {
				cout << '9';
			}
			cout << '\n';
		} else {
			cout << "Case #" << t << ": " << s << '\n';
		}
	}
}