#include <bits/stdc++.h>
using namespace std;
double Solve(){
    int D, N;
    scanf("%d%d", &D, &N);
    double max_time = 0;
    for(int i = 0 ; i < N ; i++){
        int x, s;
        scanf("%d%d", &x, &s);
        max_time = max(max_time, (double)(D - x) / (double)(s));
    }
    return (double)D / max_time;
}
int main(){
    int T;
    scanf("%d", &T);
    for(int t = 1 ; t <= T ; t++){
        printf("Case #%d: %.7f\n", t, Solve());
    }
    return 0;
}
