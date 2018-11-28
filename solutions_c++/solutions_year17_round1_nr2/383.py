#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <set>
using namespace std;

typedef long long ll;
const int maxn = 50 + 5;
int R[maxn];
int Q[maxn][maxn];
int dp[maxn];
int n, p;

int main() {
    int T; scanf("%d", &T);
    for (int Cas = 1; Cas <= T; Cas++) {
        cin >> n >> p;
        memset(dp, 0, sizeof(dp));
        for (int i = 0; i < n; i++) cin >> R[i];
        int mx = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                cin >> Q[i][j];
                mx = max(mx, Q[i][j]);
            }
            sort(Q[i], Q[i] + p);
        }
        int ans = 0;
        for (int i = 1; i <= mx; i++) {
            bool flag = true;
            for (int j = 0; j < n; j++) {
                ll tmp = (ll)R[j] * i * 9;
                while(dp[j] < p && (ll)Q[j][dp[j]] * 10 < tmp) dp[j]++;
                if((ll)Q[j][dp[j]] * 10 > (ll)R[j] * i * 11 || dp[j] >= p) flag = false;
            }
            if (flag) {
                ans++;
                i--;
                for (int j = 0; j < n; j++) dp[j]++;
            }
        }
        printf("Case #%d: %d\n", Cas, ans);
    }
    return 0;
}
