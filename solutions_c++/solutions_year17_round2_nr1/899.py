#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int D, N;
        scanf("%d%d", &D, &N);
        double a = 0;
        for (int i = 1; i <= N; ++i) {
            int k, s;
            scanf("%d%d", &k, &s);
            a = max(1.0 * (D - k) / s, a);
        }
        printf("Case #%d: %.6lf\n", t, D / a);
    }
    return 0;
}