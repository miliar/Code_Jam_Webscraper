#include <iostream>
#include <string>

using namespace std;

int main() {
	int t, k;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		string s;
		int ans = 0;
		cin >> s >> k;
		int j = 0;
		while (j < s.size()) {
			int pj = j;
			while (s[j] == '+') j++;
			if (j > 0 && pj == j) break;
			if (j + k <= s.size()) {
				for (int l = j; l < j + k; l++) {
					if (s[l] == '+') s[l] = '-';
					else s[l] = '+';
				}
				ans++;
			}
		}
		bool possible = true;
		for (int j = 0; j < s.size(); j++) {
			if (s[j] == '-') {
				possible = false;
				break;
			}
		}
		cout << "Case #" << i << ": ";
		if (possible) cout << ans << endl;
		else cout << "IMPOSSIBLE\n";
	}
	return 0;
}