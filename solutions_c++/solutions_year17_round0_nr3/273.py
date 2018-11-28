#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
typedef long long LL;

class Solution
{
private:
    LL f[100][100], len[100];

    int done(LL x)
    {
        printf("%lld %lld\n", x / 2, (x - 1) / 2);
        return 0;
    }
public:
    int bathDiv()
    {
        LL n,k;
        scanf("%lld %lld", &n, &k);
        f[0][0] = 1;
        len[0] = 1;
        for (LL i = 0, t; ; n = t, ++i)
        {
            t = n >> 1;
            len[i + 1] = t - (n - len[i]) / 2 + 1;
            fill(f[i + 1], f[i + 1] + len[i + 1], 0);
            for (LL j = 0; j < len[i]; ++j)
            {
                if ((k -= f[i][j]) <= 0)
                    return done(n - j);
                f[i + 1][t - (n - j) / 2] += f[i][j];
                f[i + 1][t - (n - j - 1) / 2] += f[i][j];
            }
        }
        return 0;
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
        s.bathDiv();
    }
    return 0;
}
