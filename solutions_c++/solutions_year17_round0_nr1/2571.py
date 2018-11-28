#include <bits/stdc++.h>
using namespace std;

int main() {
	int i, j, t, tc = 0, n, k;
	cin >> t;
	while(t--) {
		tc++;
		cout << "Case #" << tc << ": ";
		string s;
		cin >> s >> k;
		n = s.length();
		int ans = 0;
		for(i = 0; i < n-k+1; ++i) {
			if(s[i] == '-') {
				ans++;
				for(j=i; j < i+k; ++j) {
					if(s[j]=='-')	s[j] = '+';
					else	s[j] = '-';
				}
			}
		}
		bool flag = true;
		for(i = 0; i < n; ++i)
			if(s[i] == '-') {
				flag = false;
				break;
			}
		if(flag) {
			cout << ans << "\n";
		}
		else	cout << "IMPOSSIBLE\n";
	}
	return 0;
}