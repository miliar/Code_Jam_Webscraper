#include <cstring>
#include <string>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <cmath>
#include <cstdlib>
using namespace std;
#define foreach(i, c) for (__typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)

int R, C;
char grid[30][30];
int rootR;

void fillG( int i, int j, char l ) {
	grid[i][j] = l;
	if ( j > 0 ) {
		if ( grid[i][j-1] == '?' ) {
			fillG( i, j-1, l );
		}
	}
	if ( j < C ) {
		if ( grid[i][j+1] == '?' ) {
			fillG( i, j+1, l );
		}
	}
	return;
}

void fillR( int i, int root ) {
	for (size_t j = 0; j < C; j++) {
		grid[i][j] = grid[rootR][j];
	}
	if ( i > 0 ) {
		if ( grid[i-1][0] == '?' ) {
			fillR( i-1, false );
		}
	}
	if ( i < R ) {
		if ( grid[i+1][0] == '?' ) {
			fillR( i+1, false );
		}
	}
	return;
}

void work()
{
    // Code here
		scanf("%d %d\n", &R, &C);
		for (size_t i = 0; i < R; i++) {
			char tmp;
			for (size_t j = 0; j < C; j++) {
				scanf("%c", &tmp);
				grid[i][j] = tmp;
			}
			scanf("\n");
		}

		// fill by row
		for (size_t i = 0; i < R; i++) {
			for (size_t j = 0; j < C; j++) {
				if ( grid[i][j] != '?' ) {
					char asd = grid[i][j];
					fillG( i, j, asd );
				}
			}
		}

		for (size_t i = 0; i < R; i++) {
			if ( grid[i][0] != '?' ) {
				rootR = i;
				fillR( i, true );
			}
		}

		printf("\n");
		for (size_t i = 0; i < R; i++) {
			for (size_t j = 0; j < C; j++) {
				printf("%c", grid[i][j]);
			}
			printf("\n");
		}

}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int cs = 1; cs <= t; cs++)
    {
        printf("Case #%d: ", cs);
        work();
    }

    return 0;
}
