#include <bits/stdc++.h>
using namespace std;

typedef pair< int, int > PII;
typedef long long LL;
typedef double db;

const LL lInf = ( LL ) 1E16;
const int Inf = 0x23333333;
const int N = 405, M = 725;

#define foi( i, x ) for ( auto i=x.begin(); i!=x.end(); ++i )
#define pub( x ) push_back( x )
#define mkp( A, B ) make_pair( A, B )
#define fo( i, x, y ) for ( int i=x; i<y; ++i )
#define fi first
#define se second

int n, m, p;
int f[N][M][2];
PII a[N];

void update( int &A, int B ) { if ( B < A ) A = B; }

void preprocessing()
{
	fill( a, a + N, mkp( 0, 0 ) );
	int l, r;
	PII A[N], B[N];
	scanf( "%d%d", &n, &m ), p = 0;
	fo ( i, 0, n ) scanf( "%d%d", &A[i].fi, &A[i].se );
	fo ( i, 0, m ) scanf( "%d%d", &B[i].fi, &B[i].se );
	sort( A, A + n ), sort( B, B + m );
	a[ p++ ] = mkp( 0, 2 );
	for ( int i=0, j=0; i<n || j<m; )
	{
		int flag = 0;
		if ( i==n || j<m && B[j].fi < A[i].fi ) 
			l = B[j].fi, r = B[j].se, ++j, flag = 1;
		else l = A[i].fi, r = A[i].se, ++i;
		if ( a[ p-1 ].fi==l ) a[ p-1 ].se = flag;
		else a[ p++ ] = mkp( l, flag );
		a[ p++ ] = mkp( r, 2 );
	}
	if ( a[ p-1 ].fi!=1440 ) a[ p++ ] = mkp( 1440, 2 );
	n = p;
}

void solve()
{
	int ret = Inf;
	fo ( bG, 0, 2 )
	{
		fill( f[0][0], f[n][0], Inf );
		f[0][0][bG] = 0;
		fo ( i, 0, n-1 ) 
		{
			int temp = 0;
			fo ( j, 0, 721 ) fo ( last, 0, 2 )
			{
				if ( f[i][j][last]==Inf ) continue;
				int usedA = a[i].fi - j, usedB = j;
				int rem[2] = { 720 - usedA, 720 - usedB };
				int len = a[ i+1 ].fi - a[i].fi, ano = last ^ 1;
				if ( a[i].se<2 ) 
				{
					int p = a[i].se ^ 1;
					if ( len>rem[p] ) continue;
					update( f[ i+1 ][ j+p*len ][p], f[i][j][last] + ( last!=p ) );
					continue;
				}
				fo ( k, 0, 2 ) if ( len<=rem[k] )
					update( f[ i+1 ][ j+k*len ][k], f[i][j][last] + ( last!=k ) );
				fo ( k, a[i].fi+1, a[ i+1 ].fi ) 
				{
					int l1 = k - a[i].fi, l2 = a[ i+1 ].fi - k;
					if ( l1<=rem[last] && l2<=rem[ano] )
						update( f[ i+1 ][ j+last*l1+ano*l2 ][ano], f[i][j][last] + 1 ); // AAA|AABBB|
					if ( l1<=rem[ano] && l2<=rem[last] )
						update( f[ i+1 ][ j+ano*l1+last*l2 ][last], f[i][j][last] + 2 ); // AAA|BBAAA|
				}
			}
		}
		ret = min( ret, min( f[ n-1 ][720][0]+( bG ), f[ n-1 ][720][1]+( !bG ) ) );
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

