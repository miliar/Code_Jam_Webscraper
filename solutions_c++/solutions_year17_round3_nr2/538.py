#include <iostream>
#include <algorithm>
#include <cstring>

const int MAXN = 1440;

int dp[MAXN/2 + 10][MAXN/2 + 10][3][3];
int day[MAXN + 10];

int main()
{
    int T_T, t_t;
    std::cin >> T_T;
    for (t_t = 1; t_t <= T_T; ++t_t) {
        memset(dp, 0x3f3f3f3f, sizeof dp);
        int ac, aj;
        std::cin >> ac >> aj;
        memset(day, 0, sizeof day);
        for (int i = 0; i < ac; ++i) {
            int l, r;
            std::cin >> l >> r;
            for (int j = l; j < r; ++j) {
                day[j] = 1;
            }
        }
        for (int i = 0; i < aj; ++i) {
            int l, r;
            std::cin >> l >> r;
            for (int j = l; j < r; ++j) {
                day[j] = 2;
            }
        }
        if (day[1] != 1) {
            dp[1][0][1][1] = 1;
        } 
        if (day[1] != 2) {
            dp[0][1][2][2] = 1;
        }
        for (int i = 0; i <= MAXN/2; ++i) {
            for (int j = 0; j <= std::min(MAXN-i, MAXN/2); ++j) {
                if (i == 0 && j == 0) 
                    continue;
                for (int k = 1; k <= 2; ++k) {
                    if (day[i+j+1] != 1) {
                        if (dp[i][j][1][k] <= MAXN) 
                            dp[i+1][j][1][k] = std::min(dp[i+1][j][1][k], dp[i][j][1][k]);
                        if (dp[i][j][2][k] <= MAXN)
                            dp[i+1][j][1][k] = std::min(dp[i+1][j][1][k], dp[i][j][2][k] + 1);
                    }
                    if (day[i+j+1] != 2) {
                        if (dp[i][j][1][k] <= MAXN) 
                            dp[i][j+1][2][k] = std::min(dp[i][j+1][2][k], dp[i][j][1][k] + 1);
                        if (dp[i][j][2][k] <= MAXN)
                            dp[i][j+1][2][k] = std::min(dp[i][j+1][2][k], dp[i][j][2][k]);
                    }
                }
            }
        }
        int res = 0x3f3f3f3f;
        res = std::min(res, dp[MAXN>>1][MAXN>>1][1][1]-1);
        res = std::min(res, dp[MAXN>>1][MAXN>>1][2][2]-1);
        res = std::min(res, dp[MAXN>>1][MAXN>>1][1][2]);
        res = std::min(res, dp[MAXN>>1][MAXN>>1][2][1]);
        std::cout << "Case #" << t_t << ": " << res << std::endl;
    }
}
