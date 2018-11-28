#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
typedef long long LL;

class Solution
{
private:
    LL d[20],d0[20];
public:
    Solution()
    {
        d[0] = 0;
        d[1] = 1;
        d0[0] = 1;
        d0[1] = 10;
        for (int i = 2; i <= 18; ++i)
        {
            d[i] = d[i - 1] * 10LL + 1;
            d0[i] = d0[i - 1] * 10LL;
        }
    }
    void tidyNum()
    {
        LL n;
        scanf("%lld", &n);
        int l = 0;
        for (LL t = n; t > 0; t /= 10) ++ l;
        LL ans, la = 0;
        for (ans = 0; l > 0; -- l)
        {
            for (LL t = la; t < 10 && (ans + t * d[l] <= n); ++t)
                la = t;
            ans += la * d0[l - 1];
        }
        printf("%lld\n", ans);
    }
};

int main()
{
    int stt;
    Solution s;
    scanf("%d", &stt);
    for (int i = 1; i <= stt; ++i)
    {
        printf("Case #%d: ", i);
        s.tidyNum();
    }
    return 0;
}
