#include <bits/stdc++.h>
using namespace std;

#define fo( i, x, y ) for ( int i=x; i<y; ++i )
const int N = 10005;

char s[N];
int a[N];
int n, m;

void preprocessing()
{
	scanf( "%s", s ), n = strlen( s );
	scanf( "%d", &m );
}

void solve()
{
	int ret = 0x7FFFFFFF;
	fo ( times, 0, 2 ) 
	{
		reverse( s, s + n );
		fo ( i, 1, n ) a[i] = ( s[i]!=s[ i-1 ] );
		a[0] = ( s[0]=='-' );
		int sum = 0, ok = 1;
		fo ( i, 0, n-m+1 ) 
		{
			sum += a[i];
			a[ i+m ] ^= a[i];
			a[i] = 0;
		}
		fo ( i, 1, n ) ok &= ( !a[i] );
		if ( ok ) ret = min( ret, sum );
	}
	if ( ret<0x7FFFFFFF ) printf( "%d\n", ret );
	else printf( "IMPOSSIBLE\n" );
}

int main()
{
	freopen( "a.in", "r", stdin );
	freopen( "a.out", "w", stdout );
	int T;
	scanf( "%d", &T );
	fo ( Case, 0, T )
	{
		preprocessing();
		printf( "Case #%d: ", Case+1 );
		solve();
	}
	return 0;
}

