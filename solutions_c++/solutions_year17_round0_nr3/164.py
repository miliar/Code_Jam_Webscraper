#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
void solve(int tc){
    printf("Case #%d: ",tc);
    ll n,k; scanf("%I64d%I64d",&n,&k);
    map<ll,ll> dp;
    queue<ll> q;
    q.push(n); dp[n]=1;
    while(!q.empty()){
        ll t=q.front(); q.pop();
        ll ls=(t-1)/2,gt=t/2;
        if(gt>0){
            dp[gt]+=dp[t];
            if(q.empty() || q.back()!=gt) q.push(gt);
        }
        if(ls>0){
            dp[ls]+=dp[t];
            if(q.empty() || q.back()!=ls) q.push(ls);
        }
    }
    ll sum=0;
    for(auto x: dp){
        sum += x.second;
        //cout << x.first << " " << x.second << " " << sum << endl;
        if(n < sum+k){
            printf("%I64d %I64d\n",x.first/2,(x.first-1)/2);
            return;
        }
    }
}

int main()
{
    freopen("C-large.in","r",stdin); freopen("out.txt","w",stdout);
    int T; scanf("%d",&T);
    for(int tc=1;tc<=T;tc++){
        solve(tc);
    }
    return 0;
}
