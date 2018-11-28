#include <bits/stdc++.h>
using namespace std;

typedef pair< int, int > PII;
typedef long long LL;
typedef double db;

const double pi = acos( -1 );
const LL lInf = ( LL ) 1E16;
const int Inf = 0x23333333;
const int N = 1005;

#define foi( i, x ) for ( auto i=x.begin(); i!=x.end(); ++i )
#define pub( x ) push_back( x )
#define mkp( A, B ) make_pair( A, B )
#define fo( i, x, y ) for ( int i=x; i<y; ++i )
#define fi first
#define se second

PII a[N];
int n, m;

bool cmp( const PII &A, const PII &B )
{
	return ( LL ) A.fi*A.se > ( LL ) B.fi*B.se;
}

void preprocessing()
{
	scanf( "%d%d", &n, &m );
	fo ( i, 0, n ) scanf( "%d%d", &a[i].fi, &a[i].se );
	sort( a, a + n, cmp );
}

void solve()
{
	LL ret = 0;
	fo ( i, 0, n ) 
	{
		LL sum = 0;
		int cnt = 0;
		fo ( j, 0, n ) if ( j!=i && a[j].fi<=a[i].fi && cnt<m-1 )
			++cnt, sum += 2LL*a[j].fi*a[j].se;
		sum += 2LL * a[i].fi * a[i].se;
		ret = max( ret, sum + ( LL ) a[i].fi*a[i].fi );
	}
	printf( "%.10lf\n", ret*pi );
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

