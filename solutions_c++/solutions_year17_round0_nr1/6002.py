#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

bool happy[1010];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t, k;
	string s;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		cin >> s >> k;
		int len = s.size();
		if (len < k) {
			cout << "Case #" << tc << ": IMPOSSIBLE\n";
			continue;
		}
		for (int i = 0; i < len; i++) {
			if (s[i] == '+') happy[i] = true;
			else happy[i] = false;
		}
		int count = 0;
		for (int i = 0; i <= len - k; i++) {
			if (happy[i]) continue;
			count++;
			for (int j = 0; j < k; j++)
				happy[i + j] = !happy[i + j];
		}
		bool ok = true;
		for (int i = len - k; i < len; i++) {
			if (!happy[i]) {
				ok = false;
				break;
			}
		}
		if (ok) cout << "Case #" << tc << ": " << count << '\n';
		else cout << "Case #" << tc << ": IMPOSSIBLE\n";
	}
	return 0;
}