#include <iostream>
#include <string>

using namespace std;

int t, n;
string str, s;
bool ok;
char ch;

int main() {
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> str;
		n = str.size(), s = "", ok = true;
		for (int j = 0; j < n && ok; ++j) {
			for (ch = str[j]; s + string(n-s.size(), ch) > str; ch--);
			if (ch != str[j])
				ok = false;
			s += ch;
		}
		s += string(n-s.size(), '9');
		if (s[0] == '0')
			s.erase(s.begin());
		cout << "Case #" << i << ": " << s << endl;
	}
	return 0;
}