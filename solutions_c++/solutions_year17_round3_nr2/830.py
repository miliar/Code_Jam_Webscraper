#include <stdio.h>
#include <algorithm>
#include <utility>
#include <vector>
#include <iostream>
#include <set>
#include <math.h>

#define long long long

using namespace std;

int ac, aj, n;
int l[1000], r[1000];

int solve(int t) {
    scanf("%d%d", &ac, &aj);
    n = ac + aj;
    for (int i = 0; i < n; ++i) {
        scanf("%d%d", &l[i], &r[i]);
    }
    if (ac <= 1 && aj <= 1) {
        return printf("Case #%d: 2\n", t);
    }
    if (l[0] > l[1]) {
        swap(l[0], l[1]);
        swap(r[0], r[1]);
    }
    int t1 = r[1] - l[0];
    int t2 = 1440 - l[1] + r[0];
    if (t1 <= 720 || t2 <= 720) {
        return printf("Case #%d: 2\n", t);
    }
    printf("Case #%d: 4\n", t);
    return 0;
}

int main() {
    int tests;
    scanf("%d", &tests);
    for (int i = 1; i <= tests; ++i) {
        solve(i);
    }

    return 0;
}
