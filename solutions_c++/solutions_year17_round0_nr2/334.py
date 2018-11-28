#include <bits/stdc++.h>
using namespace std;

string s;

string solve() {
	s = "0" + s;
	for (int i = s.length()-1; i >= 1; i--) {
		if (s[i-1] > s[i]) {
			s[i-1]--; // assumes ascii decrement works..
			for (int j = i; j < s.length(); j++) {
				s[j] = '9';
			}
		}
	}
	
	// trim leading zeros
	while (s[0] == '0')
		s = s.substr(1, s.length());
	return s;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> s;
		cout << "Case #" << icase << ": " << solve() << endl;
	}
	return 0;
}
