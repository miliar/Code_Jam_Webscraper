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
const double PI = 3.141592653589793238462;

template<typename T>
inline T sq(T a) { return a * a; }

const int MAX_N = 105;

int e[MAX_N], v[MAX_N];
int d[MAX_N][MAX_N];
ldouble dp[MAX_N];

int main() {
    freopen("c-small.in", "rt", stdin);
    freopen("c-small.out", "wt", stdout);
    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        int n, q;
        cin >> n >> q;
        for (int i = 1; i <= n; i++)
            cin >> e[i] >> v[i];
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                cin >> d[i][j];
        printf("Case #%d:", tc);
        while (q--) {
            int x, y;
            cin >> x >> y;
            dp[1] = 0;
            for (int i = 2; i <= n; i++) {
                ll dist = 0;
                dp[i] = 1e18;
                for (int j = i - 1; j >= 1; j--) {
                    dist += d[j][j + 1];
                    if (e[j] >= dist)
                        dp[i] = min(dp[i], dp[j] + ( ldouble )dist / v[j]);
                }
            }
            cout << ' ' << setprecision(7) << fixed << dp[n];
        }
        puts("");
    }
    return 0;
}

