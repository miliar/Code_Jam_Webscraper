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

int const maxN = 60;

int ar[maxN];
vector<int> p[maxN];
int last[maxN];

int low(int v)
{
    return v - v / 10;
}

int up(int v)
{
    return v + v / 10;
}

int solve()
{
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &ar[i]);
        last[i] = -1;
    }
    for (int i = 0; i < n; ++i)
    {
        p[i].clear();
        p[i].resize(m);
        for (int j = 0; j < m; ++j)
        {
            scanf("%d", &p[i][j]);
        }
        sort(p[i].begin(), p[i].end());
    }
    int ans = 0;
    for (int s = 1; s < 1000100; ++s)
    {
        bool good = true;
        int best = 1e9;
        for (int i = 0; i < n; ++i)
        {
            if (ar[i] * (long long)s >= 100000000)
            {
                return ans;
            }
            int cur = ar[i] * s;
            int l = low(cur);
            int r = up(cur);
            auto lowr = lower_bound(p[i].begin() + last[i] + 1, p[i].end(), l);
            if (lowr == p[i].end() || *lowr > r)
            {
                good = false;
                break;
            }
            auto upr = lower_bound(p[i].begin() + last[i] + 1, p[i].end(), r + 1);
            upr--;
            if (lowr > upr)
            {
                good = false;
                break;
            }
            best = min(best, (upr - lowr) + 1);
        }
        if (good)
        {
            ans += best;
            for (int i = 0; i < n; ++i)
            {
                int cur = ar[i] * s;
                int l = low(cur);
                int r = up(cur);
                int dist = lower_bound(p[i].begin() + last[i] + 1, p[i].end(), l) - p[i].begin();
                last[i] = dist + best - 1;
            }
        }
    }
    return ans;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int tn = 1; tn <= t; ++tn)
    {
        printf("Case #%d: %d\n", tn, solve());
    }
    return 0;
}