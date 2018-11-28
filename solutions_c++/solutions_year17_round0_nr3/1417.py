#include <stdio.h>
#include <utility>

#define ll long long

using namespace std;
int T;
ll N, K, m, M;

pair<ll, ll> ans;

void bs(ll n, ll k){
    
    if(k == 1){
        ans = make_pair(n >> 1, (n-1) >> 1);
        return;
    }

    if(k & 1){
        bs((n-1)>>1, k / 2);
    } else {
        bs(n>>1, k / 2);
    }
}
int main(){
//    freopen("/Users/depa/Downloads/C-large.in", "r", stdin);
    scanf("%d", &T);
    
    for(int t = 1; t<= T; ++t){
        
        scanf("%lld %lld", &N, &K);
        
        bs(N, K);
        
        printf("Case #%d: %lld %lld\n", t, ans.first, ans.second);
    }
    
    return 0;
}
