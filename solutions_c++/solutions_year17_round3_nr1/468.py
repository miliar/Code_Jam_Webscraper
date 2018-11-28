#include <bits/stdc++.h>
#define ff first
#define ss second
#define pi 3.14159265359
using namespace std;
typedef long long ll;

double dp[1001][1001][2];
bool vis[1001][1001][2];
pair<int,int> arr[1001];
int n , k;
double solve(int idx,int k,int f){
    if(!k && f)return 0;
    if(idx == n){
        return -1e15;
    }
    double &ret = dp[idx][k][f];
    if(vis[idx][k][f])return ret;
    vis[idx][k][f] = true;
    if(!f){
        ret = solve(idx+1,k-1,1) + pi*arr[idx].ff*arr[idx].ff + pi*2 * arr[idx].ff * arr[idx].ss;
        ret = max(solve(idx+1,k-1,0) + pi*arr[idx].ff*arr[idx].ss*2 , ret) ;
        ret = max(solve(idx+1,k,0),ret)  ;
    }else{
        ret = solve(idx+1,k-1,1) + pi*arr[idx].ff*arr[idx].ss*2  ;
        ret = max(solve(idx+1,k,1),ret)  ;
    }
    return ret;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("smalllarge.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int I = 1 ; I <= t ; I ++){
       // int n,k;
        cin >> n >> k;
        multiset<pair<int,int>> s;
        for(int i = 0 ; i < n ; i ++){
            int r,h;
            cin >> arr[i].ff >> arr[i].ss;
        }
        memset(vis,0,sizeof vis);
        printf("Case #%d: %.9lf\n",I,solve(0,k,0));
    }
    return 0;
}
