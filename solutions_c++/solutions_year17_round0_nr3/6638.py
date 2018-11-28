#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

typedef long long ll;

int main()
{
    freopen("c2.in","r",stdin);
    freopen("outc2.txt","w",stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ca++)
    {
        ll n, k;
        scanf("%lld%lld", &n, &k);
        ll i = 1;
        while (k >= (1ll << i)) i++;
        ll left = (n + 1 - (1 << (i - 1))) / (1 << (i - 1));
        ll right = n / (1 << (i - 1));
        ll cnth1 = (n + 1 - (1 << (i - 1))) % (1 << (i - 1));
        k -= (1 << (i - 1));
        ll ans = (k < cnth1) ? (right - 1) : (left - 1);
        printf("Case #%d: %lld %lld\n", ca, (ans + 1) / 2, ans / 2);
    }
    return 0;
}
