#include <bits/stdc++.h>

using namespace std;

bool ok(string s) {
	if (s[0] == '0') return false ;
	for (int i = 0; i + 1 < s.length(); ++i) {
		if (s[i] > s[i + 1]) return false ;
	}
	return true;
}

string s;
int main() {
	int T; cin >> T;
	for (int TK = 1; TK <= T; ++TK) {
		printf("Case #%d: ", TK);
		cin >> s;
		if (ok(s)) {
			cout << s << endl;
			continue ;
		}
		string ans(s.length() - 1, '9');
		for (int i = s.length(); i >= 1; --i) if (s[i - 1] > '0') {
			string tmp = s;
			--tmp[i - 1];
			for (int j = i; j < s.length(); ++j) tmp[j] = '9';
			if (ok(tmp)) {
				ans = tmp;
				break ;
			}
		}
		cout << ans << endl;
	}
	return 0;
}