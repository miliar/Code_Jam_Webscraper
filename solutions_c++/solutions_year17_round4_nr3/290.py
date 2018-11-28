#include <bits/stdc++.h>
using namespace std;
#define TAM		51
#define M		(1<<5)

int R, C;
char G[TAM][TAM];
bool canH[TAM][TAM], canV[TAM][TAM];
int dp[M][M][TAM];

bool can ( int i, int j, int di, int dj ) {
	if ( i < 0 || j < 0 || i >= R || j >= C ) return true;
	if ( G[i][j] == '#' ) return true;
	if ( G[i][j] == '.' ) return can(i+di, j+dj, di, dj );
	return false;
}

int calcNeeded ( int col, int mask, int lasered ) {
	int r = 0;
    for ( int i = 0, x; i < R; ++i )
		if ( G[i][col] == '.' ) {
			if ( (lasered>>i)&1 ) continue;
			for ( x = i; x >= 0 && G[x][col] == '.'; x-- );
			if ( x >= 0 && ((mask>>x)&1) ) continue;
			for ( x = i; x < R && G[x][col] == '.'; x++ );
			if ( x < R && ((mask>>x)&1) ) continue;
			r |= (1<<i);
		}
	return r;
}

int bin ( int x ) {
	return (x>>4)*10000 + ((x>>3)&1)*1000 + 100*((x>>2)&1) +10*((x>>1)&1)+ (x&1);
}

bool f ( int needed, int lasered, int col ) {
	int& r = dp[needed][lasered][col];
	if ( r != -1 ) return r;
	if ( col == C ) return r = ( needed == 0 );
	r = 0;

	for ( int m = 0; m < (1<<R); ++m )
	{
		//printf ( "f(%05d,%05d,%d) m=%d\n", bin(needed), bin(lasered), col, m );
		bool ok = true;
		for ( int i = 0; i < R; ++i )
			if ( (m>>i)&1 ) ok &= canV[i][col];
			else ok &= canH[i][col];
		if ( !ok ) continue;

		int maskCol = 0, newNeeded = needed, newLasered = lasered;
		for ( int i = 0; i < R; ++i ) {
			if ( G[i][col] == '#' ) {
				ok &= ((needed>>i)&1) == 0;
				if ( (lasered>>i)&1 ) newLasered -= (1<<i);
			}
			else if ( G[i][col] == '.' ) { }
			else {
				if ( (m>>i)&1 ) {
					G[i][col] = '|';
					maskCol += (1<<i);
				}
				else {
					G[i][col] = '-';
					newLasered |= (1<<i);
					if ( (needed>>i)&1 ) newNeeded -= 1<<i;
				}
			}
		}
		if ( ok && f ( newNeeded | calcNeeded(col, maskCol, newLasered), newLasered, col+1 ) )
			return r = 1;
	}

	return r;
}

int main ( )
{
	freopen ( "input.txt", "r", stdin );
	freopen ( "output.txt", "w", stdout );

	int ntc;
	scanf ( "%d", &ntc );
	for ( int t = 1; t <= ntc; ++t ) {
		scanf ( "%d%d", &R, &C );
        for ( int i = 0; i < R; ++i )
			scanf ( "%s", G[i] );
		memset ( dp, -1, sizeof(dp) );

		for ( int i = 0; i < R; ++i )
			for ( int j = 0; j < C; ++j )
				if ( G[i][j] == '-' || G[i][j] == '|' ) {
					canV[i][j] = can(i-1,j,-1,0) && can(i+1,j,1,0);
					canH[i][j] = can(i,j-1,0,-1) && can(i,j+1,0,1);
				}
				else
					canV[i][j] = canH[i][j] = true;

		bool r = f(0,0,0);
		printf ( "Case #%d: %s\n", t, r ? "POSSIBLE" : "IMPOSSIBLE" );
		if ( r ) {
			for ( int i = 0; i < R; ++i )
				printf ( "%s\n", G[i] );
		}
	}

	return 0;
}
