#include <cstdio>

using namespace std;

typedef long long LL;

int main()
{
    int tt;
    scanf("%d", &tt);
    for (int ti = 1; ti <= tt; ti++)
    {
        LL n, k;
        scanf("%I64d%I64d", &n, &k);
        LL i = 1;
        while (k >= (1LL << i)) i++;
        LL low1 = (n + 1 - (1 << (i - 1))) / (1 << (i - 1));
        LL hig1 = n / (1 << (i - 1));
        LL cnth1 = (n + 1 - (1 << (i - 1))) % (1 << (i - 1));
        k -= (1 << (i - 1));
        LL ans = (k < cnth1) ? (hig1 - 1) : (low1 - 1);
        printf("Case #%d: %I64d %I64d\n", ti, (ans + 1) / 2, ans / 2);
    }
    return 0;
}
