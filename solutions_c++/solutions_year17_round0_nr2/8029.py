#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

void fhihihi(long long ind, long long n) {
    long long ans = 0, k = 1, cur = 9;
    while (n > 0) {
        if (cur >= n % 10) {
            cur = n % 10;
            ans += k * (n % 10);
        } else {
            ans = k - 1 + (n % 10 - 1) * k;
            cur = n % 10 - 1;
        }
        k *= 10;
        n /= 10;
    }
    printf("Case #%lld: %lld\n", ind, ans);
}


int main() {
    long long t, i;
    long long n;
    scanf("%lld", &t);
    for (i=1; i<=t; i++) {
        scanf("%lld", &n);
        fhihihi(i, n);
    }
}
