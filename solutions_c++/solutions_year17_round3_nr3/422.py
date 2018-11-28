#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 50;

double p[MAXN+5];
double sum;

int main() {
//    freopen("C-eg.in", "r", stdin);
    freopen("C-small-1-attempt0.in", "r", stdin);
//    freopen("C-large.in", "r", stdin);
//    freopen("C-eg.out", "w", stdout);
    freopen("C-small-1-attempt0.out", "w", stdout);
//    freopen("C-large.out", "w", stdout);

    int T, n , K;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d%d%lf", &n, &K, &sum);
        for(int i = 1; i <= n; ++i) {
            scanf("%lf", &p[i]);
        }
        p[++n] = 1;
        sort(p+1, p+n+1);
        for(int i = 1; i < n; ++i){
            double d = p[i+1]-p[i];
            if (d*i <= sum) {
                for (int j = 1; j <= i; ++j)
                    p[j] += d;
                sum -= d*i;
            } else{
                d = sum/i;
                for (int j = 1; j <= i; ++j)
                    p[j] += d;
                break;
            }
        }
        double ans = 1;
        for (int i = 1; i <= n; ++ i) {
            ans *= p[i];
        }
        printf("Case #%d: %.6lf\n", t, ans);
    }
    return 0;
}