#include <bits/stdc++.h>

using namespace std;

int t, h, l;
string s, ans;

int main() {
	ios_base::sync_with_stdio(false);
	cin >> t;
	while (t--) {
		cin >> s;
		cout << "Case #" << ++h << ": ";
		ans = "";
		int n = s.size();
		for (int i = 0; i < n; i++) {
			int x = s[i] - '0', b = false;
			for (int j = x; j >= 0; j--) {
				string st = "";
				st += ans;
				for (int k = i; k < n; k++)
					st += char(j + '0');
				if (st <= s) {
					ans += char(j + '0'), l = i;
					if (j < x)
						b = true;
					break;
				}
			}
			if (b) break;
		}
		if (ans == s) {
			cout << ans << endl;
			continue;
		}
		for (int i = l + 1; i < n; i++)
			ans += '9';
		reverse(ans.begin(), ans.end());
		while (ans[ans.size() - 1] == '0')
			ans.pop_back();
		reverse(ans.begin(), ans.end());
		cout << ans << endl;
	}
	return 0;
}
