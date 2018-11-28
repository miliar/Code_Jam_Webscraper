#include <bits/stdc++.h>
using namespace std;

int t, n, p;
int q[55][55];
int r[55];

int ceildiv(int q, int r) {
    if (q % r == 0) {
        return q / r;
    } else {
        return q / r + 1;
    }
}

int floordiv(int q, int r) {
    return q / r;
}
int main() {
    scanf("%d", &t);
    int cs = 0;
    while (t--) {
        ++cs;
        scanf("%d %d", &n, &p);
        for (int i = 0; i < n; i++) {
            scanf("%d", &r[i]);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                scanf("%d", &q[i][j]);
            }
            sort(q[i], q[i] + p);
        }
        int pnt[55];
        for (int i = 0; i < n; i++) {
            pnt[i] = 0;
        }

        int result = 0;

        while (true) {
            int lb[55];
            int rb[55];
            for (int i = 0; i < n; i++) {
                lb[i] = ceildiv(10 * q[i][pnt[i]], 11 * r[i]);
                rb[i] = floordiv(10 * q[i][pnt[i]], 9 * r[i]);
            }
            int maxlb = 0;
            int minrb = 1000000000;
            for (int i = 0; i < n; i++) {
                maxlb = max(maxlb, lb[i]);
                minrb = min(minrb, rb[i]);
            }
            bool finished = false;
            if (minrb < maxlb) {
                for (int i = 0; i < n; i++) {
                    if (rb[i] == minrb) {
                        pnt[i]++;
                        if (pnt[i] == p) {
                            finished = true;
                        }
                    }
                }
            } else {
                result++;
                for (int i = 0; i < n; i++) {
                    pnt[i]++;
                    if (pnt[i] == p) {
                        finished = true;
                    }
                }
            }
            if (finished) {
                break;
            }
        }
        printf("Case #%d: %d\n", cs, result);
    }
}
