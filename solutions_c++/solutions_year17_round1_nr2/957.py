#include <bits/stdc++.h>
using namespace std;

typedef pair< int, int > PII;
typedef long long LL;
typedef double db;

const LL lInf = ( LL ) 1E16;
const int Inf = 0x23333333;
const int N = 55;

#define foi( i, x ) for ( auto i=x.begin(); i!=x.end(); ++i )
#define pub( x ) push_back( x )
#define mkp( A, B ) make_pair( A, B )
#define fo( i, x, y ) for ( int i=x; i<y; ++i )
#define fi first
#define se second

int ceil( int x, int y )
{
	if ( x % y ) return x / y + 1;
	else return x / y;
}
int floor( int x, int y )
{
	return x / y;
}
PII getrange( int need, int have )
{
	int l = Inf, r = -Inf;
	fo ( k, ( int ) max( 1.0, have/( 1.2*need ) ), min( have/( 0.8*need ), 1000000.0 ) )
		if ( k*need*0.9<=have && have<=k*need*1.1 )
			l = min( k, l ), r = max( k, r );
	return PII( l, r );
	//return PII( ceil( have*9, ( need*10 ) ),/* ceil(*/ have*10/( need*11 ) );
}

PII f[N][N];
int a[N];
int n, m;

void preprocessing()
{
	map < int, int > Relab;
	int cnt; 
	scanf( "%d%d", &n, &m );
	fo ( i, 0, n ) scanf( "%d", &a[i] );
	fo ( i, 0, n ) fo ( j, 0, m )
	{
		scanf( "%d", &cnt );
		f[i][j] = getrange( a[i], cnt );
	}
}

void solve()
{
	int p[N];
	int ret = 0;
	fo ( i, 0, m ) p[i] = i;
	if ( n==2 )
	{
		do
		{
			int cnt = 0;
			fo ( i, 0, m ) 
			{
				if ( f[0][i].se<f[1][ p[i] ].fi ) continue; 
				if ( f[0][i].fi>f[1][ p[i] ].se ) continue;
				++cnt;
			}
			ret = max( ret, cnt );
		} while ( next_permutation( p, p + m ) );
	}
	else 
	{
		fo ( i, 0, m ) if ( f[0][i].fi<=f[0][i].se ) ++ret;
	}
	printf( "%d\n", ret );
}

int main()
{
	freopen( "b.in", "r", stdin );
	freopen( "b.out", "w", stdout );
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

