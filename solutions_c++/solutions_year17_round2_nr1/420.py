#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
using namespace std;
double km[1005], speed[1005];
int main() {
    int t, cas = 0;
    int m;
    double n;
    scanf("%d", &t);
    while (t--) {
        cas++;
        scanf("%lf %d",&n, &m);
        for (int i = 0; i < m; ++i) {
            scanf("%lf %lf", &km[i], &speed[i]);
            km[i] = n - km[i];
        }
        double max_speed = n / km[0] * speed[0];
        for (int i = 0; i < m; ++i) {
            max_speed = std::min(max_speed, n / km[i] * speed[i]);
        }
        printf("Case #%d: %.12lf\n", cas, max_speed);
    }
    return 0;
}
