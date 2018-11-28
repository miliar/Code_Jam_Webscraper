#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int testcase;
    scanf("%d", &testcase);
    for (int ti = 1; ti <= testcase; ti++) {
        printf("Case #%d: ", ti);
        int d, n;
        double ans = 0;
        scanf("%d%d", &d, &n);
        int a[1010], b[1010];
        for (int i = 0; i < n; i++) {
            int k, l;
            scanf("%d%d", &k, &l);
            double g = (d * 1.0 - k * 1.0) / l * 1.0;
            if (g > ans) {
                ans = g;
            }
        }
        printf("%.6f\n", d  * 1.0 / ans);
    }
}