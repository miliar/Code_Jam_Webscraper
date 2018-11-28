#include <bits/stdc++.h>
using namespace std;
int main() {
	int n, m, k, ans = 0;
	string s;
	cin >> n;
	for(int test = 1; test <= n; test++) {
		cin >> s >> k;
		m = s.size(); ans = 0;
		for(int i = 0; i < m - k + 1; i++) {
			if(s[i] == '-') {
				ans += 1;
				for(int j = i; j < i + k; j++) {
					if(s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		cout << "Case #" << test << ": ";
		for(int i = m - k; i < m; i++) {
			if(s[i] == '-') {
				cout << "IMPOSSIBLE" << endl;
				ans = -1;
				break;
			}
		}
		if (ans != -1) cout << ans << endl;
	}
}