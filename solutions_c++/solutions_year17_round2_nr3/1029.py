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
#define MAXN 1005
#define inf 0x3f3f3f3f

struct node{
    int x,y;
    node(){}
    node(int xx,int yy):x(xx),y(yy){}
    bool operator < (const node a) const{
        if(x == a.x) return y < a.y;
        return x < a.x;
    }
};
int a[MAXN][MAXN];
int b[MAXN];
int c[MAXN];
int d[MAXN];
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
char s[MAXN];
bool vis[MAXN];
ll sum[MAXN];
double dp[MAXN][MAXN];
int n,m;
int ans;


int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int tt,ca = 1;
    int p,q;
    scanf("%d",&tt);
    while(tt--){
        scanf("%d %d",&n,&m);
        for(int i = 0 ; i < n;i++)
            scanf("%d %d",&b[i],&c[i]);
        for(int i = 0 ;i < n; i++)
        {
            for(int j = 0 ;j < n; j++)
            {
                scanf("%d",&a[i][j]);
                if(j==i+1)
                    sum[j]=sum[j-1]+a[i][j];
            }
        }
        int u,v;
        scanf("%d %d",&u,&v);
        for(int i = 0 ;i < n; i++)
        {
            for(int j = 0;j < n; j++)
            {
                if(i==j) dp[i][j] = 0;
                else dp[i][j] = 1e18;
            }
        }
        for(int i = n-1 ;i >= 0; i--){
            for(int j = i+1;j < n; j++){
                for(int k = i+1;k <= j; k++){
                    if(sum[k] - sum[i] <= b[i]){
                        double t = (sum[k]-sum[i])*1.0/c[i];
                        dp[i][j] = min(dp[i][j],dp[k][j]+t);
                    }
                }
            }
        }
        printf("Case #%d: ",ca++);
        printf("%.9f\n",dp[0][n-1]);
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
