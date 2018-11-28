#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define FIN freopen("A-large.in", "r", stdin)
#define FOUT freopen("A-large.out", "w", stdout)

const int N = 28;

int main() {
    FIN;
    FOUT;
    int T, ncase = 0;
    scanf("%d", &T);
    while(T--) {
        int dis, m;
        scanf("%d%d", &dis, &m);
        double ans = 0;
        for(int i = 0; i < m; ++i) {
            int p, v;
            scanf("%d%d", &p, &v);
            ans = max((dis - p) * 1.0 / v, ans);
        }
        printf("Case #%d: %.7f\n", ++ncase, dis / ans);
    }
    return 0;
}
