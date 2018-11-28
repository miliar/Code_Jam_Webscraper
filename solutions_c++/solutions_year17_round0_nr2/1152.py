/*
 * Author:  vawait
 * Created Time:  六  4/ 8 16:22:29 2017
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
lint n , a[40] , b[40];

void init()
{
    clr( a , 0 );
    clr( b , 0 );
    cin >> n;
    rep(i,1,20) {
        a[i] = n % 10;
        n /= 10;
    }
}

bool ok() {
    red(i,20,1) {
        if ( a[i] > b[i] ) return true;
        if ( a[i] < b[i] ) return false;
    }
    return true;
}

void work()
{
    red(i,20,1)
        red(j,9,0) {
            rep(k,1,i) b[k] = j;
            if ( ok() ) break;
        }
    lint ans = 0;
    red(i,20,1) ans = ans * 10 + b[i];
    cout << ans << endl;
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
