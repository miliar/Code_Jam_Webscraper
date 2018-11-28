#include <iostream>
#include <cstdio>

int dp[105][105][105][4] = {};
int k;

inline int maximum(int a, int b)
{
    return (a > b ? a : b);
}

int mc(int m1, int m2, int m3, int rem)
{
    if (m1 == 0 && m2 == 0 && m3 == 0)
        return 0;
    else if (dp[m1][m2][m3][rem] == -1)
    {
        dp[m1][m2][m3][rem] = 0;
        if (m1)
        {
            if ((1 + rem) % k == 0)
                dp[m1][m2][m3][rem] = maximum(dp[m1][m2][m3][rem], mc(m1-1, m2, m3, 0) + ((m1-1) || m2 || m3));
            else
                dp[m1][m2][m3][rem] = maximum(dp[m1][m2][m3][rem], mc(m1-1, m2, m3, (1 + rem)%k));
        }
        if (m2)
        {
            if ((2 + rem) % k == 0)
                dp[m1][m2][m3][rem] = maximum(dp[m1][m2][m3][rem], mc(m1, m2-1, m3, 0) + (m1 || (m2-1) || m3));
            else
                dp[m1][m2][m3][rem] = maximum(dp[m1][m2][m3][rem], mc(m1, m2-1, m3, (2 + rem)%k));
        }
        if (m3)
        {
            if ((3 + rem) % k == 0)
                dp[m1][m2][m3][rem] = maximum(dp[m1][m2][m3][rem], mc(m1, m2, m3-1, 0) + (m1 || m2 || (m3-1)));
            else
                dp[m1][m2][m3][rem] = maximum(dp[m1][m2][m3][rem], mc(m1, m2, m3-1, (3 + rem)%k));
        }
    }
    return dp[m1][m2][m3][rem];
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    std::cin >> tc;
    for (int t = 0; t < tc; t++)
    {
        int n, x, m1 = 0, m2 = 0, m3 = 0, ans = 0;
        std::cin >> n >> k;
        for (int i = 0; i < n; i++)
        {
            std::cin >> x;
            if (x % k == 0)
                ans++;
            else if (x % k == 1)
                m1++;
            else if (x % k == 2)
                m2++;
            else if (x % k == 3)
                m3++;
            //others not possible given constraints
        }
        for (int i = 0; i <= 100; i++)
            for (int j = 0; j <= 100; j++)
                for (int u = 0; u <= 100; u++)
                    for (int v = 0; v <= 3; v++)
                        dp[i][j][u][v] = -1;
        if (m1 || m2 || m3)
            std::cout << "Case #" << t+1 << ": " << ans + mc(m1, m2, m3, 0) + 1 << '\n';
        else
            std::cout << "Case #" << t+1 << ": " << ans + mc(m1, m2, m3, 0) << '\n';
    }
}
