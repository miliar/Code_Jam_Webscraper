/*
 * Author:  vawait
 * Created Time:  日  4/30 18:26:27 2017
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
int n , k;
double m , p[100];

void init()
{
    scanf("%d%d",&n,&k);
    cin >> m;
    rep(i,1,n) cin >> p[i];
    sort( p + 1 , p + n + 1 );
}

void work()
{
    double ans = 1, sum;
    p[n+1] = 1;
    rep(i,2,n+1) {
        sum = 0;
        rep(j,1,i-1) sum += p[i] - p[j];
        if ( sum > m ) sum = m;
        m -= sum;
        rep(j,1,i-1) p[j] += sum / ( i - 1 );
    }
    rep(i,1,n) ans *= p[i];
    printf("%.9f\n",ans);
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
