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

const int maxn = 1005;
const int inf = 2e9;
const ld eps = 1e-9;
const int base = 1073676287;

vector < char > ans;

void solution( int case1 ) {
	int n, r, o, y, g, b, v;
	scanf ( "%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v );

	if ( o + b == n ) {
		if ( o != b ) {
			printf ( "Case #%d: IMPOSSIBLE\n", case1 );
			return;
		}
		printf ( "Case #%d: ", case1 );
		for ( int j = 0; j < n; j++ )
			printf ( "%c", ( j & 1 ) ? 'O' : 'B' );
		printf ( "\n" );
		return;
	}
	if ( o >= b && o ) {
		printf ( "Case #%d: IMPOSSIBLE\n", case1 );
		return;
	}

	if ( g + r == n ) {
		if ( g != r ) {
			printf ( "Case #%d: IMPOSSIBLE\n", case1 );
			return;
		}
		printf ( "Case #%d: ", case1 );
		for ( int j = 0; j < n; j++ )
			printf ( "%c", ( j & 1 ) ? 'G' : 'R' );
		printf ( "\n" );
		return;
	}
	if ( g >= r && g ) {
		printf ( "Case #%d: IMPOSSIBLE\n", case1 );
		return;
	}

	if ( v + y == n ) {
		if ( v != y ) {
			printf ( "Case #%d: IMPOSSIBLE\n", case1 );
			return;
		}
		printf ( "Case #%d: ", case1 );
		for ( int j = 0; j < n; j++ )
			printf ( "%c", ( j & 1 ) ? 'V' : 'Y' );
		printf ( "\n" );
		return;
	}
	if ( v >= y && v ) {
		printf ( "Case #%d: IMPOSSIBLE\n", case1 );
		return;
	}

	r -= g;
	y -= v;
	b -= o;

	ans.clear();
	int last = -1;
	if ( r >= y && r >= b ) {
		ans.pb( 'R' );
		--r;
		last = 'R';
	} else
		if ( y >= r && y >= b ) {
			ans.pb( 'Y' );
			--y;
			last = 'Y';
		} else
			if ( b >= y && b >= r ) {
				ans.pb( 'B' );
				--b;
				last = 'B';
			}
	while ( r + y + b > 2 ) {
		if ( last == 'R' ) {
			if ( y > b ) {
				--y;
				ans.pb( 'Y' );
				last = 'Y';
			} else {
				--b;
				ans.pb( 'B' );
				last = 'B';
			}
			continue;
		}

		if ( last == 'Y' ) {
			if ( r > b ) {
				--r;
				ans.pb( 'R' );
				last = 'R';
			} else {
				--b;
				ans.pb( 'B' );
				last = 'B';
			}
			continue;
		}

		if ( last == 'B' ) {
			if ( y > r ) {
				--y;
				ans.pb( 'Y' );
				last = 'Y';
			} else {
				--r;
				ans.pb( 'R' );
				last = 'R';
			}
			continue;
		}
	}
	if ( r == 2 || y == 2 || b == 2 ) {
		printf ( "Case #%d: IMPOSSIBLE\n", case1 );
		return;
	}
	if ( r < 0 || y < 0 || b < 0 ) {
		printf ( "Case #%d: IMPOSSIBLE\n", case1 );
		return;
	}


	if ( !r ) {
		ans.pb( 'Y' );
		ans.pb( 'B' );
		int sz = ans.size();
		if ( ans[sz - 1] == ans[0] || ans[sz - 2] == ans[sz - 3] )
			swap( ans[sz - 1], ans[sz - 2] );
		if ( ans[sz - 1] == ans[0] || ans[sz - 2] == ans[sz - 3] ) {
			printf ( "Case #%d: IMPOSSIBLE\n", case1 );
			return;
		}
	} 

	if ( !y ) {
		ans.pb( 'R' );
		ans.pb( 'B' );
		int sz = ans.size();
		if ( ans[sz - 1] == ans[0] || ans[sz - 2] == ans[sz - 3] )
			swap( ans[sz - 1], ans[sz - 2] );
		if ( ans[sz - 1] == ans[0] || ans[sz - 2] == ans[sz - 3] ) {
			printf ( "Case #%d: IMPOSSIBLE\n", case1 );
			return;
		}
	} 

	if ( !b ) {
		ans.pb( 'R' );
		ans.pb( 'Y' );
		int sz = ans.size();
		if ( ans[sz - 1] == ans[0] || ans[sz - 2] == ans[sz - 3] )
			swap( ans[sz - 1], ans[sz - 2] );
		if ( ans[sz - 1] == ans[0] || ans[sz - 2] == ans[sz - 3] ) {
			printf ( "Case #%d: IMPOSSIBLE\n", case1 );
			return;
		}
	} 

	bool orange = false;
	bool green = false;
	bool violet = false;

	printf ( "Case #%d: ", case1 );
	int sz = ans.size();
	for ( int j = 0; j < sz; j++ ) {
		printf ( "%c", ans[j] );
		if ( ans[j] == 'R' && !green ) {
			green = true;
			while ( g-- )
				printf ( "GR" );
		} 
		if ( ans[j] == 'Y' && !violet ) {
			violet = true;
			while ( v-- )
				printf ( "VY" );
		} 
		if ( ans[j] == 'B' && !orange ) {
			orange = true;
			while ( o-- )
				printf ( "OB" );
		} 
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
