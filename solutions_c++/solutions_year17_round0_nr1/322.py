#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen ( "A-large.in", "r", stdin );
	freopen ( "A.out", "w", stdout );
	
	string s;
	int ntc, k;
	cin >> ntc;
	for ( int test = 1; test <= ntc; ++test ) {
		cin >> s >> k;
		int ans = 0;
		for ( int i = 0; i+k <= s.size(); ++i )
			if ( s[i] == '-' )  {
				for ( int j = i; j < i+k; ++j )
					s[j] = s[j] == '-' ? '+' : '-';
				ans++;
			}
		cout << "Case #" << test << ": ";
		if ( s.find('-') == string::npos )
			cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	
	return 0;
}
