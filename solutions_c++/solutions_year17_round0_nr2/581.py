#include <bits/stdc++.h>
using namespace std;

int findFailIndex(string &s) {
	for(int i = 0 ; i+1 < s.length() ; i++)
		if(s[i] > s[i+1]) {
			return i;
		}
	return -1;
}

void fixString(string &s, int failIndex) {
	s[failIndex] -= 1;
	for(int i = failIndex+1 ; i < s.length() ; i++)
		s[i] = '9';
}

int main() {
	int t; cin >> t;
	for(int tc = 1 ; tc <= t ; tc++) {
		string s;
		cin >> s;

		int fail = -1;
		while((fail = findFailIndex(s)) != -1) {
			fixString(s, fail);
		}

		if(s[0] == '0') {
			s.erase(s.begin());
		}

		printf("Case #%d: %s\n", tc, s.c_str());
	}
	return 0;
}