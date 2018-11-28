#include <bits/stdc++.h>
using namespace std;
#define TAM		101
int dp[4][TAM][TAM][TAM];
int mod;

int f ( int x, int c1, int c2, int c3 ) {
	int& r = dp[x][c1][c2][c3];
	if ( r != -1 ) return r;

	r = 0;
	if ( c1 + c2 + c3 == 0 ) return r;
	if ( c1 ) r = max ( r, f( (x+1)%mod, c1-1, c2, c3 ) );
	if ( c2 ) r = max ( r, f( (x+2)%mod, c1, c2-1, c3 ) );
	if ( c3 ) r = max ( r, f( (x+3)%mod, c1, c2, c3-1 ) );
	r += ( x == 0 ? 1 : 0 );

	return r;
}

int main ( )
{
	freopen ( "input.txt", "r", stdin );
	freopen ( "output.txt", "w", stdout );

	int ntc;
	scanf ( "%d", &ntc );
	for ( int t = 1; t <= ntc; ++t ) {
		int n, ai;
		scanf ( "%d%d", &n, &mod );
		vector<int> c ( 4, 0 );
		while ( n-- ) {
			scanf ( "%d", &ai );
			c[ai%mod]++;
		}
		memset ( dp, -1, sizeof(dp) );
		printf ( "Case #%d: %d\n", t, c[0]+f(0,c[1],c[2],c[3]) );
	}

	return 0;
}
