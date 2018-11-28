#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int t, k, ans;
	string s;

	cin >> t;
	for(int i=1; i<=t; i++) {
		cin >> s >> k;
		ans = 0;
		while(true) {
			int temp = 0;
			for (int j=0; j<s.length() - k + 1; j++) {
				if (s[j] == '-') {
					ans++;
					for (int l=j; l<j+k; l++) {
						if (s[l] == '-') s[l] = '+';
						else s[l] = '-';
					}
				} else {
					temp++;
				}
			}

			if (temp == s.length() - k + 1) {
				break;
			}
		}

		int count = 0;
		for (int j=0; j<s.length(); j++) {
			if (s[j] == '+') {
				count++;
			}
		}
		if (count == s.length()) {
			cout << "Case #" << i << ": " << ans << endl;
		} else {
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		}
	}
}