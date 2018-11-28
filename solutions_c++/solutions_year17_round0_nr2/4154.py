#include<bits/stdc++.h>
using namespace std;
int main() {
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	long long t, n, ss;
	string s;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> ss;
		s = to_string(ss);
		string ans(s);
		n = s.size();
		int x = -1;
		cout << "Case #" << i << ": ";
		for (int i = 1; i < n; ++i) {
			if (s[i] < s[i - 1]) {
				x = i;
				break;
			}
			ans[i] = s[i];
		}
		if (x != -1) {
			if (s[x - 1] == '1') {
				for (int i = 0; i < n - 1; ++i) {
					ans[i] = '9';
				}
				ans.pop_back();
			} else {
				x--;
				int ff = x - 1;
				while (ff >= 0 && s[ff] == s[x]) {
					ff--;
				}
				ff++;
				ans[ff]--;
				for (int i = ff+1; i < n; ++i) {
					ans[i] = '9';
				}

			}
		}
	/*	string str;
		for (int i = ss; i >= 1; --i) {
			str = to_string(i);
			//cerr<<str<<endl;
			bool ok = true;
			for (int j = 1; j < str.size(); ++j) {
				if (str[j] < str[j - 1]) {
					ok = false;
					break;
				}
			}
			if (ok) {
				break;
			}
		}
		if (ans != str) {
			cerr << "error" << ss << endl;
			cerr << ans << " " << str << endl;
		} else {
			cout << ans << " " << str << endl;
		}*/
		cout << ans << endl;
	}
	return 0;

}
