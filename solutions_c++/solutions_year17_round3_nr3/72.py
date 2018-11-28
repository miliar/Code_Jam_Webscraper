//
// Created by Denis Mukhametianov on 30.04.17.
//

#include <cstdio>
#include <algorithm>

using namespace std;


int scanProb() {
    int a, b;
    scanf("%d.%d", &a, &b);
    return a * 10000 + b;
}

int p[146];
double realP[146];


void distributeFairly(double u, int k, int n) {
    for (int i = 0; i < k; i++) {
        realP[i] += u / k;
    }
}


void solveC(int tc) {
    int n, k;
    scanf("%d%d", &n, &k);
    int u = scanProb();
    for (int i = 0; i < n; i++)
        p[i] = scanProb();
    sort(p, p + n);
    for (int i = 0; i < n; i++)
        realP[i] = p[i] * 1. / 10000;
    while (u > 0) {
        int cnt = 1;
        for (int i = 1; i < n; i++)
            if (p[i] == p[0])
                cnt++;
        if (cnt < n) {
            int toAdd = p[cnt] - p[0];
            if (toAdd * cnt <= u) {
                for (int i = 0; i < cnt; i++) {
                    p[i] += toAdd;
                    u -= toAdd;
                    realP[i] = p[i] * 1. / 10000;
                }
            } else {
                distributeFairly(u * 1. / 10000, cnt, n);
                u = 0;
            }
        } else {
            distributeFairly(u * 1. / 10000, cnt, n);
            u = 0;
        }
    }
    double ans = 1;
    for (int i = 0; i < n; i++)
        ans *= realP[i];
    printf("Case #%d: %.8lf\n", tc + 1, ans);
}

void solveC() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
        solveC(i);
}