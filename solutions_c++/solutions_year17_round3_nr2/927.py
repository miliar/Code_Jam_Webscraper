#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

int c[200], d[200], e[200], f[200];
int dp[1500][1500];
int T, a, b;

void swap(int a[], int i , int j) {
    int t = a[i]; a[i] = a[j]; a[j] = t;
}

int cal(int a[], int b[]) {
    if (a[0] > a[1]) {
        swap(a, 0, 1);
        swap(b, 0, 1);
    }
    printf("(%d, %d) - (%d, %d)\n", a[0], b[0], a[1], b[1]);
    int M = b[1];
    int m = a[0];
    if (M - m <= 720) return 1;
    M = b[0] + 1440;
    if (M - a[1] <= 720) return 1;
    return 2;
}

int main() {
    cin >>T;
    for (int t = 1; t <= T; t++) {
        int ans = 0;
        cin >>a >>b;
        for (int i = 0; i < a; i++)
            cin >>c[i] >>d[i];
        for (int i = 0; i < b; i++)
            cin >>e[i] >>f[i];
        if (a == 2) {
            ans = cal(c, d);
        } else if (b == 2) {
            ans = cal(e, f);
        } else ans = 1;
        printf("Case #%d: %d\n", t, ans * 2);
    }
    return 0;
}
