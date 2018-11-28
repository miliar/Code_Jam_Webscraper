#include<stdio.h>
#include<string.h>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
using namespace std;
int main() {
    int ca;
    scanf("%d", &ca);
    for (int cas = 1; cas <= ca; cas++) {
        int d, n;
        scanf("%d%d", &d, &n);
        double v = 1e20;
        int k, s;
        for (int i = 0; i < n; i++) {
            scanf("%d%d", &k, &s);
            v = min(v, 1.0 * d * s / (d - k));
        }
        printf("Case #%d: %.10lf\n", cas, v);
    }
}
