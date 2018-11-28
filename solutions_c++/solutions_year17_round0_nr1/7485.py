#include <bits/stdc++.h>
using namespace std;


int main() {
	// your code goes here
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int T=1; T <= t; T++) {
		cout << "Case #" << T << ": ";
		string s;
		cin >> s;
		int k;
		cin >> k;
		int last = -1;
		int pos = -1;
		int ans = 0;
		while (1) {
			for (int i=0; i<s.length(); i++) {
				if (s[i]=='-') {
					pos = i;
					break;
				}
			}
			if (pos == -1) {
				cout << ans;
				break;
			}
			else {
				last = pos;
				pos = -1;
				if (last + k > s.length()) {
					cout << "IMPOSSIBLE";
					break;
				}
				else {
					for (int i=last; i < last + k; i++) {
						if (s[i]=='+') s[i]='-';
						else s[i] = '+';
					}
					ans++;
				}
			}
		}
		cout << endl;
	}
	return 0;
}
