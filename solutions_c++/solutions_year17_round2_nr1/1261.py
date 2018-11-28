#include <cstdio>

using namespace std;

int T, N;

double D, tm, spd;

inline double max(double a, double b) {return a < b ? b : a;}

int main() {
#ifdef RS16
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif // RS16

    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        scanf("%lf%d", &D, &N);
        //printf("%f %d\n", D, N);
        tm = 0;
        for(int i = 0; i < N; ++i) {
            double K, S;
            scanf("%lf%lf", &K, &S);
            tm = max(tm, (D-K)/S);
            //printf("%f %f %f\n", K, S, tm);
        }
        spd = D/tm;
        printf("Case #%d: %.9f\n", t, spd);
    }
}
