#include <iostream>
#include <fstream>
#include <list>
#include <stack>
#include <deque>
#include <utility>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>
#include <iomanip>
#include <ctime>
#include <iterator>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>


using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#define f first
#define s second
#define pb push_back
#define mp make_pair

const int maxn = 105;
const int inf = 2e9;
const ld eps = 1e-9;
const int base = 1073676287;

pair < int, int > a[maxn];
int dist[maxn][maxn];
int inQueue[maxn][maxn];

pair < ld, int > dp[maxn][maxn];
queue < pair < int, int > > forB;

void update( int v, int horse, ld newTime, int leftDist ) {
	assert( leftDist >= 0 );
	if ( dp[v][horse].f > newTime ) {
		dp[v][horse] = mp( newTime, leftDist );
		if ( !inQueue[v][horse] ) {
			++inQueue[v][horse];
			forB.push( mp( v, horse ) );
		}
		return;
	}
	if ( ( dp[v][horse].f - newTime ) < eps && dp[v][horse].s < leftDist ) {
		dp[v][horse] = mp( newTime, leftDist );
		if ( !inQueue[v][horse] ) {
			++inQueue[v][horse];
			forB.push( mp( v, horse ) );
		}
		return;
	}
}

ld calc( int u, int v, int n ) {
	for ( int j = 0; j < maxn; j++ )
		for ( int i = 0; i < maxn; i++ ) {
			dp[j][i] = mp( 1.0L * inf * inf * inf, 0 );
			inQueue[j][i] = 0;
		}
	dp[u][u] = mp( 0, a[u].f );
	++inQueue[u][u];
	forB.push( mp( u, u ) );
	while ( !forB.empty() ) {
		pair < int, int > cur = forB.front();
		int curV = cur.f;
		int curH = cur.s;
		--inQueue[curV][curH];
		int canMove = dp[curV][curH].s;
		ld curTime = dp[curV][curH].f;
		forB.pop();
		for ( int j = 1; j <= n; j++ ) {
			if ( dist[curV][j] == -1 )
				continue;
			if ( dist[curV][j] <= a[curV].f )
				update( j, curV, curTime + 1.0L * dist[curV][j] / a[curV].s,
					a[curV].f - dist[curV][j] );
			if ( dist[curV][j] <= canMove )
				update( j, curH, curTime + 1.0L * dist[curV][j] / a[curH].s,
					canMove - dist[curV][j] );
		}
	}
 	ld ans = 1.0L * inf * inf * inf;
 	for ( int j = 1; j <= n; j++ )
 		ans = min( ans, dp[v][j].f );
 	return ans;
}

void solution( int case1 ) {
	int n, q;
	scanf ( "%d%d", &n, &q );
	for ( int j = 1; j <= n; j++ )
		scanf ( "%d%d", &a[j].f, &a[j].s );
	for ( int j = 1; j <= n; j++ )
		for ( int i = 1; i <= n; i++ )
			scanf ( "%d", &dist[j][i] );
	printf ( "Case #%d:", case1 );
	while ( q-- ) {
		int u, v;
		scanf ( "%d%d", &u, &v );
		printf ( " %.15lf", (double)calc( u, v, n ) );
	}
	printf ( "\n" );
}

int main()
{
    srand( time( 0 ) );
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
    // ios_base::sync_with_stdio(false);
    int q;
    scanf ( "%d", &q );
    for ( int j = 1; j <= q; j++ )
    	solution( j );
    return 0;
}
