#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define pf push_front
#define iter(v, i) for (__typeof__((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define fast_io_without_cstdio ios_base::sync_with_stdio(false), cin.tie(NULL)
#define all(v) (v).begin(), (v).end()

#ifdef __linux__
#define gc getchar_unlocked
#define pc putchar_unlocked
#else
#define gc getchar
#define pc putchar
#endif

#if __cplusplus <= 199711L
template<class BidirIt>
BidirIt prev(BidirIt it, typename iterator_traits<BidirIt>::difference_type n = 1) {
    advance(it, -n);
    return it;
}

template<class ForwardIt>
ForwardIt next(ForwardIt it, typename iterator_traits<ForwardIt>::difference_type n = 1) {
    advance(it, n);
    return it;
}
#endif

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const double EPS = 1e-9;
const double PI = 3.141592653589793238462;

template<typename T>
inline T sq(T a) { return a * a; }

const int MAXD = 20;

ll memo[MAXD][11];

ll dp(int n, int d) {
    if (n == 1) return 1;
    if (n == 0) return 1;
    if (memo[n][d] != -1)
        return memo[n][d];
    ll ret = 0;
    for (int i = d; i <= 9; i++)
        ret += dp(n - 1, i);
    return memo[n][d] = ret;
}

ll solve(ll num) {
    char digs[MAXD];
    sprintf(digs, "%lld", num);
    int n = strlen(digs);

    ll ret = 0;
    bool isok = true;
    for (int i = 1; i < n; i++)
        if (digs[i] < digs[i - 1])
            isok = false;
    if (isok) ret++;

    for (int i = 1; i < n; i++)
        for (int d = 1; d <= 9; d++)
            ret += dp(i, d);

    int last = 1;
    for (int i = 0; i < n; i++) {
        if (digs[i] < digs[i - 1]) break;
        for (int d = last; d < digs[i] - '0'; d++)
            ret += dp(n - i, d);
        last = digs[i] - '0';
    }
    return ret;
}

int main() {
    freopen("B-large.in", "rt", stdin);
    freopen("B-large.out", "wt", stdout);
    memset(memo, -1, sizeof memo);
    int t, tc = 1;
    scanf("%d", &t);
    while (t--) {
        ll n;
        scanf("%lld", &n);
        ll lo = 1, hi = n, ans = -1;
        while (lo < hi) {
            ll mid = (lo + hi) / 2LL;
            if (solve(hi) - solve(mid) > 0) {
                lo = mid + 1;
            } else /*if (solve(mid) - solve(mid - 1) > 0) {
                ans = mid;
                break;
            } else */{
                hi = mid;
            }
        }
        printf("Case #%d: %lld\n", tc++, lo);
    }
    return 0;
}

