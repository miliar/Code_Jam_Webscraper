// written at 16:47 on 30 Apr 2017
#include <bits/stdc++.h>

#define IOS std::ios::sync_with_stdio(false); std::cin.tie(nullptr); std::cout.tie(nullptr);
// #define __DEBUG__
#ifdef __DEBUG__
#define DEBUG(...) printf(__VA_ARGS__)
#else
#define DEBUG(...)
#endif
#define filename "C-small-1-attempt1"
#define setfile() freopen(filename".in.txt", "r", stdin); freopen(filename".ans.txt", "w", stdout);
#define resetfile() freopen("/dev/tty", "r", stdin); freopen("/dev/tty", "w", stdout); system("more " filename".ans.txt");
#define rep(i, j, k) for (int i = j; i < k; ++i)
#define irep(i, j, k) for (int i = j - 1; i >= k; --i)

using namespace std;

template <typename T>
inline T sqr(T a) { return a * a;};

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int > Pii;

const int MAX_N = 50 + 10;
int t, n, k;
double u, P[MAX_N], PP[MAX_N];
int main(void)
{
    setfile();
    cin >> t;
    for (int _ = 0; _ < t; _++) {
        double ans = 0;
        cin >> n >> k;
        cin >> u;
        for (int i = 0; i < n; i++)
            cin >> P[i];
        sort(P, P + n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) PP[j] = P[j];
            double tot = u;
            for (int j = 0; j <= i; j++) tot += PP[j];
            tot /= (i + 1);
            if (tot > 1) tot = 1;
            for (int j = 0; j <= i; j++) {
                if (PP[i] < tot) PP[j] = tot;
            }
            double tmp = 1.;
            for (int j = 0; j < n; j++) tmp *= PP[j];
            ans = max(ans, tmp);
        }
        printf("Case #%d: %f\n", _ + 1, ans);
    }
    resetfile();
    return 0;
}
