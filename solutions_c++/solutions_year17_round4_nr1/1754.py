#include <bits/stdc++.h>

using namespace std;

void print_case(int id) {
    printf("Case #%d: ", id);
}

void solve(int id) {
    int n, p;
    scanf("%d %d", &n, &p);

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &a[i]);
    }

    print_case(id);

    vector<int> c(p);
    for (int i = 0; i < n; ++i) {
        ++c[a[i] % p];
    }

    int res;
    if (p == 2) {
        res = c[0] + (c[1] + 1) / 2;
    } else if (p == 3) {
        res = c[0];
        int mn = min(c[1], c[2]);
        int mx = max(c[1], c[2]);
        res += mn;
        res += (mx - mn + 2) / 3;
    } else {
        throw 1;
    }

    printf("%d\n", res);
    // } else if (p == 4) {
    //     int res = c[0];
    //     int mn = min(c[1], c[3]);
    //     res += mn;
    //     c[1] -= mn;
    //     c[3] -= mn;
    //     res += c[2] / 2;
    //     c[2] %= 2;
    //     if (c[2] == 1) {
    //         if (c[1] >= 2) {
    //             ++res;
    //             c[2] = 0;
    //             c[1] -= 2;
    //         }
    //     }

    //     res += c[1] / 4;
    //     c[1] %= 4;

    //     if (c[2] == 1 && c[1] == 1) {
    //         c[3] += 1;
    //         c[2] = 0;
    //     }

    //     if (c[2] == 1) {
    //         ++res;
    //         c[2] = 0;
    //         c[3] -= 2;
    //         c[3] = max(c[3], 0);
    //     }

    //     if (c[1] > 0) {
    //         ++res;
    //     }
    // }
}

int main() {
    int t;
    scanf("%d", &t);

    for (int i = 1; i <= t; ++i) {
        solve(i);
    }

    return 0;
}
