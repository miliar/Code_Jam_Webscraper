#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

#define fo( i, x, y ) for ( int i=x; i<y; ++i )

map < LL, LL > f;
LL n, m;

void change( LL &A, LL &B )
{
	LL temp = A;
	A = B, B = temp;
}

void preprocessing()
{
	f.clear();
	cin >> n >> m;
	f[n] = 1;
}

bool split( LL val, LL cnt )
{
	LL nl = ( val-1 )/2, nr = ( val/2 );
	if ( m<=cnt ) 
	{
		if ( nl < nr ) change( nl, nr );
		cout << nl << " " << nr << endl;
		return 1;
	}
	f[nl] += cnt, f[nr] += cnt, m -= cnt;
	return 0;
}

void solve()
{
	LL val, cnt;
	do 
	{
		val = ( f.rbegin() )->first; 
		cnt = ( f.rbegin() )->second;
		f.erase( val ); 
	}
	while ( !split( val, cnt ) );
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
		cout << "Case #" << ( Case+1 ) << ": ";
		solve();
	}
	return 0;
}

