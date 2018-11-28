#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#ifdef __APPLE__
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...)
#endif

const int N = (int)1e6 + 1;
const int MOD = (int)1e9 + 7;
const int inf = (int)5e8;
const long long infll = (long long)1e17;

double area(double r, double h) {
    return acos(-1.0) * 2 * r * h;
}

struct Item {
    double r, h;
    Item() {}
    Item(double r, double h) : r(r), h(h) {}
};

void solve() {
    int n, k;
    scanf("%d %d", &n, &k);
    vector<Item> a(n);
    for (int i = 0; i < n; ++i) {
        double r, h;
        scanf("%lf %lf", &r, &h);
        a[i] = Item(r, h);
    }
    sort(a.begin(), a.end(), [](const Item& lhs, const Item& rhs) {
            if (lhs.r != rhs.r) {
                return lhs.r > rhs.r;
            }
            return lhs.h > rhs.h;
    });
    vector<vector<double>> dp(n + 1, vector<double>(k + 1));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < k; ++j) {
            if (j == 0) {
                dp[i][1] = area(a[i].r, a[i].h) +
                    a[i].r * a[i].r * acos(-1.0);
            }  else {
                for (int now = i + 1; now < n; ++now) {
                    if (a[now].r <= a[i].r) {
                        dp[now][j + 1] = max(dp[now][j + 1],
                                dp[i][j] + area(a[now].r, a[now].h));
                    }
                }
            }
        }
    }
    double ans = 0;
    for (int i = 0; i < n; ++i) {
        ans = max(ans, dp[i][k]);
    }
    printf("%.10lf\n", ans);
}

int main() {
#ifdef __APPLE__
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
