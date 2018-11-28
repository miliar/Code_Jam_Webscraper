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

const int N = (int)1000 + 123;
const int MOD = (int)1e9 + 7;
const int inf = (int)5e8;
const long long infll = (long long)1e17;

const int M = 10;

int a[M];
int use[3] = {0, 2, 4};
char val[M] = {'R', 'Y', 'B'};




void solve() {
    int n;
    scanf("%d", &n);
    int total = 0;
    for (int i = 0; i < 6; ++i) {
        scanf("%d", &a[i]);
        total += a[i];
    }
    vector<int> cnt(3);
    int mx = 0;
    for (int i = 0; i < 3; ++i) {
        cnt[i] = a[use[i]];
        if (cnt[i] > cnt[mx]) {
            mx = i;
        }
        if (cnt[i] > (n + 1) / 2) {
            printf("IMPOSSIBLE\n");
            return;
        }
    }
    string ans(n, '#');
    for (int i = 0; i < cnt[mx]; ++i) {
        ans[2 * i] = val[mx];
    }
    int nmx = mx == 0 ? 1 : 0;
    int lst = -1;
    for (int i = 0; i < 3; ++i) {
        if (i != mx) {
            if (cnt[i] > cnt[nmx]) {
                nmx = i;
            }
        }
    }
    for (int i = 0; i < 3; ++i) {
        if (nmx != i && mx != i) {
            lst = i;
        }
    }
    for (int i = 0; i < cnt[nmx] - cnt[lst]; ++i) {
        ans[2 * i + 1] = val[nmx];
    }
    int k = 0;
    for (int i = 0; i < n; ++i) {
        if (ans[i] == '#') {
            if (k % 2) {
                ans[i] = val[lst];
            } else {
                ans[i] = val[nmx];
            }
            ++k;
        }
    }
    for (int i = 0; i < n; ++i) {
        if (ans[i] == ans[(i - 1 + n) % n]) {
            printf("IMPOSSIBLE\n");
            return;
        }
    }
    printf("%s\n", ans.c_str());

}

int main() {
#ifdef __APPLE__
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i)  {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
