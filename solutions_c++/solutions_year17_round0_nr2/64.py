#include <bits/stdc++.h>
using namespace std;

long long A[20];

int main() {
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int T, tI, i, j;
    long long N;
    scanf("%d", &T);
    for (tI = 0; tI < T; tI++) {
        scanf("%lld", &N);
        for (i = 0; i < 20; i++) A[i] = 0;
        i = 19;
        while (N) {
            A[i--] = N % 10;
            N /= 10;
        }
        for (i = 0; i < 19; i++) if (A[i] > A[i + 1]) break;
        if (i < 19) {
            for (j = i + 2; j < 20; j++) A[j] = 9;
            while (i > -1 && A[i] > A[i + 1]) {
                A[i]--;
                A[i + 1] = 9;
                i--;
            }
        }
        for (i = 0; i < 20; i++) N *= 10, N += A[i];
        printf("Case #%d: %lld\n", tI + 1, N);
    }
    return 0;
}
