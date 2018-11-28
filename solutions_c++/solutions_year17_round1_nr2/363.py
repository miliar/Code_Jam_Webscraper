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

int T, n, P, cases = 0, ans;
int need[60], store[60][60];

void solve() {
    if (n == 1) {
        for (int i = 1; i <= P; ++i) {
            for (int k = 1; ; ++k) {
                ll t = 1ll * k * need[1];

                ll low = t * 0.9 + 0.5, high = t * 1.1;

                if (low > store[1][i]) break;
                if (store[1][i] >= low && store[1][i] <= high) {
                    ans++;
                    break;
                }
            }
        }
    } else {
        sort(store[2] + 1, store[2] + n + 1);

        do {
            int now = 0;
            for (int i = 1; i <= P; ++i) {
                int high1 = 1.0 * need[1] / 0.9, low1 = 1.0 * need[1] / 1.1 + 0.5;
                int high2 = 1.0 * need[2] / 0.9, low2 = 1.0 * need[2] / 1.1 + 0.5;
                if (low1 > low2) swap(low1, low2), swap(high1, high2);
                if (high1 >= low2) now++;

                continue;

                for (int k = 1; ; ++k) {
                    ll t1 = 1ll * k * need[1], t2 = 1ll * k * need[2];

                    ll low1 = t1 * 0.9 + 0.5, high1 = t1 * 1.1;
                    ll low2 = t2 * 0.9 + 0.5, high2 = t2 * 1.1;

                    if (low1 > store[1][i] || low2 > store[2][i]) break;

                    if (store[1][i] >= low1 && store[1][i] <= high1 &&
                        store[2][i] >= low2 && store[2][i] <= high2) {
                        now++;
                        break;
                    }
                }
            }
            ans = max(ans, now);
        } while (next_permutation(store[2] + 1, store[2] + n + 1));
    }
}

int main() {    
   // freopen("2.in", "r", stdin);
   // freopen("2.out", "w", stdout);
  //  freopen("22.out", "w", stdout);

    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &n, &P);

        for (int i = 1; i <= n; ++i) {
            scanf("%d", &need[i]);
        }
                  
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= P; ++j) {
                scanf("%d", &store[i][j]);
            }
        }

        ans = 0;
        solve();

        printf("Case #%d: %d\n", ++cases, ans);
    }
    return 0;
}
    
