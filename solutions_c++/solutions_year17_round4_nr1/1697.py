#include <bits/stdc++.h>

#define mp make_pair

typedef std::pair<int, int> pii;

void get_ans(int n, int p)
{
    int g[n];
    int cnt[p];
    for (int i = 0; i < p; ++i)
        cnt[i] = 0;
    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &g[i]);
        g[i] = g[i] % p;
        ++cnt[g[i]];
    }
    if (p == 2)
    {
        printf("%d\n", cnt[0] + (cnt[1] + 1) / 2);
    }
    else if (p == 3)
    {
        printf("%d\n", cnt[0] + std::min(cnt[1], cnt[2]) + (std::max(cnt[1], cnt[2]) - std::min(cnt[1], cnt[2]) + 2) / 3);
    }
}

int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int ch;
    scanf("%d", &ch);
    ch = 0;
    int n, p;
    while (scanf("%d %d", &n, &p) == 2)
    {
        printf("Case #%d: ", ++ch);
        get_ans(n, p);
    }
    return 0;
}