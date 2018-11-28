#include <bits/stdc++.h>
using namespace std;


void solve() {
	string s;
	cin >> s;

	while(1) {
		bool need = false;
		for(int i=1;i<s.size();i++) {
			if(s[i] - '0' < s[i-1] - '0') {
				s[i-1] = ((s[i-1] - '0') - 1) + '0';
				for(int j=i;j<s.size();j++) s[j] = '9';
				need = true;
				break;
			}
		}
		if(!need) break;
	}

	int pr = 0;
	for(;pr<s.size();pr++) {
		if(s[pr] != '0') break;
	}
	for(;pr<s.size();pr++) cout << s[pr];
	cout << "\n";
}


int main() {
	int tc;
	cin >> tc;
	for(int i=1;i<=tc;i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
}