#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair < int, int > PII;

int main()
{
    int te; scanf("%d", &te);
    for(int t = 1; t <= te; t++)
    {
        LL n, k; scanf("%lld%lld", &n, &k);
        LL p = 0;
        while((1LL << (p + 1)) - 1 < k) p++;
        LL pot = 1 << p;
        n -= (pot - 1);
        k -= (pot - 1);
        LL kk = n / pot;
        LL x = pot * (kk + 1) - n;
        x = pot - x;
        LL mn = 0, mx = 0;
        if(k <= x) mn = kk / 2, mx = (kk + 1) / 2;
        else mn = (kk - 1) / 2, mx = kk / 2;
        printf("Case #%d: %lld %lld\n", t, mx, mn);
    }
    return 0;
}
