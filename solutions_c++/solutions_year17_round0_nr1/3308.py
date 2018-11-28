#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main() {
	int tt;
	std::ios::sync_with_stdio(false);
	cin >> tt;
	for (int t = 0; t < tt; ++t) {
		string s;
		int k;
		cin >> s >> k;
		int n = s.length();
		int carry[1002];
		for (int i = 0; i < n; ++i)
			carry[i] = 0;
		int c = 0, ans = 0;
		for (int i = 0; i < n; ++i) {
			c ^= carry[i];
			if (!((s[i] == '+') ^ c)) {
				++ans;
				if (i + k > n)
					ans = -1000000;
				else {
					c ^= 1;
					carry[i + k] = 1;
				}
			}
		}
		cout << "Case #" << (t + 1) << ": ";
		if (ans < 0) cout << "IMPOSSIBLE\n";
		else cout << ans << endl;
	}
	return 0;
}
