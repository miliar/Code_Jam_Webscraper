#include <bits/stdc++.h>

const int maxn = 55, maxp = 55;

int Tests, n, p, r[maxn], q[maxn][maxp], ans, curamount, idx[maxn];

int cando(int r, int q, int amount) {
    // q < 9/10 * r * amount
    if (10ll * q < 9ll * r * amount) {
        return -1;
    }
    // q > 11/10 * r * amount
    else if (10ll * q > 11ll * r * amount) {
        return 1;
    } else {
        return 0;
    }
}

bool go() {
    for (int i = 0; i < n; i++) {
        if (idx[i] == p) {
            return false;
        }
        int res = cando(r[i], q[i][idx[i]], curamount);
        if (res == -1) {
            idx[i]++;
            return true;
        } else if (res == 1) {
            do {
                curamount++;
            } while (cando(r[i], q[i][idx[i]], curamount) == 1);
            return true;
        }
    }
    ans++;
    for (int i = 0; i < n; i++) {
        idx[i]++;
    }
    return true;
}

int main() {
    scanf("%d", &Tests);
    for (int test = 1; test <= Tests; test++) {
        scanf("%d%d", &n, &p);
        for (int i = 0; i < n; i++) {
            scanf("%d", r+i);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                scanf("%d", &q[i][j]);
            }
            std::sort(q[i], q[i]+p);
        }
        for (int i = 0; i < n; i++) {
            idx[i] = 0;
        }
        ans = 0;
        curamount = 1;
        while (go());
        printf("Case #%d: %d\n", test, ans);
    }
}

