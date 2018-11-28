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


using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#define f first
#define s second
#define pb push_back
#define mp make_pair

const int maxn = 100500;
const int inf = 2e9;
const double eps = 1e-8;
const int base = 1073676287;

void solution( int case1 ) {
	int d, n;
	scanf ( "%d%d", &d, &n );
	ld ans = 1.0L * inf * inf * inf;
	for ( int j = 0; j < n; j++ ) {
		int k, speed;
		scanf ( "%d%d", &k, &speed );
		ld t = 1.0L * ( d - k ) / speed;
		ans = min( ans, 1.0L * d / t );
	}
	printf ( "Case #%d: %.15lf\n", case1, (double)ans );
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
