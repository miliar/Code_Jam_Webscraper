#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <vector>
#include <time.h>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <iostream>
#include <assert.h>
#include <bitset>
#include <algorithm>
using namespace std;
#define MP make_pair
#define PB push_back
#define mst(a,b) memset((a),(b),sizeof(a))
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> Pii;
typedef vector<int> Vi;
typedef vector<Pii> Vii;
const int inf = 0x3f3f3f3f;
const LL INF = (1uLL << 63) - 1;
const int mod = 1e9 + 7;
const double Pi = acos(-1.0);
const int maxn = 1e5 + 5;
const int N = 2e4 + 5;
const ULL hashmod = 2908361;
const double eps = 1e-8;
double dp[105][105];
int mov[105];
int v[105];
LL sum[105];
int dis[105][105];
int main() {
#ifdef local
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("w", "w", stdout);
#endif
    // ios::sync_with_stdio(false);
    //  cin.tie(0);
    int t;
    scanf("%d", &t);
    int ssss = 1;
    while(t--) {
        printf("Case #%d: ", ssss++);
        int n,q;
        int s,t;
        scanf("%d%d",&n,&q);
        for(int i = 1; i <= n; i++){
            scanf("%d%d",&mov[i],&v[i]);
        }
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                scanf("%d",&dis[i][j]);
            }
        }
        while(q--){
            scanf("%d%d",&s,&t);
        }
        for(int i = 0; i < 105; i++)for(int j = 0; j < 105 ;j++)dp[i][j] = 1e100;
        dp[s][s] = 0;
        sum[s] = 0;
        for(int i = s + 1; i <= t; i++){
            sum[i] = sum[i - 1] + dis[i - 1][i];
        }
        for(int i = s; i < t; i++){
            for(int j = s; j <= i; j++){
                if(dp[i][j] < 1e30){
                    if(sum[i + 1] - sum[j] <= mov[j]){
                        dp[i + 1][j] = min(dp[i+1][j],dp[i][j] + (double)(sum[i + 1] - sum[i])/v[j]);
                    }
                    if(sum[i + 1] - sum[i] <= mov[i]){
                        dp[i + 1][i] = min(dp[i+1][i],dp[i][j] + (double)(sum[i + 1] - sum[i])/v[i]);
                    }
                }
            }
        }
        double ans = 1e100;
        for(int i = 0; i <= t; i++)ans = min(ans,dp[t][i]);
        printf("%.10f\n",ans);
    }
}
