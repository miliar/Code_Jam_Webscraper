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


bool is_tidy(long long n) {
    int prev = 0;
    vector<int> digits;
    while (n > 0) {
        digits.push_back(n % 10);
        n /= 10;
    }
    reverse(digits.begin(), digits.end());
    for (auto i : digits) {
        if (prev > i) {
            return false;
        }
        prev = i;
    }
    return true;
}

void solve() {
    long long n;
    scanf("%lld", &n);
    for (long long i = n; i >= 1; --i) {
        if (is_tidy(i)) {
            printf("%lld", i);
            return;
        }
    }
}

int main() {
#ifdef __APPLE__
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t = 1;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }
    return 0;
}
