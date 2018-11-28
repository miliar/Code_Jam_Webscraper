#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

class Solution
{
private:
    char s[1024], f[1024], d[1024];
public:
    void pancake()
    {
        scanf("%s", s);
        int n = strlen(s), K;
        for (int i = 0; i < n; ++i)
            f[i] = '-' == s[i];
        scanf("%d", &K);
        int xr = 0, ans = 0;
        for (int i = 0; i <= n - K; ++i)
        {
            if (i >= K) xr ^= d[i - K];
            d[i] = xr ^ f[i];
            ans += d[i];
            xr = f[i];
        }
        for (int i = n - K + 1; i < n; ++i)
        {
            if (i >= K) xr ^= d[i - K];
            if ((xr ^ ('-' == s[i])) == 1)
            {
                printf("IMPOSSIBLE\n");
                return ;
            }
        }
        printf("%d\n", ans);
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
        s.pancake();
    }
    return 0;
}
