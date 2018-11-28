#include <algorithm>
#include <cassert>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>

const double inf = 1e18;

int d[110][110];
int e[110];
int s[110];

double dp[110];

int main() {
    // std::freopen("C:/Users/Admin/Documents/Visual Studio 2015/Projects/hackerrank/Debug/in.txt", "r", stdin);
    // std::freopen("C:/Users/Admin/Documents/Visual Studio 2015/Projects/hackerrank/Debug/out.txt", "w", stdout);

    int tn;
    std::cin >> tn;

    for (int ti = 1; ti <= tn; ++ti) {
        int n;
        std::cin >> n;

        int q;
        std::cin >> q;

        for (int i = 1; i <= n; ++i) {
            std::cin >> e[i] >> s[i];
        }

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                std::cin >> d[i][j];
            }
        }

        int u, v;
        std::cin >> u >> v;

        for (int i = 1; i <= n; ++i) {
            dp[i] = inf;
        }

        dp[1] = 0;
        for (int i = 1; i <= n; ++i) {
            int tot_d = 0;
            for (int j = i + 1; j <= n; ++j) {
                tot_d += d[j - 1][j];
                if (e[i] < tot_d) {
                    break;
                }
                double t = (double)(tot_d) / s[i];
                dp[j] = std::min(dp[j], dp[i] + t);
            }
        }

        double answer = dp[n];
        assert(answer < inf);
        std::cout << "Case #" << ti << ": " << std::fixed << std::setprecision(10) << answer << std::endl;
    }
}