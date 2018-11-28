#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

const int MAXN = 32;

int n, m;
char s[MAXN][MAXN];

void read()
{
	scanf ( "%d %d", &n, &m );
	for ( int i = 0; i < n; ++ i )
		scanf ( "%s", s[i] );
}

void update_row ( int x, int y )
{
	char c = s[x][y];

	for ( int i = y + 1; i < m; ++ i )
		if ( s[x][i] == '?' ) s[x][i] = c;
		else break;

	for ( int i = y - 1; i >= 0; -- i )
		if ( s[x][i] == '?' ) s[x][i] = c;
		else break;

}

char find ( int x, int y )
{
	for ( int i = x - 1; i >= 0; -- i )
		if ( s[i][y] != '?' ) return s[i][y];

	for ( int i = x + 1; i < n; ++ i )
		if ( s[i][y] != '?' ) return s[i][y];

}

void update_col()
{
	for ( int i = 0; i < n; ++ i )
		for ( int j = 0; j < m; ++ j )
			if ( s[i][j] == '?' )
				s[i][j] = find ( i, j );
}

void solve ()
{
	for ( int i = 0; i < n; ++ i )
		for ( int j = 0; j < m; ++ j )
			if ( s[i][j] >= 'A' && s[i][j] <= 'Z' )
				update_row ( i, j );

	update_col();

	for ( int i = 0; i < n; ++ i )
		printf ( "%s\n", s[i] );

}

int main()
{
	freopen ( "A-large.in" , "r", stdin );
    freopen ( "a-large.out", "w", stdout );

	int n;

	scanf ( "%d", &n );

	for ( int i = 1; i <= n; ++ i )
	{
		read();
		printf ( "Case #%d:\n", i );
		solve();
	}

	return 0;

}