#include<bits/stdc++.h>
#include<algorithm>
#define ll long long int
template<typename T> void print_queue(T& q) {
    while(!q.empty()) {
        std::cout << q.top() << " ";
        q.pop();
    }
    std::cout << '\n';
}
int main(){
int t; scanf("%d",&t);
for(int i=0;i<t;i++){
        ll n,k;
    scanf("%lld %lld",&n,&k);
    std::priority_queue<ll> q;
    q.push(n);
    k--;
    while(k--){
        ll temp=q.top(); q.pop();
        q.push(ceil((temp-1.0)/2)); q.push(floor((temp-1.0)/2));
    }
    ll temp=q.top(); q.pop();
    ll a=(ceil((temp-1.0)/2)); ll b=(floor((temp-1.0)/2));
    //std::cout<<a<<b;
    printf("Case #%d: %lld %lld\n",i+1,std::max(a,b),std::min(a,b));
}
return 0;
}
