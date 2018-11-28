#include <cstdio>
#include <cassert>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long llong;

bool ok(llong n) {
    char buf[25];
    sprintf(buf, "%lld", n);
    int l = strlen(buf);
    return is_sorted(buf, buf + l);
}

void solve(int cs) {
    llong n;
    scanf("%lld", &n);
    char buf[25];
    sprintf(buf, "%lld", n);
    llong ans = -1;
    if (ok(n)) {
        ans = max(ans, n);
    }
    for (llong mul = 1, cur = n, dv = n; dv > 0; ) {
        int x = dv % 10;
        cur -= x * mul;
        mul *= 10;
        dv /= 10;
        if (ok(cur - 1)) {
            ans = max(ans, cur - 1);
        }
    }
    assert(ans != -1);
    printf("Case #%d: %lld\n", cs, ans);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        solve(i + 1);
        fflush(stdout);
        fprintf(stderr, "%d\n", i);
    }
}
