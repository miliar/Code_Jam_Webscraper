/*
 * Author:  vawait
 * Created Time:  日  4/30 17:14:11 2017
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
const int maxn = 60*25;
const int n = 60 * 24;
int f[maxn][maxn][3][3], flag[maxn];

void init()
{
    int x , y , l , r;
    clr( flag , 0 );
    scanf("%d%d",&x,&y);
    rep(i,1,x) {
        scanf("%d%d",&l,&r);
        rep(j,l+1,r) flag[j] = 1;
    }
    rep(i,1,y) {
        scanf("%d%d",&l,&r);
        rep(j,l+1,r) flag[j] = 2;
    }
    clr( f , 1 );
}

void mi(int &x,int y) {
    if ( x > y ) x = y;
}

void work()
{
    f[0][0][2][2] = f[0][0][1][1] = 1;
    rep(i,0,n) {
        rep(j,0,n/2) rep(r,1,2) rep(b,1,2) {
            rep(k,1,2) if ( flag[i+1] == 0 || flag[i+1] == k ) {
                mi( f[i+1][j+(k==1)][k][b] , f[i][j][r][b] + ( k != r ) );
            }
        }
    }
    int ans = n;
    rep(i,1,2)
        rep(j,1,2) {
            mi( ans , f[n][n/2][i][j] - ( i == j ) );
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
