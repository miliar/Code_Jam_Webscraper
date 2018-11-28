#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define PB(x) push_back(x)
#define MP(a, b) make_pair(a, b)

typedef long long int64;
typedef long double ldouble;
typedef pair<int, int> pii;

// const int MNOGO = 0x3fffffff;

#define PROBLEM "C"

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        fprintf(stderr, "Case #%d\n", test);

        int n, k;
        cin >> n >> k;

        double u;
        cin >> u;

        vector<double> a;

        for (int i = 0; i < n; i++) {
            double p;
            cin >> p;
            a.PB(p);
        }

        stable_sort(a.begin(), a.end());

        while (u > 1e-9) {
            int i = 0;
            while (i < n && a[i] == a[0]) i++;

            double nl = 1;
            if (i < n) nl = a[i];

            double delta = (nl - a[0]);
            if (u >= delta * i) {
                for (int j = 0; j < i; j++) {
                    a[j] += delta;
                    u -= delta;
                }
            } else {
                double delta = u / i;

                for (int j = 0; j < i; j++) {
                    a[j] += delta;
                }

                u = 0;
            }
        }

        double answer = 1.0;
        for (int k = 0; k < n; k++) {
            answer = answer * a[k];
        }

        printf("%0.7lf", answer);

        printf("\n");
    }

    return 0;
}
