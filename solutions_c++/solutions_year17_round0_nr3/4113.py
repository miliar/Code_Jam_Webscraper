#include <stdio.h>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int n, k;

struct pii
{
	int a;
	int b;

	pii( int _a, int _b )
	{
		a = _a;
		b = _b;
	}

	bool operator< ( pii &p )
	{
		if( p.a == this->a )
		{
			return p.b < this->b;
		}
		return p.a < this->a;
	}
};

vector< pii > ans;

void divide( pii p, int index )
{
	ans.push_back( p );

	if( p.a % 2 == 1 )
	{
		pii tmp( p.a / 2, p.a / 2 );
		divide( tmp, index * 2 );
	}
	else
	{
		if( p.a != 0 )
		{
			pii tmp( p.a / 2, p.a / 2 - 1 );
			divide( tmp, index * 2 );
		}
	}

	if( p.b % 2 == 1 )
	{
		pii tmp( p.b / 2, p.b / 2 );
		divide( tmp, index * 2 + 1 );
	}
	else
	{
		if( p.b != 0 )
		{
			pii tmp( p.b / 2, p.b / 2 - 1 );
			divide( tmp, index * 2 + 1 );
		}
	}
}

int main()
{
	freopen( "C-small-2-attempt1.in", "r", stdin );	
	FILE *output = fopen( "gsan.out", "w" );

	int T;
	scanf( "%d", &T );

	for( int tc = 1; tc <= T; tc++ )
	{
		scanf( "%d %d", &n, &k );

		if( n % 2 == 1 )
		{
			pii tmp( n / 2, n / 2 );
			divide( tmp, 1 );
		}
		else
		{
			pii tmp( n / 2, n / 2 - 1 );
			divide( tmp, 1 );
		}

		sort( ans.begin(), ans.end() );

		printf( "Case #%d: %d %d\n", tc, ans[k - 1].a, ans[k - 1].b );
		fprintf( output, "Case #%d: %d %d\n", tc, ans[k - 1].a, ans[k - 1].b );
		ans.clear();
	}

	fclose( output );
	return 0;
}