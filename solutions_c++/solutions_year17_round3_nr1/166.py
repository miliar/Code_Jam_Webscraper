/*
 * Author:  vawait
 * Created Time:  日  4/30 17:54:33 2017
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
#define x first
#define y second
typedef long long lint;
const int maxn = 1100;
const double pi = acos(-1.0);
int n , k ; 
double b[maxn];
pair < int , int > a[maxn];

void init()
{
    scanf("%d%d",&n,&k);
    rep(i,1,n) scanf("%d%d",&a[i].x,&a[i].y);
    sort( a + 1 , a + n + 1 );
}

void work()
{
    double ans = 0, sum;
    rep(i,k,n) {
        sum = pi * a[i].x * a[i].x;
        rep(j,1,i) b[j] = 2 * a[j].x * pi * a[j].y;
        sort( b + 1 , b + i );
        rep(j,i-k+1,i) sum += b[j];
        if ( ans < sum ) ans = sum;
    }
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
