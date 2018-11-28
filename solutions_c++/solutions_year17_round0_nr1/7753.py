#include <iostream>
using namespace std;

void flip(int i, string &s) {
	if(s[i] == '+') s[i] = '-';
	else s[i] = '+';
	return;
}

int main(void){
	int t; cin >> t;
	for(int tt = 1; tt <= t; tt++){
		string s;
		cin >> s;
		int k;
		cin >> k;
		int ans = 0;
		for(int i = 0; i <= s.size() - k; i++){
			if(s[i] == '-') {
				ans++;
				for(int j = i; j < i + k; j++) flip(j, s);
			}
		}
		for(int i = s.size() - k; i < s.size(); i++) {
			if(s[i] == '-') ans = -1;
		}
		cout << "Case #" << tt << ": ";
		if(ans == -1) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	return 0;
}
