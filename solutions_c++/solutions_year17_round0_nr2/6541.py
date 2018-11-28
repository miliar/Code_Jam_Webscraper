#include <bits/stdc++.h>

using namespace std;

typedef long long int LL;

int num[30],len ;
LL dp[30][10];
LL dfs(int pos,int pre,int limit){
    if(pos<0) return 1;

    if(!limit&&dp[pos][pre]!=-1) return dp[pos][pre];

    int endi = 9;
    if(limit) endi = num[pos];
    LL res = 0;
    for(int i=0;i<=endi;i++){
        if(i>=pre)
            res+=dfs(pos-1,i,limit&&i==endi);
    }

    if(!limit) dp[pos][pre]=res;
    return res;
}


LL cal(LL n){
    len = 0;
    while(n){
        num[len++]=n%10;
        n/=10;
    }
    return dfs(len-1,0,1);
}

void solve(LL n){
    LL x = cal(n);

    LL l=0,r=n,mid,ans;
    while(l<=r){
        mid = (r+l)>>1;
        if(cal(mid)>=x)
            ans = mid,r=mid-1;
        else
            l=mid+1;
    }
    printf("%lld\n",ans);
    return ;
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    memset(dp,-1,sizeof(dp));
    int _;
    LL n;
    scanf("%d",&_);
//    printf("%d",&_);
    for(int i=1;i<=_;i++){
        scanf("%lld",&n);
//        printf("%lld\n",n);
        printf("Case #%d: ",i);
        solve(n);
    }
    return 0;
}
