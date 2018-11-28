#include <cstdio>
#include <algorithm>
#include <iostream>
#define EPS 1e-10

using namespace std;

int dcmp(double x) { return x < -EPS ? -1 : x > EPS; }

bool cmp(double d1, double d2) {
    return (dcmp(d1-d2) < 0);
}


int N, K;
double P[55];
double U;
void solve() {

    scanf("%d%d",&N,&K);
    scanf("%lf",&U);
    for (int i = 0; i < N; ++i) {
        scanf("%lf",&P[i]);
    }
    sort(P,P+N,cmp);
    P[N] = 1.0;

    /*for (int i = 0; i < N; ++i) {
        printf("*%lf\n",P[i]);
    }*/
    double delta;
    for (int i = 0; i < N; ++i) {
        if (dcmp(U) == 0) break;

        delta = P[i+1]-P[i];
        //printf("delta = %lf, U = %lf",delta,U);
        if (dcmp(U-(delta*(i+1))) < 0) {
            //printf("N\n");
            for(int j = 0; j <= i; ++j) {
                P[j] = P[j] + (U/(i+1));
            }
            break;
        }
        else { // >= 0
            //printf("Y\n");
            for(int j = 0; j <= i; ++j) {
                P[j] = P[i+1];
            }
            U = U-(delta*(i+1));
        }
    }

    double ans = 1;
    for (int i = 0; i < N; ++i)
        ans *= P[i];

    printf("%.6lf\n",ans);

}


int main() {
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("C-small-1-attempt0.out","w",stdout);
    int test;
    scanf("%d",&test);
    for (int t = 1; t <= test; ++t) {
        printf("Case #%d: ",t);
        solve();
    }
    return 0;
}
