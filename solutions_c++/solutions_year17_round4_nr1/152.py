#include <cstdio>
#include <algorithm>

using namespace std;

int a[4];
int dp[2][101][101][4];

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, p, ans = 0, j, k, l, r;
        
        scanf("%d %d", &n, &p);
        
        for (j = 0; j < 4; j++) a[j] = 0;
        
        for (j = 0; j < n; j++) {
            int x;
            
            scanf("%d", &x);
            
            a[x % p]++;
        }
        
        n -= a[0];
        
        for (j = 0; j < 2; j++) {
            for (k = 0; k <= n; k++) {
                for (l = 0; l <= n; l++) {
                    for (r = 0; r < p; r++) {
                        dp[j][k][l][r] = -1;
                    }
                }
            }
        }
        
        dp[0][0][0][0] = 0;
        
        for (j = 0; j < n; j++) {
            for (k = 0; k <= a[1]; k++) {
                for (l = 0; l <= a[2]; l++) {
                    for (r = 0; r < p; r++) {
                        int c = dp[0][k][l][r];
                        
                        if (c == -1) continue;
                        
                        if (r == 0) c++;
                        
                        if (k < a[1]) dp[1][k + 1][l][(r + 1) % p] = max(dp[1][k + 1][l][(r + 1) % p], c);
                        if (l < a[2]) dp[1][k][l + 1][(r + 2) % p] = max(dp[1][k][l + 1][(r + 2) % p], c);
                        if (j - k - l < a[3]) dp[1][k][l][(r + 3) % p] = max(dp[1][k][l][(r + 3) % p], c);
                    }
                }
            }
            
            for (k = 0; k <= a[1]; k++) {
                for (l = 0; l <= a[2]; l++) {
                    for (r = 0; r < p; r++) {
                        dp[0][k][l][r] = dp[1][k][l][r];
                        dp[1][k][l][r] = -1;
                    }
                }
            }
        }
        
        for (j = 0; j <= a[1]; j++) {
            for (k = 0; k <= a[2]; k++) {
                for (l = 0; l < p; l++) {
                    ans = max(ans, dp[0][j][k][l]);
                }
            }
        }
        
        ans += a[0];
        
        printf("Case #%d: %d\n", i + 1, ans);
    }
    
    return 0;
}
