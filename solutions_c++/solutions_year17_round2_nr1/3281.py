#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i,j,n) for(ll i= j;i<=n;++i)
void solve(ll case_no){
    ll total_km,total_horse;
    cin>>total_km>>total_horse;
    ll arr[total_horse];
    double time,dist;
    double time_max = INT_MIN;
    rep(i,0,total_horse-1){
        ll speed;
        cin>>dist>>speed;
        dist = total_km - dist;
        dist = dist/(speed*1.0);
        time_max = max(time_max,dist);
    }

    printf("Case #%lld: %.6f\n",case_no,(total_km/time_max));
    return;

}


int main() {
    freopen("largeA.in","r",stdin);
    freopen("outc.txt","w",stdout);
    ll t;
    cin>>t;
    rep(i,1,t) solve(i);
    return 0;
}