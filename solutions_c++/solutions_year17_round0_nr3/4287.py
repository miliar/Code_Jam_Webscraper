#include <cstdio>
#include <set>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    long long N;
    int K;
    for(int t = 1; t <= T; t++) {
        scanf("%lld %d", &N, &K);
        multiset<long long> s;
        s.insert(-N);
        long long b;
        for(int k = 1; k < K; k++) {
            b = -*s.begin();
            s.erase(s.begin());
            if(b % 2 == 0) {
                s.insert(-(b / 2));
                if(b != 2) s.insert(-(b / 2) + 1);
            } else {
                if(b != 1) {
                    s.insert(-(b / 2));
                    s.insert(-(b / 2));
                }
            }
        }
        b = -*s.begin();
        if(b % 2 == 0) printf("Case #%d: %lld %lld\n", t, b / 2, b / 2 - 1);
        else printf("Case #%d: %lld %lld\n", t, b / 2, b / 2);
    }
    return 0;
}
