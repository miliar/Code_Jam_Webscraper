#include <stdio.h>

int main() {
    int tn, cn;
    for (scanf("%d", &tn), cn = 1; cn <= tn; cn++) {
        int d, n;
        double max_speed = -1;
        scanf("%d%d", &d, &n);
        for (int i = 0; i < n; i++) {
            int k, s;
            scanf("%d%d", &k, &s);
            double cur_speed = (double)(d) * s / (double)(d - k);
            if (i == 0 || cur_speed < max_speed) {
                max_speed = cur_speed;
            }
        }
        printf("Case #%d: %.8lf\n", cn, max_speed);
    }
    return 0;
}
