#include <cstdio>
#include <map>
using namespace std;

int main() {
    int t;
    long long n, k;
    scanf("%d", &t);
    for(int T = 1; T <= t; T++) {
        long long m, ans, a, b;
        map<long long, long long> d;
        scanf("%lld %lld", &n, &k);
        d[n] = 1;
        while (k > 0) {
            auto it = d.rbegin();
            ans = it -> first;
            k -= it -> second;
            d[ans / 2] += it -> second;
            d[ans / 2 - (ans+1) % 2] += it -> second;
            d.erase(ans);
        }
        printf("Case #%d: %lld %lld\n", T, ans / 2, ans / 2 - (ans+1) % 2);
    }
    return 0;
}