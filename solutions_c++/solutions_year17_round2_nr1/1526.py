#include<bits/stdc++.h>
/*
*/

using namespace std;

int main() {
	long long int T;
	cin >> T;
	for( size_t index = 0; index < T; index++ ) {
		long double len;
		long long int  c;
		cin >> len >> c;
		long double maxtime = 0;
		for( size_t i = 0; i < c; i++ ) {
			long double  K, D;
			cin >> K >> D;
			maxtime = max( maxtime, ( len - K )*1.L / D );
		}
		cout << fixed << setprecision( 20 ) << "Case #" << index + 1 << ": " << len / maxtime << endl;
	}

}
