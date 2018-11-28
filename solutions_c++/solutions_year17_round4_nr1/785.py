/*
 * Author:  vawait
 * Created Time:  六  5/13 22:14:54 2017
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
int n, p, a[10], s, ans;

void init()
{
    int x;
    clr( a , 0 );
    cin >> n >> p;
    rep(i,1,n) {
        cin >> x;
        a[x%p] ++;
    }
}

void add(int t) {
    if ( !s ) ans ++;
    s += t;
    s %= p;
}

void work()
{
    ans = a[0];
    rep(i,1,3) if ( i * 2 == p ) {
        ans += a[i] / 2;
        a[i] %= 2;
    }
    rep(i,1,3)
        rep(j,i+1,3) if ( i + j  == p ) {
            int x = min( a[i], a[j] );
            ans += x;
            a[i] -= x;
            a[j] -= x;
        }
    s = 0;
    while ( a[2] ) add( 2 ), a[2] --;
    red(i,p,1) while ( a[i] ) add( i ) , --a[i];
    cout << ans << endl;
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
