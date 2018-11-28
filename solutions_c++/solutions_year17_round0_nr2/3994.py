#include <iostream>
#include <string>
using in = long long int;
using namespace std;

#define forn(i, n) for(in i = 0; i<(n); ++i)
#define forv(i, v) forn(i, v.size())

void testcase() {
	string s; cin >> s;
	int last = 0;
	for(int i = 1; i < s.size(); i++) {
		if(s[i-1] < s[i]) last = i;
		if(s[i-1] > s[i]) {
			s[last]--;
			if(s[last] == '0') {
				forn(i,s.size()-1) cout << "9";
				return;
			} else {
				for(int i = last+1; i < s.size(); i++) s[i]='9';
				break;
			}
		}
	}
	cout << s;
}

int main() {
	int T; cin >> T;
	for(int t = 1; t<=T; t++) {
		cout << "Case #" << t << ": "; testcase(); cout << endl;
	}
}