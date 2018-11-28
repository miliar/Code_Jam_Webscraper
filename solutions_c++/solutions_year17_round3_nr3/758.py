#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const double EPSILON = 1e-7;

bool fEqual(double a, double b){
    return fabs(a - b) < EPSILON;
}

int main(void){
    int tt;
    int n, k;
    double u;
    double p[60];
    scanf("%d", &tt);
    for(int tc = 1; tc <= tt; tc++){
        scanf("%d%d", &n, &k);
        scanf("%lf", &u);
        for(int i = 0; i < n; i++){
            scanf("%lf", &p[i]);
        }

        sort(p, p + n);
        for(int i = 0; i < n && !fEqual(u, 0.0);){
            int j;
            for(j = i+1; j < n && fEqual(p[i], p[j]); j++);
            double usedValue = (j == n)? u: min((p[j] - p[i]) * j, u);
            double toPlus = usedValue / j;
            for(int k = 0; k < j; k++){
                p[k] += toPlus;
            }
            i = j;
            u -= usedValue;
        }

        double ans = 1.0;
        for(int i = 0; i < n; i++){
            ans *= p[i];
        }
        printf("Case #%d: %.6f\n", tc, ans);
    }
    return 0;
}
