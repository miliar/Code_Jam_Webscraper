#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
    int T, Case = 1;
    cin >> T;
    while (T--) {
        double max_time = 0;
        int D, n;
        scanf("%d%d", &D, &n);
        for (int i = 0; i < n; i++) {
            int k, s;
            scanf("%d%d", &k, &s);
            max_time = max(max_time, (double)(D - k) / s);
        }
        double ans = D / max_time;
        printf("Case #%d: %.10f\n", Case++, ans);
    }
    return 0;
}
