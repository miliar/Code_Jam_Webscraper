#include <cstdio>
#include <algorithm>

using namespace std;

long long a[20];
long long dp[20][10][2];

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int c = 0, j, k, l, r;
        long long n, ans = 0;
        
        scanf("%lld", &n);
        
        while (n > 0) {
            a[c++] = n % 10;
            n /= 10;
        }
        
        for (j = 0; j <= c; j++) {
            for (k = 0; k < 10; k++) {
                for (l = 0; l < 2; l++) {
                    dp[j][k][l] = -1;
                }
            }
        }
        
        dp[0][0][0] = 0;
        
        for (j = 0; j < c; j++) {
            for (k = 0; k < 10; k++) {
                for (l = 0; l < 2; l++) {
                    if (dp[j][k][l] == -1) continue;
                    
                    for (r = k; r < 10; r++) {
                        long long x = dp[j][k][l] * 10 + r;
                        
                        if (l == 0 && r > a[c - j - 1]) break;
                        
                        if (l == 0 && r == a[c - j - 1]) {
                            dp[j + 1][r][0] = x;
                        } else {
                            dp[j + 1][r][1] = max(dp[j + 1][r][1], x);
                        }
                    }
                }
            }
        }
        
        for (j = 0; j < 10; j++) {
            for (k = 0; k < 2; k++) {
                ans = max(ans, dp[c][j][k]);
            }
        }
        
        printf("Case #%d: %lld\n", i + 1, ans);
    }
    
    return 0;
}
