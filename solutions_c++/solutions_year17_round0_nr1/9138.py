#include <bits/stdc++.h>
using namespace std;

#define LL long long int

int main() {

	LL t, k;
	cin >> t;
	string s;
	for(int i = 1; i <= t; i++) {
		cin >> s >> k;
		s = '#' + s;
		int ans = 0;

		for(int j = 1; j + k <= (int)s.size(); j++) {
			if(s[j] == '-') {
				ans++;
				for(int m = j; m <= j + k - 1; m++) {
					if(s[m] == '+') s[m] = '-';
					else s[m] = '+';
				}
			}
		}

		bool ok = true;

		for(int j = (int)s.size() - k; j <= (int)s.size()-1; j++) 
			if(s[j] != '+') {
				ok = false;
				break;
			}

		if(ok) cout << "Case #" << i << ": " <<  ans << endl;
		else cout << "Case #" << i << ": " <<  "IMPOSSIBLE" << endl;
	}
	return 0;
}