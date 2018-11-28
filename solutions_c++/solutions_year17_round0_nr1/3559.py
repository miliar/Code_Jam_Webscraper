#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
const LL mod = 1e9 + 7;
const int N = 1e5 + 5;
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, ca = 1, k;
    char s[1005];
    scanf("%d", &T);
    while(T--)
    {
        scanf("%s%d", s, &k);
        int len = strlen(s);
        int ans = 0;
        bool ok = true;
        for (int i = 0; i < len && ok; i++)
        {
            if (s[i] == '-')
            {
                if (len - i >= k)
                {
                    for (int j = i; j < i + k; j++)
                    {
                        s[j] = (s[j] == '+' ? '-' : '+');
                    }
                    ans++;
                }
                else
                {
                    ok = false;
                }
            }
        }
        printf("Case #%d: ", ca++);
        if (!ok)
        {
            puts("IMPOSSIBLE");
        }
        else
        {
            printf("%d\n", ans);
        }
    }
    return 0;
}
