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

bool check( string const & s)
{
	u32 n = s.size();
	for ( u32 i = 0; i != n; ++i )
		if ( s[ i ] == '-' )
			return false;
	return true;
}

bool happify( string& s, u32 k, int& r )
{
	if ( check( s ) )
		return true;
	
	u32 n = s.size();
	if ( k > n )
		return false;

	if ( k == n )
	{
		for ( u32 i = 1; i != n; ++i )
			if ( s[ i ] != s[ i - 1 ] )
				return false;
	}
	if ( k == 1 )
	{
		int c = 0;
		for ( u32 i = 0; i != s.size(); ++i )
			if ( s[ i ] == '-' ) c++;
		r = c;
		return true;
	}


	if ( s[ 0 ] == '-' )
	{
		u32 c = 0;
		for ( ; c != k; ++c )
		{
			if ( s[ c ] == '-' )
				s[ c ] = '+';
			else
				s[ c ] = '-';
		}

		return happify( s, k , ++r);
	}
	else if ( s[ n - 1 ] == '-' )
	{
		reverse( s.begin(), s.end() );
		return happify( s , k, r);
	}
	else
	{
		u32 c = 0;
		for ( ; c != n; ++c )
			if ( s[ c ] == '-' ) break;

		s = s.substr( c, n-c );

		return happify( s, k, r );
	}
}

int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );

	u32 t,k;
	string s;
	cin >> t;

	for ( u32 i = 0; i != t; ++i )
	{
		cin >> s >> k;
		int r = 0;
		if ( happify( s, k, r ) )
			printf( "Case #%d: %d\n", i+1, r );
		else
			printf( "Case #%d: IMPOSSIBLE\n", i+1 );
	}

    return 0;
}
