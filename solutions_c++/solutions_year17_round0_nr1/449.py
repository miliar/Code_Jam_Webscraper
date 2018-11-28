#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		cout << "Case #" << tc << ": ";
		string s;
		int k;
		cin >> s >> k;
		int sol = 0;
		for (int i = 0; i+k-1 < s.size(); ++i) {
			if (s[i] == '-') {
				++sol;
				for (int j = 0; j < k; ++j) {
					if (s[i+j] == '-') s[i+j] = '+';
					else s[i+j] = '-';
				}
			}
		}
		bool ok = true;
		for (int i = 0; i < s.size(); ++i) {
			char c = s[i];
			if (c == '-') ok = false;
		}
		if (ok) cout << sol << '\n';
		else cout << "IMPOSSIBLE\n";
	}
}