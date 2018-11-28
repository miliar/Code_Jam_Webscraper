#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

const int MAXN = 1024;

int n, k;
char s[MAXN];

void read()
{
	scanf ( "%s", s );
	scanf ( "%d", &k );

	n = (int) strlen(s);

}

void update (int pos)
{
	for ( int i = pos; i < min ( n, pos + k ); ++ i )
	{
		if ( s[i] == '+' ) s[i] = '-';
		else s[i] = '+';
	}

}

bool check()
{
	for ( int i = 0; i < n; ++ i )
	{
		if ( s[i] == '-' )
			return false;
	}

	return true;

}

void solve (int test)
{
	read();

	int updates = 0;
	for ( int i = 0; i < n - k + 1; ++ i )
	{
		if ( s[i] == '-' )
		{
			updates ++;
			update(i);
		}
	}

	if ( check() )
		printf ( "Case #%d: %d\n", test, updates );
	else
		printf ( "Case #%d: IMPOSSIBLE\n", test );

}

int main()
{
	freopen ( "A-large.in" , "r", stdin );
    freopen ( "a.out", "w", stdout );

	int n;

	scanf ( "%d", &n );

	for ( int i = 1; i <= n; ++ i )
		solve (i);

	return 0;

}