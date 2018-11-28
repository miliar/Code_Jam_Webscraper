#include <bits/stdc++.h>
using namespace std;

bool isTidy(const string& s) {
	char c = '0';
	for ( char x : s ) {
		if ( x < c ) return false;
		c = x;
	}
	return true;
}

string solve(string s) {
	if ( isTidy(s) ) return s;
	for ( int i = s.size()-1; i >= 0; --i ) {
		if ( ( !i && s[i] > '1' ) || ( i && s[i] > '0' ) ) {
			s[i]--;
			if ( isTidy(s) )
				return s;
		}
		s[i] = '9';
	}
	return string(s.size()-1,'9');
}

int main() {
	freopen ( "B-large.in", "r", stdin );
	freopen ( "B.out", "w", stdout );
	
	int ntc;
	cin >> ntc;
	for ( int test = 1; test <= ntc; ++test ) {
		string s;
		cin >> s;
		cout << "Case #" << test << ": " << solve(s) << endl;
	}
	
	return 0;
}
