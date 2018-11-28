#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for(int ca = 1; ca <= t; ++ca) {
        int d, n;
        scanf("%d%d", &d, &n);
        double max_use = 0;
        for(int i = 0; i < n; ++i) {
            int k, s;
            scanf("%d%d", &k, &s);
            double use = double(d - k) / s;
            if(use > max_use) max_use = use;
        }
        printf("Case #%d: %.6f\n", ca, d / max_use);
    }
    return 0;
}
