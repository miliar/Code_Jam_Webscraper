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
typedef long double ldouble;

const double EPS = 1e-9;
const ldouble PI = 3.141592653589793238462;

template<typename T>
inline T sq(T a) { return a * a; }

const int MAX_N = 1005;

ll dp[MAX_N][MAX_N];
ii pan[MAX_N];

int main() {
    freopen("a-large.in", "rt", stdin);
    freopen("a-large.out", "wt", stdout);
    int t;
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        int n, k;
        scanf("%d %d", &n, &k);
        for (int i = 1; i <= n; i++)
            scanf("%d %d", &pan[i].fi, &pan[i].se);
        sort(pan + 1, pan + n + 1, greater<ii>());
        //memset(dp, 0, sizeof dp);
        for (int i = 1; i <= n; i++) {
            dp[i][1] = max(dp[i - 1][1],
                sq(( ll )pan[i].fi) + pan[i].fi * 2LL * pan[i].se);
            for (int j = 2; j <= i; j++) {
                dp[i][j] = max(dp[i - 1][j],
                    dp[i - 1][j - 1] + pan[i].fi * 2LL * pan[i].se);
            }
        }
        cout << "Case #" << tc << ": " << setprecision(8) << fixed <<
                ( ldouble )(PI * dp[n][k]) << endl;
    }
    return 0;
}

