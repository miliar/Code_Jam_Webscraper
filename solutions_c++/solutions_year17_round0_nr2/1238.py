#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

typedef long long ll;

int t, tbk;

int main() {
	cin >> t;
	tbk = t;
	char s[20];
	while (t) {
		t--;
		cout << "Case #" << tbk - t << ": ";
		cin >> s;
		int l = strlen(s);
		char c = '9';
		for (int i = l-1; i >= 0; i--) {
			if (c < s[i]) {
				s[i]--;
				s[i+1] = 0;
			}
			c = s[i];
			while (i > 0 && c == '0') {
				while (i > 0 && s[i] == '0')
					i--;
				s[i] -= 1;
				s[i+1] = 0;
				c = s[i];
			}
		}
		bool nine = false;
		for (int i = 0; i < l; i++) {
			if (nine == true) {
				cout << '9';
			} else if (s[i] == '0') {
				continue;
			} else if (s[i] == 0) {
				nine = true;
				cout << '9';
			} else {
				cout << s[i];
			}
		}
		cout << endl;
	}
}
