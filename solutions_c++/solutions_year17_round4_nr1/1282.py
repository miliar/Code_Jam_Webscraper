#include <bits/stdc++.h>
using namespace std;

int A[4];

int main() {
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int T, tI, N, P, x, t, i, j;
    scanf("%d", &T);
    for (tI = 0; tI < T; tI++) {
        t = 0;
        scanf("%d %d", &N, &P);
        for (i = 0; i < 4; i++) A[i] = 0;
        for (i = 0; i < N; i++) scanf("%d", &x), A[x % P]++;
        t += A[0];
        if (P == 2) {
            t += (A[1] + 1) / 2;
        } else if (P == 3) {
            x = min(A[1], A[2]);
            A[1] -= x;
            A[2] -= x;
            t += x;
            t += A[1] / 3 + A[2] / 3 + (A[1] % 3 || A[2] % 3);
        } else if (P == 4) {
            x = min(A[1], A[3]);
            A[1] -= x;
            A[3] -= x;
            t += x;
            if (A[3]) swap(A[1], A[3]);
            x = min(A[2], A[1] / 2);
            A[2] -= x;
            A[1] -= x * 2;
            t += x;
            t += A[2] / 2;
            t += A[1] / 4;
            A[2] %= 2;
            A[1] %= 4;
            t += A[2] || A[1];
        }
        printf("Case #%d: %d\n", tI + 1, t);
    }
    return 0;
}
