#include<bits/stdc++.h>
using namespace::std;
typedef long long ll;
ll getPrev2(ll N){
    N |= N >> 1;
    N |= N >> 2;
    N |= N >> 4;
    N |= N >> 8;
    N |= N >> 16;
    N |= N >> 32;
    return (N >> 1) + 1;
}

ll getNext2(ll N)
{
    N |= N >> 1;
    N |= N >> 2;
    N |= N >> 4;
    N |= N >> 8;
    N |= N >> 16;
    N |= N >> 32;
    N++;
    return N;
}
ll getMaxLR(ll N,ll K){
    N = N-K+1;
    if(N<=getPrev2(K)){ return 0LL; }
    N = N-getPrev2(K);
    ll div = getNext2(K);
    return (N+div-1)/div;
}
ll getMinLR(ll N,ll K){
    ll res = max(N-K,0LL)/getNext2(K);
    return res;
}
int main(){
    int T;
    cin >> T;
    ll N,K;
    for(int tt=1;tt<=T;tt++){
        cin >> N >> K;
        printf("Case #%d: %lld %lld\n",tt,getMaxLR(N,K),getMinLR(N,K));
    }
}
