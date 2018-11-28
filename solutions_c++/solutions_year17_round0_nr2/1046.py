#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;


long long calc(long long n) {
    long long tens = 1000000000000000000LL;
        while (n/tens == 0) tens/=10;
    long long ans = 0;
    int prev = 0;
    while (tens >= 1 && n/tens >= prev) {
        prev = n/tens;
        ans*=10;
        ans += n/tens;
        n = n%tens;
        tens/=10;
    }
    if (tens >= 1) {
        ans--;
    }
    while (tens >= 1) {
        ans *= 10;
        ans += 9;
        tens /= 10;
    }
    return ans;
}

int main() {
    freopen("Documents/Informatics/GoogleCodeJam/in.txt", "r", stdin);
    freopen("Documents/Informatics/GoogleCodeJam/tidy.txt", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int cas = 1; cas <= tc; cas++) {
        long long n;
        scanf("%lld", &n);
        long long ans = calc(n);
        while (ans != n) {
            n = ans;
            ans = calc(n);
        }
        printf("Case #%d: %lld\n", cas, ans);
    }
    return 0;
}
