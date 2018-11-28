#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int const maxN = 110;
int const maxP = 5;

int n, p;
int cnt[maxP];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
    {
        scanf("%d%d", &n, &p);
        for (int j = 0; j < p; ++j)
        {
            cnt[j] = 0;
        }
        for (int j = 0; j < n; ++j)
        {
            int x;
            scanf("%d", &x);
            cnt[x % p]++;
        }
        printf("Case #%d: ", i + 1);
        if (p == 2)
        {
            printf("%d\n", cnt[0] + cnt[1] / 2 + (cnt[1] % 2 > 0));
            continue;
        }
        if (p == 3)
        {
            int ans = cnt[0];
            int k = min(cnt[1], cnt[2]);
            ans += k;
            cnt[1] -= k;
            cnt[2] -= k;
            ans += cnt[1] / 3 + (cnt[1] % 3 > 0);
            ans += cnt[2] / 3 + (cnt[2] % 3 > 0);
            printf("%d\n", ans);
            continue;
        }
        if (p == 4)
        {
            int ans = cnt[0];
            int k = min(cnt[1], cnt[3]);
            ans += k;
            cnt[1] -= k;
            cnt[3] -= k;
            ans += cnt[2] / 2;
            cnt[2] %= 2;
            if (cnt[2] == 0)
            {
                ans += cnt[1] / 4 + (cnt[1] % 4 > 0);
                ans += cnt[3] / 4 + (cnt[3] % 4 > 0);
            }
            else
            {
                if (cnt[1] >= 2)
                {
                    ans += 1 + (cnt[1] - 2) / 4 + ((cnt[1] - 2) % 4 > 0);
                }
                else
                {
                    if (cnt[1] == 1)
                    {
                        ans++;
                    }
                    else
                    {
                        if (cnt[3] >= 2)
                        {
                            ans += 1 + (cnt[3] - 2) / 4 + ((cnt[3] - 2) % 4 > 0);
                        }
                        else
                        {
                            ans++;
                        }
                    }
                }
            }
            printf("%d\n", ans);
        }
    }
    return 0;
}