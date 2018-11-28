#include <cstdio>
#include <algorithm>
using namespace std;

int n, k;
double u;
double a[64];

void read() {
    scanf("%d%d%lf", &n, &k, &u);
    for (int i = 0; i < n; i++) {
        scanf("%lf", &a[i]);
    }
}

void solve() {
    sort(a, a+n);
    while(1) {
        if (1 - a[0] < 1e-6) break;

        double next = 1;
        int count = 1;
        for (int i = 1; i < n; i++) {
            if (a[i] - a[0] > 1e-6) {
                next = a[i];
                break;
            }
            ++ count;
        }
        //printf ("%lf %d %lf\n", next, count, u);

        if ((next - a[0]) * count < u) {
            u -= (next - a[0]) * count;
            for (int i = 0; i < count; i++) {
                a[i] = next;
            }
        } else {
            u /= count;

            for (int i = 0; i < count; i++) {
                a[i] += u;
            }
            break;
        }
    }
    double ans = 1.;
    for (int i = 0; i < n; i++) {
        ans *= a[i];
    }
    printf ("%.6lf\n", ans);
}

int main() {
    int i, cases;

    scanf("%d", &cases);
    for (i = 1; i <= cases; i++) {
        read();
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

