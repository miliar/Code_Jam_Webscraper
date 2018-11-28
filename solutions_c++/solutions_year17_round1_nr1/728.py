/*
 */
#include <cassert>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <queue>
#include <vector>
#include <map>
#include <set>
#define L(k) ((k)&((~(k))+1))
#define oo (0xfffffffful)
#define BIT(k) (1ULL<<(k))
#define MASK(k) (BIT(k)-1ULL)
using namespace std;
typedef long long i64;
typedef unsigned long long u64;
#define N 32

char which[1<<20];
int who( u64 u ) {
	if ( u < BIT(20) )
		return which[u];
	if ( u < BIT(40) )
		return 20+which[u>>20];
	if ( u < BIT(60) )
		return 40+which[u>>40];
	return 60+which[u>>60];
}

int m,n;
char g[N][N];

int is_empty( char *c ) {
	int j;
	for ( j = 0; j < n; ++j )
		if ( c[j] != '?' ) return 0;
	return 1;
}

int next_pos( int row, int j0 ) {
	for ( int j = j0; j < n; ++j )
		if ( g[row][j] != '?' ) return j;
	return n;
}

void fill( int x0, int y0, int x1, int y1, char ch ) {
	if ( x0 > x1 || y0 > y1 ) return ;
	for ( int i = x0; i <= x1; ++i )
		for ( int j = y0; j <= y1; ++j )
			g[i][j] = ch;
}

char from_upwards( int i, int j ) {
	for ( int k = i; k >= 0; --k )
		if ( g[k][j] != '?' )
			return g[k][j];
	return '\0';
}

int main() {
	int i,j,k,t,ts,cs = 0,jprev,iprev;
	for ( i = 0; i < 20; which[1<<i] = i, ++i ) ;
	for ( scanf("%d",&ts); ts-->0; ) {
		printf("Case #%d:\n",++cs);
		scanf("%d %d",&m,&n);
		for ( i = 0; i < m; ++i )
			scanf("%s",g[i]);
		iprev = -1;
		do {
			for ( i = iprev+1; i < m; ++i )
				if ( !is_empty(g[i]) ) break ;
			if ( i == m ) {
				for ( t = iprev+1; t < m; ++t ) 
					for ( k = 0; k < n; ++k ) {
						g[t][k] = from_upwards(t,k);
						assert( g[t][k] != '\0' );
					}
				break ;
			}
			jprev = -1;
			do {
				j = next_pos(i,jprev+1);
				if ( j < n ) {
					fill(iprev+1,jprev+1,i,j,g[i][j]);
					jprev = j;
				}
				else {
					assert( j == n );
					assert( jprev >= 0 && g[i][jprev] != '?' );
					fill(iprev+1,jprev+1,i,n-1,g[i][jprev]);
				}
			} while ( j != n );
			iprev = i;
		} while ( 1 );

		for ( i = 0; i < m; ++i )
			printf("%s\n",g[i]);
	}
	return 0;
}

