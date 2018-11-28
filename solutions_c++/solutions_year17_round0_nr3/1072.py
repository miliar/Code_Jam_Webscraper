#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

long long dp(long long n1, long long c1, long long n2, long long c2, long long k) {
    if (c1 + c2 >= k) {
        if (k <= c1) return n1;
        else return n2;
    }
    else {
        long long newn1 = -1, newc1 = 0, newn2 = -1, newc2 = 0;
        if (n1%2==0) {
            newn1 = n1/2;
            newn2 = (n1-1)/2;
            newc1 += c1;
            newc2 += c1;
        }
        else {
            newn1 = (n1-1)/2;
            newc1 += 2*c1;
        }
        if (n2 != -1) {
            if (n2%2==0) {
                newn2 = (n2-1)/2;
                newc1 += c2;
                newc2 += c2;
            }
            else {
                if (newn2 == -1) newn2 = (n2-1)/2;
                newc2 += 2*c2;
            }
        }

        return dp(newn1, newc1, newn2, newc2, k-c1-c2);
    }
}

int main() {
    freopen("Documents/Informatics/GoogleCodeJam/in.txt", "r", stdin);
    freopen("Documents/Informatics/GoogleCodeJam/bathroom.txt", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int cas = 1; cas <= tc; cas++) {
        long long n, k;
        scanf("%lld %lld", &n, &k);
        long long ans = dp(n, 1, -1, 0, k);
        printf("Case #%d: %lld %lld\n", cas, ans/2, (ans-1)/2);
    }
    return 0;
}
