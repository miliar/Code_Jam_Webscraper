#include <bits/stdc++.h>
#define TR(c, it) for(__typeof(c.begin()) it = c.begin(); it != c.end(); ++it)
#define FOR(i, a, b) for(int i = (a), _b = (b); i < _b; ++i)
#define FORD(i, a, b) for(int i = (a), _b = (b); i >= _b; --i)
#define FORE(i, a, b) for(int i = (a), _b = (b); i <= _b; ++i)
#define SZ(c) (int) (c).size()

using namespace std;
const double PI = acos(-1);
const int N = 1010;

int n, k;
pair<int, int> a[N];
long long c[N];
multiset<long long> qq;

int main() {
    //freopen("A.inp", "r", stdin);
    //freopen("A.out", "w", stdout);
    //ios::sync_with_stdio(false); cin.tie(NULL);
    int tests;
    scanf("%d", &tests);
    for (int test = 1; test <= tests; ++test) {
        scanf("%d %d", &n, &k);
        FOR(i, 0, n) scanf("%d %d", &a[i].first, &a[i].second);
        sort(a, a + n);
        /*FOR(i, 0, n) {
            printf("%d %d %I64d\n", a[i].first, a[i].second, (long long)a[i].first * a[i].second);
        }*/
        qq.clear();
        long long value = 0;
        long long best = 0;
        FORE(i, 0, k - 1) {
            long long d = (long long)a[i].first * a[i].second;
            qq.insert(d);
            value += d;
            if (i == k - 1) {
                best = max(best, value * 2 + (long long)a[i].first * a[i].first);
            }
        }
        FOR(i, k, n) {
            long long u = *qq.begin();
            long long d = (long long)a[i].first * a[i].second;
            best = max(best, (value - u + d) * 2 + (long long)a[i].first * a[i].first );
            qq.insert(d);
            value += d;
            if (SZ(qq) > k) {
                d = *qq.begin(); qq.erase(qq.begin());
                value -= d;
            }
        }

        double ans = PI * best;
        printf("Case #%d: %.08lf\n", test, ans);

    }
    return 0;
}

