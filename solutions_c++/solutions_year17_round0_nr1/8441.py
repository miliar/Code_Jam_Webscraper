/*/**/
#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; tc++) {
		string s;
		cin >> s;
		int k;
		cin >> k;
		int n = s.size();
		int ans = 0;
		for(int i = 0; i <= n - k; i++) {
			if(s[i] == '+') {
				continue;
			}
			ans++;
			for(int j = i; j < i + k; j++) {
				if(s[j] == '-') {
					s[j] = '+';
				}
				else {
					s[j] = '-';
				}
			}
		}
		for(int i = n - k; i < n; i++) {
			if(s[i] == '-') {
				ans = -1;
			}
		}
		cout << "Case #" << tc << ": ";
		if(ans == -1) {
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			cout << ans << endl;
		}
	}
	return 0;
}