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

const int maxn = 1000500;
const int inf = 2e9;
const double eps = 1e-8;
const int base = 1073676287;

set < pair < int, int > > a[maxn];

void solve( int num ) {
	for ( int j = 0; j < maxn; j++ )
		a[j].clear();
	int k, n;
	cin >> n >> k;
	cout << "Case #" << num << ": ";
	a[n].insert( mp( 1, n ) );
	int len = n;
	int ans = -1;
	pair < int, int > cnt;
	for ( int j = 0; j < k; j++ ) {
		while ( a[len].empty() )
			--len;
		pair < int, int > cur = *a[len].begin();
		a[len].erase( a[len].begin() );
		ans = ( len - 1 ) / 2 + cur.f;
		int lenL = ( len - 1 ) / 2;
		a[lenL].insert( mp( cur.f, ans - 1 ) );
		int lenR = len / 2;
		a[lenR].insert( mp( ans + 1, cur.s ) );
		cnt = mp( max( lenL, lenR ), min( lenL, lenR ) );
	}
	assert( ans != -1 );
	cout << cnt.f << ' ' << cnt.s << endl;
}

int main()
{
    srand( time( 0 ) );
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
    // ios_base::sync_with_stdio(false);
    int q;
    cin >> q;
    for ( int j = 1; j <= q; j++ )
    	solve( j );
    return 0;
}
