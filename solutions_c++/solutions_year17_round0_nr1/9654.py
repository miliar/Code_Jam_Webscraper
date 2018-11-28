#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1005;

char S[ N ];
int k;
int tp = 0;

void load( ) {
	scanf( "%s%d", S, &k );
}

void solve( ) {
	int sol = 0;
	printf( "Case #%d: ", ++tp );
	int n = strlen( S );
	for( int i = 0; i < n; i++ ) {
		if( S[ i ] == '-' ) {
			sol++;
			if( i + k - 1 >= n ) {
				printf( "IMPOSSIBLE\n" );
				return;
			}
			for( int j = i; j < i + k; j++ ) {
				if( S[ j ] == '-' ) S[ j ] = '+';
				else S[ j ] = '-';
			}
		}
	}
	for( int i = 0; i < n; i++ ) {
		if( S[ i ] == '-' ) {
			printf( "IMPOSSIBLE\n" );
			return;
		}
	}
	printf( "%d\n", sol );
}

int main( void ) {
	int t;
	scanf( "%d", &t );
	while( t-- ) {
		load( );
		solve( );
	}
	return 0;
}
