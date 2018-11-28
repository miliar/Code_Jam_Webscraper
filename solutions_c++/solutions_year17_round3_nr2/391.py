/*    brioso     */
//#include <bits/stdc++.h>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;
#define PB push_back
#define MP make_pair
#define AA first
#define BB second
#define SZ size()
#define BG begin()
#define ED end()
#define SQ(x) ((x)*(x))
#define MT(a,x) memset(a,x,sizeof(a))
#define rep(i,a,b) for (int i=(a);i<(b);i++)
#define per(i,a,b) for (int i=(b)-1;i>=(a);i--)
typedef long long ll ;
typedef pair<int, int> PII;
typedef pair<double,double> PDD;
const double PI = acos(-1.0);
const double eps =1e-8;
const int mod = 1000000007;
#define MAXN 1505
#define inf 0x3f3f3f3f

struct node{
    int x,y;
    node(){}
    node(int xx,int yy):x(xx),y(yy){}
    bool operator < (const node a) const{
        if(x == a.x) return y < a.y;
        return x < a.x;
    }
}a[MAXN],b[MAXN];
int c[MAXN];
int d[MAXN];
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
char s[MAXN];
int vis[MAXN];
int n,m;
int ans;
int dp[MAXN][MAXN][3][3];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int tt,ca = 1;
    int p,q;
    scanf("%d",&tt);
    while(tt--){
        scanf("%d %d",&n,&m);
        MT(vis,0);
        for(int i = 1 ; i <=n ; i++){
            scanf("%d %d",&a[i].x,&a[i].y);
            for(int j = a[i].x+1 ; j <= a[i].y ; j++)
                vis[j] = 1;
        }
        for(int i = 1 ; i <=m ; i++){
            scanf("%d %d",&b[i].x,&b[i].y);
            for(int j = b[i].x+1 ; j <= b[i].y ; j++)
                vis[j] = 2;
        }
        MT(dp,inf);
        if(vis[1] != 1)
            dp[1][1][1][1] = 0;
        if(vis[1] != 2)
            dp[1][0][2][2] = 0;
        rep(i,2,1441){
            rep(j,0,721){
                if(vis[i] != 1){
                    if(j)
                        rep(k,1,3) dp[i][j][1][k]=min(dp[i][j][1][k],dp[i-1][j-1][1][k]);
                    rep(k,1,3) dp[i][j][1][k]=min(dp[i][j][1][k],dp[i-1][j-1][2][k]+1);
                }
                if(vis[i] != 2){
                    rep(k,1,3) {
                        dp[i][j][2][k]=min(dp[i][j][2][k],dp[i-1][j][2][k]);
                        dp[i][j][2][k]=min(dp[i][j][2][k],dp[i-1][j][1][k]+1);
                    }
                }
            }
        }
        ans = inf;
        rep(i,1,3) rep(j,1,3){
            if(i!=j)
                dp[1440][720][i][j]++;
            ans=min(ans,dp[1440][720][i][j]);
        }
        printf("Case #%d: ",ca++);
        printf("%d\n",ans);
    }
    return 0;
}


/*

unsigned   int   0～4294967295
int   2147483648～2147483647
unsigned long 0～4294967295
long   2147483648～2147483647
long long的最大值：9223372036854775807
long long的最小值：-9223372036854775808
unsigned long long的最大值：18446744073709551615

__int64的最大值：9223372036854775807
__int64的最小值：-9223372036854775808
unsigned __int64的最大值：18446744073709551615

*/
