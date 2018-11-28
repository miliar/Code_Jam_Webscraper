#include <bits/stdc++.h>

using namespace std;

string s;
int len;
int main() {
	int T; cin >> T;
	for (int TK = 1; TK <= T; ++TK) {
		printf("Case #%d: ", TK);
		cin >> s;
		cin >> len;
		int cnt = 0;
		for (int i = 0; i + len <= s.length(); ++i) if (s[i] == '-') {
			for (int j = i; j < i + len; ++j) {
				if (s[j] == '-') s[j] = '+'; else s[j] = '-';
			}
			++cnt;
		}
		if (s == string(s.length(), '+')) cout << cnt << endl; else puts("IMPOSSIBLE");
	}
	return 0;
}