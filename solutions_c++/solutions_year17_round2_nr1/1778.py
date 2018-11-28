#include <iostream>
#include <cstdio>
#include <limits>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);

    for (int i = 1; i <= T; i++) {
        int D,N;
        scanf("%d %d", &D, &N);

        double v = -1;

        for (int j = 0; j < N; j++) {
            double xi, vi;
            scanf("%lf %lf", &xi, &vi);

            if (xi == D) continue;

            //printf("%lf %lf %lf\n", xi, vi, D*vi/(D-xi));
            if (v == -1) v = D*vi/(D - xi);
            else v = min(v, D*vi/(D - xi));
        }

        printf("Case #%d: %lf\n", i, v);
    }
}