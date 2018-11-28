#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n, c, m;
int a[1024], b[1024];
int d[1024], e[1024];

void read() {
    scanf("%d%d%d", &n, &c, &m);
    memset(d, 0, sizeof d);
    memset(e, 0, sizeof e);

    for (int i = 0; i < m; i++) {
        scanf("%d%d", &a[i], &b[i]);
        d[ a[i] ] ++;
        e[ b[i] ] ++;
    }
}

int can(int x) {
    int carry = 0;
    int ans = 0;

    for (int i = n; i >= 1; i--) {
        if (d[i] > x) {
            carry += d[i] - x;
            ans += d[i] - x;
        } else {
            carry -= x - d[i];
        }
        if (carry < 0) carry = 0;
    }

    if (carry) {
        return -1;
    }
    return ans;
}

void solve() {
    int mn = 0;
    for (int i = 0; i <= c; i++) {
        mn = max(mn, e[i]);
    }

    //printf ("%d\n", can(5));return ;

    int l = mn, r = m;
    while (l < r) {
        int mid = l + (r - l) / 2;

        if (can(mid) != -1) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }

    printf("%d %d\n", l, can(l));
}

int main() {
    int i, cases;

    scanf("%d", &cases);
    for (i = 1; i <= cases; i++) {
        read();
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

