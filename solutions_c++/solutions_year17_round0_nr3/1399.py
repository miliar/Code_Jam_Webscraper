#include <cstdio>
#include <map>

using namespace std;

typedef long long lint;

int main() {
    int t;
    lint n, k;
    scanf("%d", &t);
    
    for (int tc = 1; tc <= t; tc++) {                
        scanf("%lld %lld", &n, &k);
        
        map<lint, lint, greater<lint> > m;
        
        m[n] = 1;
        
        while (k > 0) {
            pair<lint, lint> p = *(m.begin());
            
            lint big = p.first / 2LL;
            lint small = (p.first - 1LL) / 2LL;
            
            if (k <= p.second) {
                printf("Case #%d: %lld %lld\n", tc, big, small);
            } else {            
                m.erase(m.begin());
                
                m[big] += p.second;
                m[small] += p.second;                
            }
            k-= p.second;
        }
    }
    return 0;
}

