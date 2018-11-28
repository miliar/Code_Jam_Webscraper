#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <cmath>
using namespace std;

int N, K, i, j;
double U, P[51];

int main() {
    int cases;
    scanf("%d", &cases);
    for (int kejs = 1; kejs <= cases; kejs++) {
        printf("Case #%d: ", kejs);
        scanf("%d%d", &N, &K);
        scanf("%lf", &U);
        for (i = 0; i < N; i++) {
            scanf("%lf", &P[i]);
        }
        sort(P, P+N);
        P[N] = 1;
        for (i = 0; i < N; i++) {
            if (P[i] < P[i+1]) {
                int n = i+1;
                double diff = P[i+1] - P[i];
                double needed = n * diff;
                if (needed > U) needed = U;
                for (j = 0; j <= i; j++) P[j] += needed / n;
                U -= needed;
            }
        }
        double res = 1;
        for (i = 0; i < N; i++) res *= P[i];

        printf("%.20lf\n", res);
    }
    return 0;
}
