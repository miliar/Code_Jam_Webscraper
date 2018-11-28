#include<bits/stdc++.h>
#define ll long long
using namespace std;

pair<ll,ll> result(ll n, ll k){
    priority_queue<ll> pq;
    pq.push(n);
    k--;
    while(k--){
        ll temp = pq.top()-1;
        pq.pop();
        if(temp)
            pq.push(temp/2);
        if (temp - temp/2)
            pq.push(temp - temp/2);
    }
    ll M = pq.top()-1;
    return pair<ll,ll>(M-M/2,M/2);
    /*
    int lsb=sizeof(ll)*8-1;
    for(;!(k & (1LL<<lsb));lsb--);
    for(int cnt=lsb-1;cnt>=0;cnt--){
        n--;
        if(k & (1<<cnt))
            n = n/2;
        else n = n-n/2;
    }
    n--;
    return pair<ll,ll>(n-n/2,n/2);
    */
}

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        ll n,k;
        cin>>n>>k;
        pair<ll,ll> res=result(n,k);
        printf("Case #%d: ",t);
        cout<<res.first<<" "<<res.second<<"\n";

    }

    return 0;
}
