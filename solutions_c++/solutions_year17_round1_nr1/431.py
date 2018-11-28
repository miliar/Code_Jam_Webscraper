#include <bits/stdc++.h>
using namespace std;

int main() {
	int nt; cin >> nt;
	for (int tc = 1; tc <= nt; ++tc) {
		int m, n; cin >> m >> n;
		string s[m];
		for (int i = 0; i < m; ++i) cin >> s[i];
		for (int j = 0; j < n; ++j) {
			for (int i = 1; i < m; ++i) {
				if (s[i][j] == '?') s[i][j] = s[i - 1][j];
			}
			for (int i = m - 2; i >= 0; --i) {
				if (s[i][j] == '?') s[i][j] = s[i + 1][j];
			}
		}
		for (int i = 0; i < m; ++i) {
			for (int j = 1; j < n; ++j) {
				if (s[i][j] == '?') s[i][j] = s[i][j - 1];
			}
			for (int j = n - 2; j >= 0; --j) {
				if (s[i][j] == '?') s[i][j] = s[i][j + 1];
			}
		}
		cout << "Case #" << tc << ":" << '\n';
		for (int i = 0; i < m; ++i) cout << s[i] << '\n';
	}
	return 0;
}
