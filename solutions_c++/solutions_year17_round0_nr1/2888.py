#include <iostream>

using namespace std;

int main() {
	if (fopen("A-large.in", "r")) {
		freopen("A-large.in", "r", stdin);
		freopen("A-large.out", "w", stdout);
	}
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		string s; int n;
		cin >> s >> n;
		int ans = 0;
		int length = s.length();
		for (int i = 0; i + n - 1 < length; i++) {
			if (s[i] == '-') {
				for (int j = 0; j < n; j++) {
					if (s[i + j] == '-') {
						s[i + j] = '+';
					} else {
						s[i + j] = '-';
					}
				}
				ans++;
			}
		}
		bool good = true;
		for (int i = 0; i < length; i++) {
			good &= (s[i] == '+');
		}
		if (good) {
			cout << "Case #" << t << ": " << ans << endl;
		} else {
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}