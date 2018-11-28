#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for (int o=1; o<=t; o++) {
        int d, n, nw, s;
        double a = 1e100;
        double mx;
        scanf("%d %d", &d, &n);
        for (int i=0; i<n; i++) {
            scanf("%d %d", &nw, &s);
            mx = (1.0*d*s) / (d-nw);
            if (a>mx)
                a = mx;
        }
        printf("Case #%d: %f\n", o, a);
    }
}
