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

const int maxn = 105;
const int inf = 2e9;
const double eps = 1e-8;
const int base = 1073676287;

vector < int > all;

int dp[maxn][maxn][maxn][4];

void solve( int id ) {
    int n, p;
    scanf ( "%d%d", &n, &p );
    all.clear();
    int ans = 0;
    for ( int j = 0; j < n; j++ ) {
        int x;
        scanf ( "%d", &x );
        if ( x % p == 0 )
            ++ans;
        else {
            all.pb( x );
        }
    }
    n = all.size();
    for ( int j = 0; j < maxn; j++ )
        for ( int i = 0; i < maxn; i++ )
            for ( int y = 0; y < maxn; y++ )
                for ( int e = 0; e < 4; e++ )
                    dp[j][i][y][e] = -inf;
    dp[0][0][0][0] = 0;
    for ( int j = 0; j < n; j++ )
        for ( int i = 0; i < n; i++ )
            for ( int y = 0; y <= j - i; y++ ) {
                dp[j + 1][i + 1][y][1] = max( dp[j + 1][i + 1][y][1], 1 + dp[j][i][y][0] );
                dp[j + 1][i][y + 1][2] = max( dp[j + 1][i][y + 1][2], 1 + dp[j][i][y][0] );
                dp[j + 1][i][y][3] = max( dp[j + 1][i][y][3], 1 + dp[j][i][y][0] );

                for ( int e = 1; e < p; e++ ) {
                    dp[j + 1][i + 1][y][( 1 + e ) % p] = max( dp[j + 1][i + 1][y][( 1 + e ) % p], dp[j][i][y][e] );
                    dp[j + 1][i][y + 1][( 2 + e ) % p] = max( dp[j + 1][i][y + 1][( 2 + e ) % p], dp[j][i][y][e] );
                    dp[j + 1][i][y][( 3 + e ) % p] = max( dp[j + 1][i][y][( 3 + e ) % p], dp[j][i][y][e] );
                }
            }
    int cnt1 = 0;
    int cnt2 = 0;
    for ( int j = 0; j < n; j++ ) {
        if ( all[j] % p == 1 )
            ++cnt1;
        if ( all[j] % p == 2 )
            ++cnt2;
    }
    ans += max( max( dp[n][cnt1][cnt2][0], dp[n][cnt1][cnt2][1] ), max( dp[n][cnt1][cnt2][2], dp[n][cnt1][cnt2][3] ) );
    printf ( "Case #%d: %d\n", id, ans );
}

int main()
{
    srand( time( 0 ) );
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
//    ios_base::sync_with_stdio(false);
    int q;
    scanf ( "%d", &q );
    for ( int j = 1; j <= q; j++ )
        solve( j );
    return 0;
}
