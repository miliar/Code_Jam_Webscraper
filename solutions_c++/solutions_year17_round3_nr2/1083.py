#include <stdio.h>
#include <algorithm>
#include <iostream>

using namespace std;

#define DEBUG(x) cout<<#x<<":"<<x<<endl

struct Act {
    int s, e;
}act1[10], act2[10];

bool in_mid(Act ac) {
    return ac.s < 720 && ac.e >= 720;
}

int func(Act* ac, int num) {
    if (num == 1) {
        return 2;
    } else if (num == 2) {
        if (ac[0].s > ac[1].s) {
            swap(ac[0], ac[1]);
        }
        //DEBUG(ac[0].s);DEBUG(ac[1].s);
        if (ac[1].e - ac[0].s <= 720) {
            return 2;
        } else if (ac[0].e + 60 * 24 - ac[1].s <= 720) {
            return 2;
        } else {
            return 4;
        }
    } else {
        return 0;
    }
}

int solve() {
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i) {
        scanf("%d%d", &act1[i].s, &act1[i].e);
    }
    for (int i = 0; i < m; ++i) {
        scanf("%d%d", &act2[i].s, &act2[i].e);
    }
    if (m == 0) {
        return func(act1, n);
    } else if (n == 0) {
        return func(act2, m);
    } else {
        return 2;
    }
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        int ans = solve();
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
