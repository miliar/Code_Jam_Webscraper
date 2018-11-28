#include <bits/stdc++.h>
using namespace std;

typedef pair< int, int > PII;
typedef long long LL;
typedef double db;

const LL lInf = ( LL ) 1E16;
const int Inf = 0x23333333;
const int N = 50;

#define foi( i, x ) for ( auto i=x.begin(); i!=x.end(); ++i )
#define pub( x ) push_back( x )
#define mkp( A, B ) make_pair( A, B )
#define fd( i, y, x ) for ( int i=y-1; i>=x; --i )
#define fo( i, x, y ) for ( int i=x; i<y; ++i )
#define fi first
#define se second

char s[N][N];
int n, m;

void preprocessing()
{
	fill( s[0], s[N], 0 );
	scanf( "%d%d", &n, &m );
	fo ( i, 0, n ) scanf( "%s", s[i] );
}

void solve()
{
	fo ( i, 0, n )
	{
		char pre = '?';
		fo ( j, 0, m ) if ( s[i][j]=='?' )
			s[i][j] = pre;
		else pre = s[i][j];
		pre = '?';
		fd ( j, m, 0 ) if ( s[i][j]=='?' )
			s[i][j] = pre;
		else pre = s[i][j];
	}
	fo ( i, 1, n ) 
	{
		if ( s[i][0]!='?' ) continue;
		fo ( j, 0, m ) s[i][j] = s[ i-1 ][j];
	}
	fd ( i, n-1, 0 )
	{
		if ( s[i][0]!='?' ) continue;
		fo ( j, 0, m ) s[i][j] = s[ i+1 ][j];
	}
	printf( "\n" );
	fo ( i, 0, n ) printf( "%s\n", s[i] );
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

