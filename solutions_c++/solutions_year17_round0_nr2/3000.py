#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

#define fo( i, x, y ) for ( int i=x; i<y; ++i )

LL n;

void preprocessing()
{
	cin >> n;
}

void solve()
{
	LL last = ( LL ) 1e18;
	for ( LL temp=( LL ) 1e18; temp; temp/=10 )
		if ( n/temp%10 < n/temp/10%10 )
		{
			cout << ( ( n/last-1 )*last+last-1 ) << endl;
			return;
		}
		else if ( n/temp%10 > n/temp/10%10 ) last = temp;
	cout << n << endl;
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

