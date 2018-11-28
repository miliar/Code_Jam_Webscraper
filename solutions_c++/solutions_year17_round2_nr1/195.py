#include <cstdio>
#include <iostream>
using namespace std;

int nrt;
int n, d;

int main() {

    scanf("%d", &nrt);
    for(int t = 1; t <= nrt; ++t) {
        scanf("%d %d", &d, &n);
        
        double maxT = 0;
        for(int i = 1; i <= n; ++i) {
            int pos, speed;
            scanf("%d %d", &pos, &speed);

            double tm = (d - pos) * 1.0 / speed;
            maxT = max(maxT, tm);
        }

        printf("Case #%d: %.10f\n", t, d / maxT);
    }

    return 0;
}