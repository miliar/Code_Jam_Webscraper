#include <cstdio>
const int NMAX = 1005;
double eps = 1e-8;
double INF = 0x3f3f3f3f3f;

int tests, N, D;
struct horse {
    int pos, speed;
};
horse H[NMAX];
double howLong[NMAX];

inline double abs(double x) {
    return x < 0.0 ? -x : x;
}

inline bool eq(double x, double y) {
    return abs(x - y) < eps;
}

inline bool ok(double s) {
    double tGet;
    for (int i = 1; i <= N; i++) {
        if (H[i].speed > s - eps) {
            continue ; 
        }
        tGet = (1.0 * H[i].pos) / (s - H[i].speed);
        if (tGet < howLong[i]) {
            return false;
        }
    }

    return true;
}

int main() {
    freopen("horses.in", "r", stdin);
    freopen("horsesLarge.out", "w", stdout);
    //freopen("horsesSmall2.out", "w", stdout);

    scanf("%d", &tests);
    for (int test = 1; test <= tests; test++) {
        scanf("%d%d", &D, &N);
        for (int i = 1; i <= N; i++) {
            scanf("%d%d", &H[i].pos, &H[i].speed);
            howLong[i] = (1.0 * D - H[i].pos) / H[i].speed;
        }

        double left = 0.0, right = 1.0 * D * 10000, mid;
        for (int steps = 0; steps <= 100; steps++) {
            mid = left + (right - left) / 2;

            if (ok(mid)) {
                left = mid;
            } else {
                right = mid;
            }
        }

        printf("Case #%d: %.10lf\n", test, left);
    }
    return 0;
}