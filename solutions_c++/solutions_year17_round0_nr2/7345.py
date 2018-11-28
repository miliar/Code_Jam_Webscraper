#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;

typedef unsigned int u32;

bool isTidy( const string & n )
{
	for ( u32 i = 1; i != n.size(); ++i )
	{
		if ( n[ i ] < n[ i - 1 ] ) return false;
	}
	return true;
}

void tidify( string& s )
{
	u32 n = s.size();
	if ( n == 1 ) return;

	if ( isTidy( s ) ) return;
	u32 lastIdx = n - 1;
	
	if ( s[ lastIdx ] == '0' )
	{
		u32 idx = lastIdx - 1;
		for ( ; idx >= 0; --idx )
			if ( s[ idx ] >= '1' )
				break;
		if ( idx == 0 && s[idx] == '1' )
		{
			s = string( n - 1, '9' );
			return;
		}
		else
		{
			s[ idx ]--;
			idx += 1;
			for ( ; idx != n; ++idx )
				s[ idx ] = '9';

			return tidify( s );
		}
	}
	else
	{
		u32 idx = 1;
		for ( ; idx != n; ++idx )
			if ( s[ idx ] < s[ idx-1 ] )
				break;

		for ( ; idx != n; ++idx )
			s[ idx ] = '0';

		tidify( s );
	}
}

int main()
{
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );

	int t;
	cin >> t;
	string n;

	for ( u32 i = 0; i != t; ++i )
	{
		cin >> n;
		tidify( n );
		printf( "Case #%d: %s\n", i + 1, n.c_str() );
	}

    return 0;
}
