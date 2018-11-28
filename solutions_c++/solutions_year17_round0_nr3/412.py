#include <cstdio>
#include <map>

using namespace std;

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        long long n, k, y, z;
        map <long long, long long> mp;
        map <long long, long long>::iterator it;
        
        scanf("%lld %lld", &n, &k);
        
        mp[n] = 1;
        
        while (1) {
            it = mp.end();
            it--;
            
            if (it->second >= k) {
                y = it->first / 2;
                z = (it->first - 1) / 2;
                break;
            } else {
                mp[it->first / 2] += it->second;
                mp[(it->first - 1) / 2] += it->second;
                k -= it->second;
                mp.erase(it);
            }
        }
        
        printf("Case #%d: %lld %lld\n", i + 1, y, z);
    }
    
    return 0;
}
