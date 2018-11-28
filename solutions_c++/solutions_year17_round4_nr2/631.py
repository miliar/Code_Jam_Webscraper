#include <iostream>
#include <random>
#include <ctime>
#include <cstdio>

using namespace std;

bool check(int a, int b, int c)
{
    return a >= 0 && b >= 0 && c >= 0;
}

inline void work()
{
    int n, c, m;
    scanf("%d%d%d", &n, &c, &m);
    int a[c + 1];
    int b[n + 1];
    memset(a, 0, sizeof(a));
    memset(b, 0, sizeof(b));
    for (int i = 0; i < m; ++i)
    {
        int x, y;
        scanf("%d%d", &x, &y);
        ++a[y];
        ++b[x];
    }
    int down = 0;
    for (int i = 1; i <= c; ++i) down = max(down, a[i]);
    int cur = 0, tot = 0;
    for (int i = 1; i <= n; ++i)
    {
        tot += b[i];
        int need = tot / i + (tot % i != 0);
        cur = max(cur, need);
    }
    down = max(down, cur);
    printf("%d", down);
    int ppp = 0;
    for (int i = 1; i <= n; ++i)
    {
        if (b[i] > down) ppp += b[i] - down;
    }
    printf(" %d\n", ppp);
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
