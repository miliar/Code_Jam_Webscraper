#include <iostream>
#include <string>

using namespace std;

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		cout << "Case #" << tt << ": ";
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		for (int i =0; i <= int(s.size()) - k; i++) {
			if (s[i] == '-') {
				ans++;
				for (int j = 0; j < k; j++) {
					if (s[i + j] == '-') {
						s[i + j] = '+';
					}
					else {
						s[i + j] = '-';
					}
				}
			}
		}
		bool ind = 1;
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '-') {
				ind = 0;
			}
		}
		if (ind  ) {
			cout << ans << "\n";
		}
		else {
			cout << "IMPOSSIBLE\n";
		}
	}
}