#include <stdio.h>
#include <map>

using namespace std;

#define ll long long

int main() {
    int T;
    long long N, K;
    map<ll, ll> m;
    map<ll, ll>::reverse_iterator it;
    int i;
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &T);
    for(i = 0; i < T; i++) {
        scanf("%lld %lld", &N, &K);
        m.clear();
        m[N] = 1;
        it = m.rbegin();
        for(it = m.rbegin(); K > 0; it++) {
            //printf("[%lld %lld]\n", it -> first, it -> second);
            K -= it -> second;
            m[(it -> first) / 2] += it -> second;
            m[(it -> first - 1) / 2] += it -> second;
        }
        it--;
        printf("Case #%d: %lld %lld\n", i + 1, (it -> first) / 2, (it -> first - 1) / 2);
    }
    
    return 0;
}
