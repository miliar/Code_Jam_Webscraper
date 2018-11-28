/*
 * B.cpp
 *
 *  Created on: Apr 8, 2017
 *      Author: tigran
 */



#include <iostream>
#include <string>
#include <cassert>

using namespace std;


void solve()
{
	string s;
	cin >> s;

	s.insert( 0, 1, '0' );
	bool wasTidy;
	do {
		wasTidy = true;
		for ( int i = 1; i < (int)s.length(); ++i ) {
			if ( s[ i-1 ] > s[ i ] ) {
				wasTidy = false;
				--s[ i-1 ];
				for ( int j = i; j < (int)s.length(); ++j )
					s[ j ] = '9';
				break;
			}
		}
	} while ( ! wasTidy );
	assert( s[ 0 ] == '0' );
	while ( s.length() > 1 && s[ 0 ] == '0' )
		s.erase( 0, 1 );
	cout << s;
}


int main()
{
	int T;
	cin >> T;
	for ( int t = 1; t <= T; ++t ) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
