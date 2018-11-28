#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        int D, N;
        scanf("%d %d", &D, &N);
        double time = 0;
        int k, s;
        for(int n = 0; n < N; n++) {
            scanf("%d %d", &k, &s);
            
            time = max(time, (0. + D - k) / s);
        }
        printf("Case #%d: %.6lf\n", t, D / time);
    }
    return 0;
}
