#include <bits/stdc++.h>
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
using namespace std;
typedef long long ll;
#define mp make_pair
#define fi first
#define se second
#define pb push_back

const double pi = acos(-1.0);
const int inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3fll;
const int MAX_N = 110;

int T, Hd, Ad, Hk, Ak, B, D, cases = 0;
int dp[MAX_N][MAX_N][MAX_N][MAX_N];

int solve(int i, int j, int p, int q, int d = 0) {
    if (i <= 0 || d > 10) return inf;
    if (p >= j) return 1;

    int* now = &dp[i][j][p][q];
    
 //   printf("i = %d j = %d p = %d q = %d\n", i, j, p, q);

    if (*now != inf) return *now;

    int ii = i - max(0, q);

    if (ii > 0) {
        *now = min(*now, solve(ii, j, p + B, q, d + 1) + 2); // buff
        *now = min(*now, solve(ii, j - p, p, q, d + 1) + 2); // attack
    }

    if (i != Hd && q > 0) *now = min(*now, solve(Hd - max(0, q), j, p, q, d + 1) + 2); // cure

    if (q > 0) *now = min(*now, solve(i - q + D, j, p, q - D, d + 1) + 2); // debuff
    return *now;
}

int main() {    
    freopen("3.in", "r", stdin);
    freopen("3.out", "w", stdout);

    scanf("%d", &T);
    while (T--) {
        scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
        memset(dp, 0x3f, sizeof (dp));
        int ans = solve(Hd, Hk, Ad, Ak);

        printf("Case #%d: ", ++cases);

        if (dp[Hd][Hk][Ad][Ak] == inf) puts("IMPOSSIBLE");
        else printf("%d\n", dp[Hd][Hk][Ad][Ak]);
    }
    return 0;
}
    
