#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
	int t, k;
	string s;
	cin >> t;
	for(int _t = 1; _t <= t; _t++) {
		cin >> s;
		int l = s.length();
		bool changed = false;
		int ind;
		for(int i=l-1; i>=1; i--) {
			if(s[i-1] > s[i]) {
				changed = true;
				ind = i;
				if(s[i-1] != '0') s[i-1]--;
			}
		}
		
		if(changed)
		for(int i=ind; i<l; i++) {
			s[i] = '9';
		}
		
		if(s[0] == '0') { s = s.substr(1, s.length()); }
		
		printf("Case #%d: ", _t);		
		cout << s << endl;
	}
	
	return 0;
}
