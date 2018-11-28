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

const int maxn = 1050;
const int inf = 2e9;
const double eps = 1e-8;
const int base = 1073676287;


vector < int > position[maxn];
int cnt[maxn];
set < int > passengers[maxn];
//set < int > emptyBusses[maxn];
map < int, int > Free[maxn];
map < int, int >::iterator it;
int used[maxn][maxn];
int timer;

//int calc( int n, int c, int mid, int id ) {
//    for ( int j = 0; j < maxn; j++ ) {
//        passengers[j].clear();
//        Free[j].clear();
////        emptyBusses.clear();
//    }
////    for ( int j = 1; j <= c; j++ )
////        for ( int i = 0; i < mid; i++ )
////            emptyBusses[j].insert( i );
//    int ans = 0;
//    for ( int j = 1; j <= c; j++ ) {
//        int sz = position[j].size();
//        int it = 0;
//        for ( int i = 0; i < sz; i++ ) {
//            int seat = position[j][i];
//            while ( it < mid && used[it][seat] == id )
//                ++it;
//            if ( it != mid ) {
//                used[it][seat] = id;
//                passengers[it].insert( j );
//                ++it;
////                emptyBusses[j].erase( it );
//            } else {
//                ++Free[seat][j];
//                ++ans;
//            }
//        }
//    }
//    for ( int j = n; j >= 1; j-- )
//        for ( it = Free[j].begin(); it != Free[j].end(); it++ ) {
//            int idPerson = it -> f;
//            int cnt = it -> s;
//            if ( !cnt )
//                continue;
//            for ( int i = 0; i < mid && cnt; i++ ) {
//                if ( used[i][j] == id )
//                    continue;
//                if ( passengers[i].find( idPerson ) != passengers[i].end() )
//                    continue;
//                used[i][j] = id;
//                passengers[i].insert( idPerson );
//                --cnt;
//            }
//            Free[j - 1][idPerson] += cnt;
//        }
//    for ( it = Free[0].begin(); it != Free[0].end(); it++ )
//        if ( it -> s )
//            return inf;
//    return ans;
//}

void solve( int id ) {
    for ( int j = 0; j < maxn; j++ ) {
        position[j].clear();
        cnt[j] = 0;
    }
    int n, c, m;
    scanf ( "%d%d%d", &n, &c, &m );
    for ( int j = 0; j < m; j++ ) {
        int x, y;
        scanf ( "%d%d", &x, &y );
        ++cnt[x];
        position[y].pb( x );
    }
    int ans = 0;
    for ( int j = 1; j <= c; j++ )
        ans = max( ans, (int) position[j].size() );
    int sum = 0;
    for ( int i = 1; i <= n; i++ ) {
        sum += cnt[i - 1];
        ans = max( ans, ( sum + cnt[i] + i - 1 ) / i );
    }
    if ( n * ans < m )
        ans = ( m + n - 1 ) / n;
    int anotherAns = 0;
    for ( int j = 1; j <= n; j++ )
        anotherAns += max( 0, cnt[j] - ans );
    printf ( "Case #%d: %d %d\n", id, ans, anotherAns );
//    int l = 1;
//    int r = m;
//    while ( r - l ) {
//        int mid = ( l + r ) >> 1;
//        if ( calc( n, c, mid, ++timer ) != inf )
//            r = mid;
//        else
//            l = mid + 1;
//    }
//    printf ( "Case #%d: %d %d\n", id, l, calc( n, c, l, ++timer ) );
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
