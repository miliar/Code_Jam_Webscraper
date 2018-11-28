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

const int N = (int)1e6;

int n, m;
int a[4];
int b[4];
int dp[N];

int solve()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; i++)
        a[i] = 0;
    for (int i = 0; i < n; i++)
    {
        int x;
        scanf("%d", &x);
        a[x % m]++;
    }
    int all = 1;
    for (int i = 1; i < m; i++)
        all *= a[i] + 1;
    for (int i = 0; i < all; i++)
        dp[i] = 0;
    for (int mask = 0; mask < all; mask++)
    {
        int cur = mask;
        int sum = 0;
        for (int i = 1; i < m; i++)
        {
            b[i] = cur % (a[i] + 1);
            cur /= a[i] + 1;
            sum += b[i] * i;
        }
        sum %= m;
        int w = dp[mask] + (int)(sum == 0);
        int C = 1;
        for (int i = 1; i < m; i++)
        {
            if (b[i] != a[i])
                dp[mask + C] = max(dp[mask + C], w);
            C *= a[i] + 1;
        }
    }
    return a[0] + dp[all - 1];
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
