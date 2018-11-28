#include <stdio.h>
#include <algorithm>

double p[60];
double ps[60];

int main()
{
    int tc, tt;
    scanf("%d", &tt);
    for (tc = 0; tc < tt; tc++){
        printf("Case #%d: ", tc + 1);
        int n, k;
        double u;

        scanf("%d%d", &n, &k);
        scanf("%lf", &u);
        for(int i = 0; i < n; i++){
            scanf("%lf", &p[i]);
            }
        std::sort(p, p+n);
        ps[0] = 0.0;
        for(int i = 0; i < n; i++){
            ps[i+1] = ps[i] + p[i];
            }
        for(int i = n; i > 0; i--){
            double pnew = (ps[i] + u) / i;
            if (pnew > 1.0)
                pnew = 1.0;
            if(pnew > p[i-1]){
                for(int j = 0; j<i; j++){
                    p[j] = pnew;
                    }
                break;
                }
            }
        double ans = 1.0;
        for(int i = 0; i < n; i++){
            ans *= p[i];
            }
        printf("%0.8lf\n", ans);
        }
    return 0;
}
