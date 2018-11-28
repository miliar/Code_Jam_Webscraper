#include <cstdio>
#include <algorithm>

using namespace std;

const int maxN = 60;
const double eps = 1e-12;

int N, K;
double U;
double p[maxN];
double ans;

inline double min(double a, double b) {return a < b ? a : b;}

void solveEasy() {
    sort(p+1, p+N+1); p[N+1] = 1.;
    while(U > eps) {
        int cnt;
        for(cnt = 1; cnt < N; ++cnt) {
            if(p[cnt] < p[cnt+1]-eps) break;
        }

        double hei = min(p[cnt+1]-p[cnt], U/cnt);
        for(int i = 1; i <= cnt; ++i) {
            p[i] += hei;
        }
        U -= cnt*hei;
        if(cnt == N) break;
    }

    ans = 1.;
    for(int i = 1; i <= N; ++i) ans *= p[i];
}

void solveHard() {
    ans = 1.;
}

int main() {
    #ifdef RS16
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("C-small-1-attempt0.out", "w", stdout);
#endif // RS16

    int T; scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);

        scanf("%d%d", &N, &K);
        scanf("%lf", &U);
        for(int i = 1; i <= N; ++i) scanf("%lf", p+i);

        if(K == N) {
            solveEasy();
        }
        else {
            solveHard();
        }
        printf("%.12f\n", ans);
    }
}


