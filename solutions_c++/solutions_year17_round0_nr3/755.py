#include <bits/stdc++.h>
#define ll long long
using namespace std;
map<ll,ll> mp;
priority_queue<ll> pq;

void solve() {
    while(!pq.empty()) pq.pop();
    mp.clear();
    ll n,k;
    scanf("%lld %lld",&n,&k);
    mp[n] = 1;
    pq.push(n);
    while(k > 0) {
        ll toPop = pq.top();
        pq.pop();
        k -= mp[toPop];
        //printf("POP (%lld) %lld\n",toPop,mp[toPop]);
        if(k <= 0) {
            // ans
            printf("%lld %lld\n",(toPop)/2,(toPop-1)/2);
            return;
        }
        if(mp[toPop/2]==0) pq.push(toPop/2);
        mp[toPop/2] += mp[toPop];

        if(mp[(toPop-1)/2] == 0) pq.push((toPop-1)/2);
        mp[(toPop-1)/2] += mp[toPop];

        mp.erase(toPop);
    }
}
int main() {
    int t;
    scanf("%d",&t);
    for(int i = 0;i < t;i++) {
        printf("Case #%d: ",i+1);
        solve();
    }
}
