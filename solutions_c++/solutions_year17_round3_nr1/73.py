//
// Created by Denis Mukhametianov on 30.04.17.
//

#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

pair<int, int> a[1046];
double dp[1046][1046];

const double PI = atan2(0, -1.);


bool doubleEqual(double a, double b) {
    return fabs(a - b) < 1e-6;
}

void solveA(int tc) {
    int n, k;
    scanf("%d%d", &n, &k);
    for(int i = 0; i < n; i++) {
        scanf("%d%d", &a[i].first, &a[i].second);
    }
    sort(a, a + n);
    reverse(a, a + n);
    for(int i = 0; i <= n; i++)
        for(int j = 0; j <= n; j++)
            dp[i][j] = -1;
    dp[0][0] = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j <= k; j++) {
            if(doubleEqual(dp[i][j], -1))
                continue;
            double square = 2. * PI * a[i].first * a[i].second;
            if(j == 0)
                square += PI * a[i].first * a[i].first;
            //printf("go %.5lf\n", square);
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + square);
        }
    }
//    for(int i = 0; i <= n; i++) {
//        for (int j = 0; j <= k; j++)
//            printf("%.5lf ", dp[i][j]);
//        printf("\n");
//    }
    printf("Case #%d: %.8lf\n", tc + 1, dp[n][k]);
}

void solveA() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++)
        solveA(i);
}