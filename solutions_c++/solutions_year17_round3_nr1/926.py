#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

const double EPS = 1e-8;
long long k, n, T;
struct Pancake {
public:
    long long r, h;
    double sArea() const {
        return 2.0 * acos(-1) * h * r;
    }
    bool operator < (const Pancake &other) const {
        return sArea() > other.sArea();
    }
} a[4000], b[4000];

int main() {
    cin >>T;
    for (long long t = 1; t <= T; t++) {
        cin >>n >>k;
        for (long long i = 0; i < n; i++) {
            cin >>a[i].r >>a[i].h;
            b[i] = a[i];
        }
        double best = -1;
        for (long long j = 0; j < n; j++) {
            memcpy(b, a, sizeof(b));
            b[0] = a[j];
            b[j] = a[0];
            sort(b + 1, b + n);
            double sum = 0;
            long long maxr = 0;
            for (long long i = 0; i < k; i++) {
                sum += b[i].sArea();
                if (maxr < b[i].r)
                    maxr = b[i].r;
            }
            sum += maxr * maxr * acos(-1);
            if ((best - sum) < EPS)
                best = sum;
            //printf("Now trying %.9lf\n", sum);
        }
        printf("Case #%lld: %.9lf\n", t, best);
    }
    return 0;
}
