#include <iostream>
#include <string>

using namespace std;

int main() {
	int T; cin >> T;
	for (int test = 1; test <= T; ++test) {
		string s; cin >> s;
		for (int i = s.size() - 2; i >= 0; --i) {
			if (s[i] > s[i + 1]) { // ordering problem, but s[i+1] is first increased when we drop to ?99...
				s[i]--;
				for (int j = i + 1; j < s.size(); ++j) {
					s[j] = '9';
				}
			}
		}
		// can only be one leading zero, because deleting leading digit and replacing
		// remaining digits with 9's always works
		if (s[0] == '0') s = s.substr(1); // delete leading zero
		cout << "Case #" << test << ": " << s << endl;
	}
	return 0;
}