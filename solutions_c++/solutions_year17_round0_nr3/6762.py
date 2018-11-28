#include <bits/stdc++.h>
using namespace std;
#define ll long long


int main() {
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++) {
        ll n,k,y,ans;
        printf("Case #%d: ",tt);
        scanf("%lld%lld",&n,&k);
        priority_queue<ll> p;
        p.push(n);
        for(int i=0;i<k-1;i++)
        {
            y=p.top();
            p.pop();
            if(y%2!=0)
            {
               p.push(y/2);
               p.push(y/2);
            }
            if(y%2==0)
            {
                p.push(y/2);
                p.push(y/2 - 1);                  
            }
        }
        ans=p.top();
        if(ans%2!=0)
        {
            printf("%lld %lld\n",ans/2,ans/2);
        }
        if(ans%2==0)
        {
            printf("%lld %lld\n",ans/2,ans/2 - 1);
        }
    }
    return 0;
}