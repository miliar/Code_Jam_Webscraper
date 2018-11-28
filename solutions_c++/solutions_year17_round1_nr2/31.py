#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <string>
#include <cstring>
#include <complex>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair

const int N = 100;
int n, m;
int a[N];
int b[N][N];
int l[N][N];
int r[N][N];
int p[N];

int getL(int x, int y)
{
    return (10 * y - 1) / (11 * x) + 1;
}
int getR(int x, int y)
{
    return (10 * y) / (9 * x);
}

int solve()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            scanf("%d", &b[i][j]);
        sort(b[i], b[i] + m);
        for (int j = 0; j < m; j++)
        {
            l[i][j] = getL(a[i], b[i][j]);
            r[i][j] = getR(a[i], b[i][j]);
        }
    }
    for (int i = 0; i < n; i++)
        p[i] = 0;
    int ans = 0;
    while(true)
    {
        bool ended = false;
        for (int i = 0; i < n; i++)
            if (p[i] == m)
            {
                ended = true;
                break;
            }
        if (ended) break;
        int L = 0, R = (int)1e9, Rid = -1;
        for (int i = 0; i < n; i++)
        {
            L = max(L, l[i][p[i]]);
            if (R > r[i][p[i]])
            {
                R = r[i][p[i]];
                Rid = i;
            }
        }
        if (L > R)
        {
            p[Rid]++;
            continue;
        }
        ans++;
        for (int i = 0; i < n; i++)
            p[i]++;
    }
    return ans;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        printf("Case #%d: %d\n", i, solve());
    }

    return 0;
}
