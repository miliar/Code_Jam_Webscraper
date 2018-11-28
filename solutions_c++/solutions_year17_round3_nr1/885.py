#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

struct cake {
    int h, r;

    long long surface() {
        return (long long) r * r;
    }

    long long side() {
        return 2LL * h * r;
    }
};

bool cmp(const cake& c1, const cake& c2) {
    if (c1.r != c2.r) {
        return c1.r > c2.r;
    }

    return c1.h > c2.h;
}

#define MAX_N 1111
#define INF   100000000000000000LL
#define M_PIl (3.14159265358979323846264338327950288)


cake a[MAX_N];

long long f[MAX_N][3];
long long maxf[MAX_N][3];

int main() {

    int nTest;
    cin >> nTest;

    for (int test = 0; test < nTest; test++) {
        int n, k;
        cin >> n >> k;
        for (int i = 0; i < n; ++i) {
            cin >> a[i].r >> a[i].h;
        }

        sort(a, a + n, cmp);

        // j = 1
        for (int i = 0; i < n; i++) {
            f[i][1] = a[i].side() + a[i].surface();

            if (i == 0)
                maxf[i][1] = f[i][1];
            else
                maxf[i][1] = max(maxf[i - 1][1], f[i][1]);
        }

        for (int jj = 2; jj <= k; jj++) {
            int j = jj % 2;
            for (int i = 0; i < n; i++) {
                // f[i][j] = max(f[0..i-1][1 - j])
                if (i == 0) f[i][j] = -INF;
                else f[i][j] = maxf[i - 1][1 - j] + a[i].side();

                if (i == 0)
                    maxf[i][j] = f[i][j];
                else
                    maxf[i][j] = max(maxf[i - 1][j], f[i][j]);
            }
        }

        cout << "Case #" << test + 1 << ": " << setprecision(20) << maxf[n - 1][k % 2] * M_PIl << endl;
    }

    return 0;
}
