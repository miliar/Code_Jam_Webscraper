#include <stdio.h>
#include <algorithm>
#include <utility>
#include <vector>
#include <iostream>
#include <set>
#include <math.h>

#define long long long

using namespace std;

double p[51];
double u;
double ans;
int n, k;

void solve(int t) {
    scanf("%d%d", &n, &k);
    scanf("%lf", &u);
    for (int i = 0; i < n; ++i) {
        scanf("%lf", &p[i]);
    }
    double lb = 0, rb = 1;
    for (int step = 0; step < 100; ++step) {
        double mb = (lb + rb) / 2;
        double left = u;
        for (int i = 0; i < n; ++i) {
            if (p[i] < mb) {
                left -= mb - p[i];
            }
        }
        if (left < 0) {
            rb = mb;
        } else {
            lb = mb;
        }
    }
    ans = 1;
    for (int i = 0; i < n; ++i) {
        if (p[i] > lb) {
            ans *= p[i];
        } else {
            ans *= lb;
        }
    }
    printf("Case #%d: %.10g\n", t, ans);
}

int main() {
    int tests;
    scanf("%d", &tests);
    for (int i = 1; i <= tests; ++i) {
        solve(i);
    }

    return 0;
}
