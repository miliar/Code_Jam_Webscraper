#include <cstdio>
#include <iostream>

using namespace std;

void solve() {
    int D, N;
    int k, s;
    double time = 0;
    scanf("%d%d",&D,&N);
    for (int i = 1 ; i <= N; ++i) {
        scanf("%d%d",&k,&s);
        time = max(time,(D-k)*1.0/s);
    }
    printf("%lf\n",D/time);
}


int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int test;
    scanf("%d",&test);
    for (int t = 1; t <= test; ++t) {
        printf("Case #%d: ",t);
        solve();
    }
    return 0;
}
