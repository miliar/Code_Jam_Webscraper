#include <iostream>
#include <random>
#include <ctime>
#include <cstdio>

using namespace std;

inline void work()
{
    int t, n;
    scanf("%d%d", &n, &t);
    if (t == 2)
    {
        int e = 0, o = 0;
        for (int i = 0; i < n; ++i)
        {
            int x;
            scanf("%d", &x);
            if (x % 2 == 0) ++e; else ++o;
        }
        printf("%d\n", e + (o + 1) / 2);
    }
    else
    {
        int p = 0, q = 0, r = 0;
        for (int i = 0; i < n; ++i)
        {
            int x;
            scanf("%d", &x);
            if (x % 3 == 0) ++r; else if (x % 3 == 1) ++p; else ++q;
        }
        int s = min(p, q);
        int ans = r + s;
        p -= s, q -= s;
        ans += p / 3 + q / 3;
        p %= 3, q %= 3;
        if (p + q) ++ans;
        printf("%d\n", ans);
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i)
    {
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}
