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

int a[maxn];

void solve( int num ) {
	cout << "Case #" << num << ": ";
	string c;
	int n, k;
	cin >> c >> k;
	n = c.size();

	for ( int j = 0; j < n; j++ )
		a[j] = c[j] == '+';
	int ans = 0;
	for ( int j = 0; j < n - k + 1; j++ ) {
		if ( a[j] )
			continue;
		for ( int i = j; i < j + k; i++ )
			a[i] ^= 1;
		++ans;
	}
	for ( int j = 0; j < n; j++ )
		if ( !a[j] ) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
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
