#include <bits/stdc++.h>

using namespace std;

const int N = 1005;
const long double PI = 3.141592653589793L;

int n, k;
int r[N], h[N], t[N];
long long dp[N][N], best[N][N];

bool cmp(int a, int b) {
    return r[a] < r[b];
}

void solveTest() {
    
    scanf("%d %d", &n, &k);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            dp[i][j] = best[i][j] = 0;
        }
    }
    
    for (int i = 1; i <= n; i++) {
        scanf("%d %d", &r[i], &h[i]);
        t[i] = i;
    }
    
    sort(t + 1, t + 1 + n, cmp);
    
    for (int i = 1; i <= n; i++) {
        int w = t[i];
        for (int j = 1; j <= k; j++) {
            dp[i][j] = (long long)r[w] * h[w] + best[i - 1][j - 1];
            best[i][j] = max(best[i - 1][j], dp[i][j]);
        }
    }
    
    long double best = 0.0;
    for (int i = k; i <= n; i++) {
        best = max(best, (long double)dp[i][k] + (long double)r[t[i]] / 2.0 * r[t[i]]);
    }
    
    printf("%.10Lf\n", PI * best * 2);    
}

int main() {

    int t;
    scanf("%d", &t);
    for (int test = 1; test <= t; test++) {
        printf("Case #%d: ", test);
        solveTest();
    }
    
    return 0;
}