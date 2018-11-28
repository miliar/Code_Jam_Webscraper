#include <iostream>
#include <cstdio>
#include <string>
using namespace std;



int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		for (int i = 0; i < s.length() - k + 1; i++) {
			if (s[i] != '+') {
				ans++;
				for (int j = i; j < i + k; j++) {
					if (s[j] == '+') {
						s[j] = '-';
					} else {
						s[j] = '+';
					}
				}
			}
		}
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '-') {
				ans = -1;
			}
		}
		if (ans == -1) {
			cout << "Case #" << tt << ": " << "IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << tt << ": " << ans << endl;
		}
	}
	return 0;
}