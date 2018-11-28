#include <bits/stdc++.h>
using namespace std;


void solve() {
	string s;
	int k;
	cin >> s >> k;
	int ans = 0;
	int n = s.size();
	for(int i=0;i<=n-k;i++) {
		if(s[i] == '+') continue;
		ans++;
		for(int j=0;j<k;j++) {
			if(s[j+i] == '-') s[j+i] = '+';
			else s[j+i] = '-';
		}
	}
	// cout << s << endl;
	for(int i=0;i<n;i++) {
		if(s[i] == '-') {
			cout << "IMPOSSIBLE\n";
			return;
		}
	}
	cout << ans << "\n";
}


int main() {
	int tc;
	cin >> tc;
	for(int i=1;i<=tc;i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
}