#include <cstdio>
#include <string>

void solve(int cas, long long lo, long long lc, long long hi, long long hc, long long rem) {
   if (rem <= hc) {
        printf("Case #%d: %lld %lld\n", cas, hi/2, (hi - 1)/2);
        return;
    } else if (rem <= lc + hc) {
        printf("Case #%d: %lld %lld\n", cas, lo/2, (lo - 1)/2);
        return;
    }
    long long ll = (lo - 1) / 2;
    long long hh = hi / 2;
    long long llc = lc, hhc = hc;
    if (lo / 2 == ll)
        llc += lc;
    else
        hhc += lc;
    if ((hi - 1) / 2 == ll)
        llc += hc;
    else
        hhc += hc;
    solve(cas, ll, llc, hh, hhc, rem - lc - hc);
}

void run(int cas) {
    long long n, k;
    scanf("%lld%lld", &n, &k);
    solve(cas, n, 1, n, 0, k);
}

int main() {
    int tt;
    scanf("%d", &tt);
    for (int cas = 1; cas <= tt; cas++)
        run(cas);
    return 0;
}
