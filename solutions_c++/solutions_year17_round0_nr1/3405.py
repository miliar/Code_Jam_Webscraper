#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;

	int c = 1;
	while (t--) {
		string s; cin >> s;
		int k; cin >> k;

		int ans = 0;
		for (int i = 0; i < s.size()-k+1; i++) {
			if (s[i] == '-') {
				for (int j = i; j < i+k; j++) {
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
				ans++;
			}
		}
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '-') ans = -1;
		}
		

		cout << "Case #" << c << ": ";
		if (ans == -1) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
		c++;
	}

	return 0;
}
