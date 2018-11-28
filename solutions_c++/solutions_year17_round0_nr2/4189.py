#include <bits/stdc++.h>
using namespace std;
int mx[100];
int main () {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t; cin >> t;
	for (int tt = 1; tt <= t; ++tt) {
		string s; cin >> s; cout << "Case #" << tt << ": ";
		int n = s.length(), flag = 0; s += (char) 100; 
		//for (int i = n - 1; i >= 0; --i) mx[i] = max((int)s[i], mx[i + 1]);
		for (int i = 0; i < n; ++i) 
			if (flag) cout << '9'; 
			else if (s[i] >= s[i + 1]) {
				if (s[i] == s[i + 1]) {
					int j = i;
					while (s[j] == s[j + 1]) ++j;
					if (s[j] < s[j + 1]) { cout << s[i]; continue; } 
				}
				flag = 1;
				if (((s[i] - 1) ^ '0') || i == n - 1) cout << (char)(s[i] - 1);
			} else cout << s[i];
		cout << '\n';
	}
	return 0;
}

