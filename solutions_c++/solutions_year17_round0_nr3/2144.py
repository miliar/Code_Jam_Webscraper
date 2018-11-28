#include <bits/stdc++.h>

void test(int t) {
    long long N, K;
    std::cin >> N >> K;
    
    std::map<long long, long long> mp;
    mp[N] = 1;
    
    while(!mp.empty()) {
        auto iter = --mp.end();
        
        mp[(iter->first-1ll)/2ll] += iter->second;
        long long r = (iter->first-1ll)%2ll;
        mp[(iter->first-1ll)/2ll+r] += iter->second;
        
        K -= iter->second;
        if(K <= 0) {
            std::cout << "Case #" << t << ": " << (iter->first-1ll)/2ll+r << " " << (iter->first-1ll)/2ll << std::endl;
            return;
        }
        mp.erase(iter);
    }
}

int main() {
    int t;
    std::cin >> t;
    for(int i=0; i<t; ++i) test(i+1);
}
