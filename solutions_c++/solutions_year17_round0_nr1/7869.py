#include <algorithm>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

#ifdef __APPLE__
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...)
#endif

const int N = (int)1e6 + 123;
const int MOD = (int)1e9 + 7;
const int inf = (int)5e8;
const long long infll = (long long)1e17;

void solve() {
    string s;
    int k;
    cin >> s >> k;
    int n = s.size();
    for (int i = 0; i < n; ++i) {
        if (s[i] == '+') {
            s[i] = '1';
        } else {
            s[i] = '0';
        }
    }
    int ans = 0;
    for (int i = 0; i + k - 1 < n; ++i) {
        if (s[i] == '0') {
            ++ans;
            for (int j = i; j < i + k; ++j) {
                s[j] = (s[j] - '0') ^ 1 + '0';
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        if (s[i] == '0') {
            printf("IMPOSSIBLE");
            return;
        }
    }
    printf("%d", ans);
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
        printf("\n");
    }
    return 0;
}
