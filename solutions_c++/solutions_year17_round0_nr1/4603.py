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

const int MAXN = 1005;

char str[MAXN];

int main() {
    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out", "wt", stdout);
    int t, tc = 1;
    scanf("%d", &t);
    while (t--) {
        int n, k;
        scanf("%s %d", str, &k);
        n = strlen(str);
        int ans = 0;
        for (int i = 0; i + k - 1 < n; i++) {
            if (str[i] == '-') {
                ans++;
                for (int j = i; j < i + k; j++)
                    if (str[j] == '-') str[j] = '+';
                    else str[j] = '-';
            }
        }
        bool found = true;
        for (int i = 0; i < n; i++)
            if (str[i] == '-')
                found = false;
        printf("Case #%d: ", tc++);
        if (found)
            printf("%d\n", ans);
        else
            puts("IMPOSSIBLE");
    }
    return 0;
}

