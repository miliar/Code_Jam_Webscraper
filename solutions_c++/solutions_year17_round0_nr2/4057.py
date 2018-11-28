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

const int maxn = 100500;
const int inf = 2e9;
const double eps = 1e-8;
const int base = 1073676287;

vector < int > a;

void solve( int num ) {
	ll x;
	cin >> x;
	ll X = x;
	cout << "Case #" << num << ": ";
	a.clear();
	while ( x ) {
		a.pb( x % 10 );
		x /= 10;
	}
	reverse( a.begin(), a.end() );
	ll ans = 0;
	int sz = a.size();
	// for ( int j = 1; j < sz; j++ ) {
	// 	ans *= 10LL;
	// 	ans += 9LL;
	// }
	for ( int j = 0; j <= sz; j++ ) {
		bool correct = true;
		for ( int i = 0; i < j - 1; i++ )
			if ( a[i] > a[i + 1] )
				correct = false;
		if ( !correct )
			continue;
		ll curAns = 0;
		for ( int i = 0; i < j; i++ ) {
			curAns *= 10LL;
			curAns += 1LL * a[i];
		}
		if ( j == sz ) {
			ans = max( ans, curAns );
			continue;
		}
		int prev = j ? a[j - 1] : -1;
		if ( a[j] - 1 >= prev ) {
			curAns *= 10LL;
			curAns += a[j] - 1;
			for ( int i = j + 1; i < sz; i++ ) {
				curAns *= 10LL;
				curAns += 9LL;
			}
			ans = max( curAns, ans );
		}
	}
	assert( ans <= X );
	cout << ans << endl;
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
