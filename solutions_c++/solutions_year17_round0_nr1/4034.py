#include <iostream>
#include <string>
using in = long long int;
using namespace std;

#define forn(i, n) for(in i = 0; i<(n); ++i)
#define forv(i, v) forn(i, v.size())

void testcase() {
	string s; cin >> s;
	in k; cin >> k;
	// cout << s << " " << k << " res ";
	in n = s.size();
	in res = 0;
	for(in i = 0; i < n; i++) {		
		if(s[i]=='-') {
			if(i <= n-k) {
				res++;
				for(int j = i; j < i+k; j++) {
					s[j] = (s[j]=='-') ? '+' : '-';
				}
			} else {
				cout << "IMPOSSIBLE";
				return;
			}
		}
	}
	cout << res;
}

int main() {
	int T; cin >> T;
	for(int t = 1; t<=T; t++) {
		cout << "Case #" << t << ": "; testcase(); cout << endl;
	}
}