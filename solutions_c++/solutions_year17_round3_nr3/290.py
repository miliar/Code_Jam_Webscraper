#include <bits/stdc++.h>

const int N = 60;
const double EPS = 1E-12;

int sgn(double x) {
    return x < -EPS ? -1 : x > EPS;
}

double dp[N][N], p[N], temp[N], u;
int n, k;

bool Check(double x) {
    double remain = u;
    for (int i = 1; i <= n; ++ i) {
        temp[i] = p[i];
        if (temp[i] < x) {
            if (x - temp[i] <= remain) {
                remain -= x - temp[i];
                temp[i] = x;
            } else {
                return false;
            }
        }
    }
    return true;
}

int main() {
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; ++ t) {
        scanf("%d%d%lf", &n, &k, &u);
        for (int i = 1; i <= n; ++ i) {
            scanf("%lf", p + i);
        }

        double lower = 0, upper = 1, result = -1;
        while (upper - lower > EPS) {
            double middle = (lower + upper) / 2;
            if (Check(middle)) {
                lower = result = middle;
            } else {
                upper = middle;
            }
        }
        Check(result);
        memcpy(p, temp, sizeof(temp));

        memset(dp, 0, sizeof(dp));
        dp[0][0] = 1;
        for (int i = 1; i <= n; ++ i) {
            for (int j = 0; j <= i; ++ j) {
                dp[i][j] = dp[i - 1][j] * (1 - p[i]);
                if (j > 0) {
                    dp[i][j] += dp[i - 1][j - 1] * p[i];
                }
            }
        }

        double answer = 0;
        for (int i = k; i <= n; ++ i) {
            answer += dp[n][i];
        }
        printf("Case #%d: %.7f\n", t, answer);
    }
    return 0;
}