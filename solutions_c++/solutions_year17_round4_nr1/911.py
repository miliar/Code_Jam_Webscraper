#include <stdio.h>
#include <vector>
#include <algorithm>

int gcd(int a, int b)
{
    return b == 0 ? a : gcd(b, a % b);
}

void update(int &a, int b)
{
    if (a < b) a = b;
}

const int kN = 100 + 25;
int dp[kN][kN][kN];

int solve(int n, std::vector<int> vec)
{
    int p = vec.size();
    if (p == 2)
        return vec[0] + (vec[1] + 1) / 2;

    int ret = 0;

    if (p == 3) {
        std::vector<std::pair<int, int>> sol{{3, 0}, {1, 1}, {0, 3}};
        for (int x = 0; x <= n; ++ x) {
            for (int y = 0; y <= n; ++ y) {
                for (int z = 0; z <= n; ++ z) {
                    if (sol[0].first * x + sol[1].first * y + sol[2].first * z > vec[1]) continue;
                    if (sol[0].second * x + sol[1].second * y + sol[2].second * z > vec[2]) continue;
                    int tmp = vec[0] + x + y + z;
                    if (n - vec[0] - x * 3 - y * 2 - z * 3) tmp ++;
                    ret = std::max(ret, tmp);
                }
            }
        }
        return ret;
    }

    fprintf(stderr, "fuck");

    for (int i = 0; i <= vec[1]; ++ i) {
        for (int j = 0; j <= vec[2]; ++ j) {
            for (int k = 0; k <= vec[3]; ++ k) {
                int tmp = vec[0] + dp[i][j][k];
                if (vec[0] + i + j + k < n)
                    tmp ++;
                ret = std::max(ret, tmp);
            }
        }
    }
    return ret;
}

void init() {
    std::vector<std::tuple<int, int, int>> sol;
    int total = 0;
    for (int i = 0; i <= 4; ++ i) {
        for (int j = 0; j <= 4; ++ j) {
            for (int k = 0; k <= 4; ++ k) {
                if (i + j + k == 0) continue;
                if ((i + j * 2 + k * 3) % 4 == 0) {
                    sol.emplace_back(i, j, k);
                }
            }
        }
    }
    for (int i = 0; i < sol.size(); ++ i) {
        bool flag = true;
        for (int j = 0; j < sol.size(); ++ j) {
            int a, b, c, d, e, f;
            std::tie(a, b, c) = sol[i];
            std::tie(d, e, f) = sol[j];
            if (i != j && a >= d && b >= e && c >= f)
                flag = false;
        }
        if (flag)
            sol[total ++] = sol[i];
    }
    sol.resize(total);
    int n = 100;
    for (int i = 0; i <= n; ++ i) {
        for (int j = 0; i + j <= n; ++ j) {
            for (int k = 0; i + j + k <= n; ++ k) {
                for (auto t : sol) {
                    int a, b, c;
                    std::tie(a, b, c) = t;
                    update(dp[i + a][j + b][k + c], dp[i][j][k] + 1);
                }
            }
        }
    }
}

int main()
{
    init();
    int cas;
    scanf("%d", &cas);
    while (cas--) {
        int n, p;
        scanf("%d%d", &n, &p);
        std::vector<int> vec(p);
        for (int i = 0; i < n; ++ i) {
            int x;
            scanf("%d", &x);
            vec[x % p] ++;
        }
        static int ca = 0;
        printf("Case #%d: %d\n", ++ ca, solve(n, vec));
    }
}
