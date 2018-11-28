#include <bits/stdc++.h>

using namespace std;

int tests;

int main() 
{
	//ios_base::sync_with_stdio(false);
	//cin.tie(0);
	
	freopen("input-large.in", "r", stdin);
	freopen("output-large.out", "w", stdout);
	
	
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		string s;
		int ans = 0, len, k;
		cin >> s >> k;
		len = s.length();
		for (int i = 0; i <= len - k; ++i) {
			if (s[i] == '-') {
				++ans;
				for (int j = 0; j < k; ++j) {
					char c = s[i + j];
					s[i + j] = c == '-' ? '+' : '-';
				}
			}
		}
		int IMP = 0;
		for (int i = 0; i < len; ++i) {
			if (s[i] == '-') {
				IMP = 1;
				break;
			}
		}
		cout << "Case #" << test << ": ";
		if (IMP) cout << "IMPOSSIBLE\n";
		else cout << ans << endl;
	}
	return 0;
}
