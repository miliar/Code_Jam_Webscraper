#include <iostream>
#include <tuple>
using namespace std;
using LL = long long;

pair<LL, LL> solve(LL n, LL k) {
    LL bt = 1, ml = 1;
    for (; ml*2<=k; ml*=2) {
        if (n % 2) bt += ml;
        n /= 2;
    }
    if (k - ml >= bt) --n;
    return {n / 2, (n - 1) / 2};
}

int main() {
    int t; cin >> t;
    LL n, k;
    for (int i=1; i<=t; ++i) {
        cin >> n >> k;
        LL l, r; tie(l, r) = solve(n, k);
        printf("Case #%d: %lld %lld\n", i, l, r);
    }
}
