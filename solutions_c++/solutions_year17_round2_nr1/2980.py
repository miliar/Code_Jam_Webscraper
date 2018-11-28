#include <bits/stdc++.h>

using namespace std;

int main() {
    int tc;
    cin >> tc;
    for(int ii=1;ii<=tc;++ii) {
        int D, N;
        scanf("%d %d", &D, &N);
        double slowestTime = 0;
        for(int i=0;i<N;++i) {
            int k, s;
            scanf("%d %d", &k, &s);
            double horseTime = (double)(D - k) / s;
            slowestTime = max(slowestTime, horseTime);
        }
        printf("Case #%d: %.6f\n", ii, D/slowestTime);
    }
    return 0;
}
