
#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include<cmath>
#include <cstring>
#include <map>
#include <set>
#include <iomanip>
#include <bitset>
#define pb push_back
#define PI acos(-1)
#define fi first
#define se second
#define INF 0x3f3f3f3f
#define INF64 0x3f3f3f3f3f3f3f3f
using namespace std;
const int mod = 1e8+7;
const int MAX_P = 2e4+10;
const int maxn =1e3+10;
const int MAX_V = 5e5+10;
const int maxv = 1e6+10;
typedef long long LL;
typedef long double DB;
typedef pair<int,int> Pair;
struct Node{
    int r,h;
    bool operator<(const Node & o)const {
        if(r == o.r)return o.h <h;
        else return o.r < r;
    }
};

Node a[maxn];
double dp[maxn][maxn];
int main() {

    int T;
    scanf("%d",&T );
    int n,k;
    int kase =0;
    while (T--) {
        scanf("%d%d",&n,&k );
        for(int i=0 ; i<n ; ++i){
            scanf("%d%d",&a[i].r,&a[i].h );
        }
        sort(a,a+n);
        memset(dp,0,sizeof(dp));
        dp[0][1] = 2*PI*a[0].r*a[0].h+PI*a[0].r*a[0].r;
        for(int i=1 ; i<n ; ++i){
            dp[i][1] = 2*PI*a[i].r*a[i].h+PI*a[i].r*a[i].r;
            for(int j=2 ;j<=k ; ++j ){
                dp[i][j] = max(dp[i][j],dp[i-1][j-1]+2*a[i].r*PI*a[i].h);
            }
            for(int j=1 ; j<=k ; ++j){
                dp[i][j] = max(dp[i][j],dp[i-1][j]);
            }
        }
        printf("Case #%d: %.9lf\n",++kase,dp[n-1][k] );

    }
    return 0;
}
