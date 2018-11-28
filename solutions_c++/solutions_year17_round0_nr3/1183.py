/*
 * Author:  vawait
 * Created Time:  六  4/ 8 15:55:37 2017
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
lint n , k , ans;

void init()
{
    cin >> n >> k;
}

lint f(lint n,lint k) {
    if ( k == 1 ) return n - 1;
    n --;
    k --;
    if ( k & 1 ) return f( n - n / 2 , k / 2 + 1 );
    return f( n / 2 , k / 2 );
}

void work()
{
    lint ans = f( n , k );
    cout << ans - ans / 2 << " " << ans/2 << endl;
}

int main()
{
    freopen("a.in","r",stdin);
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
