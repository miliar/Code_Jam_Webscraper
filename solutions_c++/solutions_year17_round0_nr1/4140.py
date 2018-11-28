/*
 * A.cpp
 *
 *  Created on: Apr 8, 2017
 *      Author: tigran
 */



#include <iostream>
#include <string>

using namespace std;


void flip( char& ch )
{
	if ( ch == '+' )
		ch = '-';
	else if ( ch == '-' )
		ch = '+';
}


void solve()
{
	string s;
	int K;
	cin >> s >> K;
	int result = 0;
	for ( int i = 0; i + K <= (int)s.length(); ++i ) {
		if ( s[ i ] == '-' ) {
			++result;
			for ( int j = i; j < i + K; ++j )
				flip( s[ j ] );
		}
	}
	for ( int i = s.length() - K; i < (int)s.length(); ++i ) {
		if ( s[ i ] == '-' ) {
			cout << "IMPOSSIBLE";
			return;
		}
	}
	cout << result;
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
