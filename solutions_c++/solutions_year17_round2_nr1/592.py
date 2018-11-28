#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <list>


using namespace std;

#define N 1005

double p[N];
double d[N];

int main() {
    double ed;
    int n, test;
    scanf("%d", &test);
    for (int cas = 1; cas <= test; cas++) {
        scanf("%lf%d", &ed, &n);
        double tt = 0;
        for (int i = 0; i < n; i++) {
            scanf("%lf%lf", p + i, d + i); 
            tt = max(tt, (ed - p[i]) / d[i]);
        }
        printf("Case #%d: %.7f\n", cas, ed / tt);
    }
    return 0;
}
