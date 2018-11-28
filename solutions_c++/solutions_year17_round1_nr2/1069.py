#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

int n, p;
ll r[16], q[16][16];
bool used[16][16];

inline int lo(int x) { return x - 1000; }
inline int hi(int x) { return x + 1000; }

inline int valid(ll x, ll y, ll c)
{
    return (9 * c * x <= 10 * y && 10 * y <= 11 * c * x);
}

int check(ll x, ll y)
{
    ll v = y / x;
    ll l = lo(v), h = hi(v);
    for (ll i = l; i <= h; i++)
        if (valid(x, y, i)) return true;
    return false;
}

int check(ll x1, ll y1, ll x2, ll y2)
{
    ll v1 = y1 / x1, v2 = x2 / y2;
    ll l1 = lo(v1), h1 = hi(v1), l2 = lo(v2), h2 = hi(v2);
    for (ll i = l1; i <= h1; i++)
        if (valid(x1, y1, i) && valid(x2, y2, i)) return true;
    for (ll i = l2; i <= h2; i++)
        if (valid(x1, y1, i) && valid(x2, y2, i)) return true;
    return false;
}

int back(int c)
{
    int ret = 0;
    if (c == p) return 0;
    for (int j = 0; j < p; j++) {
        if (used[1][j]) continue;
        ll x1 = r[0], x2 = r[1];
        ll y1 = q[0][c], y2 = q[1][j];
        if (check(x1, y1, x2, y2)) {
            used[0][c] = true, used[1][j] = true;
            ret = max(ret, 1 + back(c + 1));
            used[0][c] = false, used[1][j] = false;
        }
    }
    ret = max(ret, back(c + 1));
    return ret;
}

int solve()
{
    int ret = 0;
    if (n == 1) {
        int x = r[0], y;
        for (int i = 0; i < p; i++) {
            y = q[0][i];
            if (check(x, y)) ++ret;
        }
        return ret;
    }
    ret = back(0);
    return ret;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        memset(used, 0, sizeof(used));
        scanf("%d%d", &n, &p);
        for (int i = 0; i < n; i++)
            scanf("%lld", &r[i]);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < p; j++)
                scanf("%lld", &q[i][j]);
        /*
        if (tc == 36) {
            printf("======\n");
            printf("%d %d\n", n, p);
            for (int i = 0; i < n; i++) printf("%lld ", r[i]);
            printf("\n");
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < p; j++) {
                    printf("%lld ", q[i][j]);
                }
                printf("\n");
            }
            printf("======\n");
        }
        */
        int ans = solve();
        printf("Case #%d: %d\n", tc, ans);
    }
    return 0;
}
