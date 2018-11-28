#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

const int MAXN = 32;

int n;
char s[MAXN];
int num;

void read_large()
{
	scanf ( "%s", s );

	n = ( int ) strlen ( s );

}

void read_small()
{
	scanf ( "%d", &n );
}

bool check ( int num )
{
	int prev = 10;

	while ( num > 0 ) 
	{
		int dig = num % 10;

		if ( dig > prev ) 
			return false;

		num /= 10;
		prev = dig;

	}

	return true;

}

void solve_small(int test)
{
	read_small();

	for ( int i = n; ; -- i )
	{
		if ( check(i) )
		{
			printf ( "Case #%d: %d\n", test, i );
			return;
		}
	}

}

void solve_large(int test)
{
	read_large();

	if ( n == 1 ) 
	{
		printf ( "Case #%d: %s\n", test, s );
		return;
	}

	for ( int i = 0; i < n - 1; ++ i )
	{
		if ( s[i] - '0' > s[i + 1] - '0' )
		{
			int k = i;
			for ( ; k >= 0; -- k )
				if ( s[i] != s[k] )
					break;

			s[k + 1] --;

			for ( int j = k + 2; j < n; ++ j )
			{
				s[j] = '9';
			}
		}
	}

	printf ( "Case #%d: ", test );
	for ( int i = 0; i < n; ++ i )
	{
		if ( i == 0 && s[i] == '0' )
			continue;

		printf ( "%c", s[i] );
	}

	printf ( "\n" );

}

int main()
{
	freopen ( "B-large.in" , "r", stdin );
    freopen ( "b1.out", "w", stdout );

	int tests;

	scanf ( "%d", &tests );

	for ( int i = 1; i <= tests; ++ i )
		solve_large(i);

	return 0;

}