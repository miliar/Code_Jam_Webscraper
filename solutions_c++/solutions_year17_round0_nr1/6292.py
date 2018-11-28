#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

char s[2000];

int main () {
	int T, k;
	cin >> T;
	for ( int kase = 1; kase <= T; kase ++ ) {
		cin >> s >> k;
		int len = ( int ) strlen (s);
		//cout << s <<" " << k << endl;

		int ans = 0;
		for ( int i = 0; i < len - k + 1; i ++ ) {
			if ( s[i] == '-' ) {
				ans ++;
				for ( int j = i; j < i + k; j ++ ) {
					s[j] = ( s[j] == '+' ) ? '-' : '+';
				}
			}
		}

		bool f = 0;
		for ( int i = 0; i < len; i ++ ) {
			if ( s[i] == '-' ) {
				f = 1;
				break;
			}
		}
		printf("Case #%d: ", kase);
		if ( f ) {
			printf ("IMPOSSIBLE\n");
		}
		else {
			cout << ans << endl;
		}
	}
	return 0;
}