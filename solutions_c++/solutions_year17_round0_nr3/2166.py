#include <bits/stdc++.h>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;++i)

void solve() {
    long long n,k;
    scanf("%lld%lld",&n,&k);
    ++n;
    set<long long> s;
    unordered_map<long long, long long> count;
    
    s.insert(n);
    count[n] = 1;
    while(1) {
        auto x = *s.rbegin();
        s.erase(x);
        auto c = count[x];
        if (k <= c) {
            printf("%lld %lld\n", x-x/2-1, x/2-1);
            return;
        }
        k -= c;
        s.insert(x/2);
        count[x/2]+=c;
        s.insert(x-x/2);
        count[x-x/2]+=c;
    }
    
    
}


int main(void) {
    int t;
    scanf("%d\n",&t);
    FOR(i,t) {
        printf("Case #%d: ", i+1);
        solve();
    }
    
}
