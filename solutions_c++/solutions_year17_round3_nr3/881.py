#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

double probs[50];

int N, K;
double U;

bool can(double m) {
    double req = 0;
    for(int i = 0; i < N; ++i) {
        if(m > probs[i])
            req += (m - probs[i]);
    }
    if(req <= U) return true;
    return false;
}

void solve1() {
    scanf("%d %d %lf", &N, &K, &U);

    for(int i = 0; i < N; ++i) {
        scanf("%lf", &probs[i]);
    }

    sort(probs, probs + N);
    double lo = probs[0];
    double hi = 1;
    for(int i = 0; i < 1000000; ++i) {
        double mid = (lo + hi) / 2;
        if(can(mid)) {
            lo = mid;
        } else {
            hi = mid;
        }
    }
    double res = 1;
    for(int i = 0; i < N; ++i) {
        if(probs[i] > lo)
            res *= probs[i];
        else
            res *= lo;
    }

    printf("%lf\n", res);
}

int main() {
    int T;
    scanf("%d", &T);
    for(int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        solve1();
    }

    return 0;
}
