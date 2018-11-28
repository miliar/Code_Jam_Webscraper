#include <cstdio>
#include <algorithm>

using namespace std;

#define NMAX 1000
#define DMAX 1000000000
#define SMAX 10000

struct Horse {
    int k;
    int s;
};

bool cmp_k(const Horse &a, const Horse &b)
{
    return a.k < b.k;
}

int main()
{
    int t;
    static Horse h[NMAX];

    scanf("%d", &t);
    for (int tc = 1; tc <= t; ++tc) {
        int d, n;
        double tmax = 0.0;

        scanf("%d %d", &d, &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d %d", &h[i].k, &h[i].s);
        }

        sort(h, h+n, cmp_k);

        for (int i = 0; i < n; ++i) {
            double t = (double)(d-h[i].k)/h[i].s;

            //printf("t[%d] = %f\n", i, t);
            tmax = max(tmax, t);
        }

        //printf("tmax = %f\n", tmax);

        printf("Case #%d: %f\n", tc, d/tmax);
    }

    return 0;
}
