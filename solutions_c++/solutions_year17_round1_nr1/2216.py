#include <stdio.h>
#include <assert.h>


int gwidth;
int gheight;
char grid[32][32];

int maxAlphabet( int x, int y )
{
	char a = grid[y][x];
	int i;
	
	int maxleft, maxright, maxtop, maxbottom;
	int ok;
	
	maxleft = 0;
	while ( x-maxleft >= 1 ) {
		if ( grid[y][x-maxleft-1] == '?' ) {
			maxleft++;
			grid[y][x-maxleft] = a;
		} else break;
	}
	
	maxright = 0;
	while ( x+maxright+1 < gwidth ) {
		if ( grid[y][x+maxright+1] == '?' ) {
			maxright++;
			grid[y][x+maxright] = a;
		} else break;
	}
	
	maxtop = 0;
	while ( y-maxtop >= 1 ) {
		ok = 1;
		for ( i = x-maxleft; i <= x+maxright; i++ ) {
			if ( grid[y-maxtop-1][i] != '?' ) {
				ok = 0;
			}
		}
		
		if ( ok ) {
			for ( i = x-maxleft; i <= x+maxright; i++ ) {
				grid[y-maxtop-1][i] = a;
			}
			maxtop++;
		} else break;
	}
	
	maxbottom = 0;
	while ( y+maxbottom+1 < gheight ) {
		ok = 1;
		for ( i = x-maxleft; i <= x+maxright; i++ ) {
			if ( grid[y+maxbottom+1][i] != '?' ) {
				ok = 0;
			}
		}
		
		if ( ok ) {
			for ( i = x-maxleft; i <= x+maxright; i++ ) {
				grid[y+maxbottom+1][i] = a;
			}
			maxbottom++;
		} else break;
	}
	
	return 0;
}

int doSolve( int cn )
{
	scanf( " %d %d", &gheight, &gwidth );
	int i, j;

	int axlist[32];
	int aylist[32];
	int acount = 0;
	
	for ( i = 0; i < gheight; i++ ) {
		for ( j = 0; j < gwidth; j++ ) {
			scanf( " %c", &grid[i][j] );
			if ( grid[i][j] != '?' ) {
				axlist[acount] = j;
				aylist[acount] = i;
				acount++;
			}
		}
	}
	
	for ( i = 0; i < acount; i++ ) {
		maxAlphabet( axlist[i], aylist[i] );
	}
	
	printf( "Case #%d:\n", cn );
	for ( i = 0; i < gheight; i++ ) {
		for ( j = 0; j < gwidth; j++ ) {
			assert( grid[i][j] != '?' );
			printf( "%c", grid[i][j] );
		}
		printf( "\n" );
	}
	return 0;
}

int main()
{
	int cn;
	scanf( " %d", &cn );
	
	int i;
	for ( i = 0; i < cn; i++ ) {
		doSolve( i+1 );
	}
}

