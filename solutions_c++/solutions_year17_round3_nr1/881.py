#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <cmath>
using namespace std;

long long N, K, R[1000], H[1000], i, j, k, RH[1000];

int main() {
    int cases;
    scanf("%d", &cases);
    for (int kejs = 1; kejs <= cases; kejs++) {
        printf("Case #%d: ", kejs);
        scanf("%lld%lld", &N, &K);
        for (i = 0; i < N; i++) {
            scanf("%lld%lld", &R[i], &H[i]);
            RH[i] = R[i]*H[i];
        }
        bool change;
        do {
            change = false;
            for (i = 1; i < N; i++) {
                if (RH[i-1] < RH[i]) {
                    swap(RH[i-1], RH[i]);
                    swap(R[i-1], R[i]);
                    swap(H[i-1], H[i]);
                    change = true;
                }
            }
        } while (change);

        double best = 0;
        for (k = 0; k < N; k++) {
            int cnt = 1;
            double res = M_PI * R[k] * R[k] + 2 * M_PI * RH[k];
            for (j = 0; j < N && cnt < K; j++) {
                if (j == k) continue;
                if (R[j] <= R[k]) {
                    cnt++;
                    res += 2 * M_PI * RH[j];
                }
            }
            if (cnt == K) {
                if (res > best) best = res;
            }
        }
        printf("%.10lf\n", best);
    }
    return 0;
}
