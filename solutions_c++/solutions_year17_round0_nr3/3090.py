#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

#define fo( i, x, y ) for ( int i=x; i<y; ++i )

map < LL, LL > f;
LL n, m;

void preprocessing()
{
	f.clear();
	cin >> n >> m;
	f[n] = 1;
}

void solve()
{
	while ( 1 )
	{
		f.erase( val );
		LL nl = ( val-1 )/2, nr = ( val/2 );
		if ( m<=cnt ) 
		{
			if ( nl < nr ) swap( nl, nr );
			printf( "%lld %lld\n", nl, nr );
			return;
		}
		m -= cnt;
		f[nl] += cnt, f[nr] += cnt;
	}
}

int main()
{
	freopen( "c.in", "r", stdin );
	freopen( "c.out", "w", stdout );
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

