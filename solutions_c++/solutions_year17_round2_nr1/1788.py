#include <iostream>
#include <cstdio>
using namespace std;

int N, D;
int s, k;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d%d", &D, &N);
        double m = 0.0;
        int d;
        for (int i = 0; i < N; i++) {
            scanf("%d%d", &k, &s);
            d = D - k;
            m = max(m, 1.0*d/s);
        }
        double S = 1.0*D/m;
        printf("Case #%d: %.6lf\n",t,  S);
    }
    return 0;
}
