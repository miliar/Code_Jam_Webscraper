/*
 * Author:  vawait
 * Created Time:  六  5/13 22:40:32 2017
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
const int maxn = 10100;
int l, n, m, sum[maxn], t[maxn];

void init()
{
    int x, y;
    clr( sum , 0 );
    clr( t , 0 );
    cin >> l >> n >> m;
    rep(i,1,m) {
        cin >> x >> y;
        t[y] ++;
        sum[x] ++;
    }
}

int calc(int x,int y) {
    return ( x + y - 1 ) / y;
}

void work()
{
    int ans1 = 1, ans2 = 0, c = n, s = 0;
    rep(i,1,n) ans1 = max( ans1, t[i] );
    rep(i,1,n) if ( t[i] ) c += t[i] - 1;
    ans1 = max( ans1, c / l );
    rep(i,1,l) {
        s += sum[i];
        ans1 = max( ans1, calc( s , i ) );
    }
    rep(i,1,l) {
        if ( sum[i] > ans1 ) ans2 += sum[i] - ans1;
    }
    cout << ans1 << " " << ans2 << endl;
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
