#include <iostream>
#include <string>

using namespace std;

int main() {
	int t = 0;
	cin >> t;
	for (int p = 1; p <= t; ++p) {
		string s;
		cin >> s;
		cout << "Case #" << p << ": ";
		int l = s.length();
		char c = s[l-1];
		string ans = "";
		for (int i = l - 1; i >= 0; --i) {
			if (c > s[i]) {
				c = s[i];
			}
			else if (c < s[i]) {
				c = s[i] - 1;
				ans = string(ans.length(), '9');
			}
			ans += c;
		}
		if (c == '0') {
			cout << string(l - 1, '9') << endl;
		}
		else {
			for (int i = l - 1; i >= 0; --i) cout << ans[i];
			cout << endl;
		}
	}
}
