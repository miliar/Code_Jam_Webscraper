#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAX_N = 50;
const double eps = 1e-6;

int N, K;
double U;
double p[MAX_N];

double solve(){
    sort(p, p+N);
    for (int i = 0; i < N-1; ++i){
        if (U < eps) break;
        double tmp = (i+1)*(p[i+1]-p[i]);
        if (U > tmp){
            for (int j = 0; j <= i; ++j)
                p[j] = p[i+1];
            U -= tmp;
        }
        else{
            double h = U / (i+1);
            for (int j = 0; j <= i; ++j)
                p[j] += h;
            U = 0;
        }
    }
    // remain
    if (U > eps){
        double h = U / N;
        for (int i = 0; i < N; ++i)
            p[i] += h;
        U = 0;
    }
    double ret = 1.0;
    for (int i = 0; i < N; ++i){
        ret *= p[i];
    }
    return ret;
}

int main(){
    freopen("/Users/eajoy/Downloads/C-small-1-attempt0.in", "r", stdin);
    freopen("/Users/eajoy/Downloads/C-small-1-attempt0.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for (int CASE = 1; CASE <= TEST; ++CASE){
        scanf("%d%d%lf", &N, &K, &U);
        for (int i = 0; i < N; ++i) scanf("%lf", p+i);
        double ans = solve();
        printf("Case #%d: %.10lf\n", CASE, ans);
    }
    return 0;
}
