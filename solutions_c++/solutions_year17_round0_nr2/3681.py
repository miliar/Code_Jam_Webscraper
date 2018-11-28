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
const int MAX_N = 10010;

int T, cases = 0;
ll n;
ll pw[10][20], pw10[20];

ll solve() {
    ll ans = 0, tmp = n;
    int len = 0, digit[20];

    while (tmp) {
        digit[++len] = tmp % 10;
        tmp = tmp / 10;
    }

    for (int i = len; i >= 1; --i) {
        ll pre = ans;
        for (int j = 0; j < 10; ++j) {
            if (pre + pw[j][i] <= n) ans = pre + j * pw10[i];
            else break;
        }
   //     printf("i = %d ans = %lld\n", i, ans);
    }
    return ans;
}

int main() {
    freopen("2.in", "r", stdin);
    freopen("2.out", "w", stdout);

    pw10[1] = 1;
    for (int i = 2; i <= 18; ++i) pw10[i] = pw10[i - 1] * 10;

    for (int i = 1; i < 10; ++i) {
        for (int j = 1; j <= 18; ++j) {
            pw[i][j] = pw[i][j - 1] * 10 + i;
        //    printf("pw[%d][%d] = %lld\n", i, j, pw[i][j]);
        }
    }

    scanf("%d", &T);
    while (T--) {
        scanf("%lld", &n);
        if (n == (ll)(1e18)) printf("Case #%d: 99999999999999999\n", ++cases);
        else printf("Case #%d: %lld\n", ++cases, solve());
    }
    return 0;
}
