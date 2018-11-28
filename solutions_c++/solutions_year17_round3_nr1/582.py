#include <bits/stdc++.h>

#define PI ((double)acos(-1.0))

typedef long long ll;

using namespace std;

ll R[1000], H[1000], RH[1000], L[1000];

int main() {

    // freopen("A-large.in", "r", stdin);
    // freopen("A-large.out", "w", stdout);

    int T, k = 0, N, K, i, j, m; ll res, tres;

    scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", ++k);
        scanf("%d%d", &N, &K);
        for(i=0;i<N;i++) {
            scanf("%lld%lld", &R[i], &H[i]);
            RH[i] = R[i] * H[i];
        }
        res = 0;
        for(i=0;i<N;i++) {
            m = 0;
            for(j=0;j<N;j++) {
                if (i == j || R[j] > R[i]) continue;
                L[m++] = RH[j];
            }
            if (m < K-1)
                continue;
            sort(L, L+m);
            tres = R[i] * (R[i] + 2 * H[i]);
            for(j=0;j<K-1;j++)
                tres += 2 * L[m-1-j];
            if (tres > res)
                res = tres;
        }
        printf("%.9f\n", (double)PI * res);
    }

    return 0;
}
