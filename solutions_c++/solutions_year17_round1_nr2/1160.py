/*
 * Author:  vawait
 * Created Time:  六  4/15 10:43:49 2017
 * File Name: a.cpp
 */
#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<stack>
using namespace std;
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define red(i, a, b) for (int i = (a); i >= (b); --i)
#define clr( x , y ) memset(x,y,sizeof(x))
#define sqr(x) ((x) * (x))
#define mp make_pair
#define pb push_back
#define db pop_back
typedef long long lint;
const int maxn = 1100;
int n , m , R[maxn] , a[maxn][maxn], p[maxn] , b[maxn];

void init()
{
    scanf("%d%d",&n,&m);
    rep(i,1,n) scanf("%d",&R[i]);
    rep(i,1,n) {
        rep(j,1,m) scanf("%d",&a[i][j]);
        sort( a[i] + 1 , a[i] + m + 1 );
        p[i] = 1;
    }
}

int ok() {
    int min = 1e7 , p = 0 , l = 0 , r = 1e7;
    int mi , mx;
    rep(i,1,n) {
        mx = b[i] / ( R[i] * 0.9 );
        if ( mx < min ) min = mx , p = i;
        if ( mx < r ) r = mx;
        mi = int( b[i] / ( R[i] * 1.1 ) + 0.99 );
        if ( mi > l ) l = mi;
        //printf("%d %d\n",mx,mi);
    }
    if ( l <= r ) return 0;
    return p;
}

void work()
{
    int ans = 0 , x;
    while ( 1 ) {
        rep(i,1,n) b[i] = a[i][p[i]];
        x = ok();
        if ( !x ) {
            ans ++;
            rep(i,1,n) p[i] ++;
        } else p[x] ++;
        int vis = 0;
        rep(i,1,n) if ( p[i] > m ) vis = 1;
        if ( vis ) break;
    }
    printf("%d\n",ans);
}

int main()
{
    freopen("a.out","w",stdout);
    int t;
    cin >> t;
    rep(i,1,t) {
        printf("Case #%d: ",i);
        init();
        work();
    }
    return 0;
}
