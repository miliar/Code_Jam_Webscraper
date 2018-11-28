#include<bits/stdc++.h>
using namespace std;
const int N = 1002;
int n , k;
pair<int,int> arr[N];
double seg[N][4*N];
double dp[N][N];
double pi = 3.1415926535897932384626433832795;
double getmax(int s,int e,int idx,int k,int l,int r){
    if(s > r || e < l)
        return 0;
    if(s >=l && e <= r)
        return seg[k][idx];
    return max(getmax(s,(s+e)/2,idx*2,k,l,r),getmax((s+e)/2+1,e,idx*2+1,k,l,r));
}
double update(int s,int e,int idx,int k,int idx2,double val){
    if(s > idx2 || e < idx2)
        return seg[k][idx];
    if(s == idx2 && e == idx2)
        return seg[k][idx] = val;
    return seg[k][idx] = max(update(s,(s+e)/2,idx*2,k,idx2,val),update((s+e)/2+1,e,idx*2+1,k,idx2,val));
}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int cs = 1;
    while(t--){
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++){
            scanf("%d%d",&arr[i].first,&arr[i].second);
        }
        sort(arr,arr+n);
        double ans =0  ;
        for(int j=k-1;j>=0;j--){
            for(int i = n-1;i>=0;i--){
                double cur = (double)2*pi*(double)arr[i].second*(double)arr[i].first;
                if(j == k-1){
                    cur += (double)arr[i].first*(double)arr[i].first*pi;
                    dp[i][j] = cur;
                    update(0,n-1,1,j,i,dp[i][j]);
                    if(j == 0)
                        ans = max(ans,dp[i][j]);
                    continue;
                }
                double mx = (i == n-1 ? 0 : getmax(0,n-1,1,j+1,i+1,n-1));
                dp[i][j] = mx+cur;
                update(0,n-1,1,j,i,dp[i][j]);
                if(j == 0)
                ans = max(ans,dp[i][j]);
            }
        }
        printf("Case #%d: %.9lf\n",cs++,ans);
    }
    return 0;
}

