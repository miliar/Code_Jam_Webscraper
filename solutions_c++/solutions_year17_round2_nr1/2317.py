#include "stdafx.h"
#include "R1B_A.h"

void R1B_A::Solve() {
    int d, n;
    cin >> d >> n;
    int k, s;
    double max_time = 0;
    for (int i = 0; i < n; ++i) {
        cin >> k >> s;
        max_time = max(max_time, (d - k + 0.0) / s);
    }
    printf("%.7f\n", d / max_time);
}
