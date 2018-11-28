#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>

using namespace std;

int n, T;
long long p[100];
int K;
int a, b, x;

int main() {
    cin >>T;
    for (int t = 1; t <= T; t++) {
        cin >>n >>K;
        scanf(" %d.%d", &a, &b);
        x = a * 10000 + b;
        for (int i = 0; i < n; i++) {
            scanf(" %d.%d", &a, &b);
            p[i] = a * 10000 + b;
        }
        double ans = 1;
        sort(p, p + n);
        while (x != 0) {
            int second = 10000, run = 1;
            for (int i = 0; i < n; i++)
                if (p[i] != p[0]) {
                    run = i;
                    second = p[i];
                    break;
                }
            if (second == 10000) {
                int inc = x / n;
                int r = x % n;
                for (int i = 0; i < n; i++)
                    p[i] = p[i] + inc + (i < r);
                x = 0;
            } else {
                if (x < (second - p[0]) * run) {
                    int inc = x / run;
                    int r = x % run;
                    for (int i = 0; i < run; i++)
                        p[i] = p[i] + inc + (i < r);
                    x = 0;
                } else {
                    x -= (second - p[0]) * run;
                    for (int i = 0; i < run; i++)
                        p[i] = second;
                }
            }
        }
        for (int i = 0; i < n; i++)
            ans = (0.0001 * p[i]) * ans;
        printf("Case #%d: %.6lf\n", t, ans);
        /*for (int i = 0; i < n; i++)
            printf("p[%d] = %d\n", i, p[i]);
        puts("");*/
    }
    return 0;
}
