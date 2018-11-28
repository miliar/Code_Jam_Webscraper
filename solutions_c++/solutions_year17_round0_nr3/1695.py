#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    int cs = 0;
    while (t--) {
        cs++;
        long long n, k;
        scanf("%lld %lld", &n, &k);
        long long i = 0; 
        while ((1LL << (i + 1)) - 1LL < k) {
            i = i + 1;
        }
        long long used = ((1LL << i) - 1);
        long long remaining = k - used;
        long long ones = (n - used) % (used + 1);
        long long base = (n - used) / (used + 1);
        if (ones == 0) {
            base = base - 1;
            ones = (used + 1);
        }
        printf("Case #%d: ", cs);
        if (remaining <= ones) {
            printf("%lld %lld\n", (base + 1) / 2, (base) / 2);
        } else {
            printf("%lld %lld\n", (base) / 2, (base - 1) / 2);
        }
    }
}
