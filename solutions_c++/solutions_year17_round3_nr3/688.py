#include <cstdio>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

const int MAX_NUM = 50;
int T;
int N, K;

double U;
double P[MAX_NUM];

double solve(double tot) {
    int up = N-1;
    while (0 <= up && P[up] > tot / (up + 1)) {
        tot -= P[up];
        up--;
    }
    
    if (0 <= up) {
        double target = tot / (up + 1);
        
        while (0 <= up) {
            P[up--] = target;
        }
    }
    
    double res = 1.0;
    for (int i = 0; i < N; i++) {
        res *= P[i];
    }
    return res;
}

int main() {
    freopen("1c.in", "r", stdin);
    
    scanf("%d\n", &T);
    
    for (int test = 1; test <= T; test++) {
        scanf("%d %d\n", &N, &K);
        scanf("%lf\n", &U);
        
        double tot = 0.0;
        for (int i = 0; i < N; i++) {
            scanf("%lf", &P[i]);
            tot += P[i];
        }
        sort(P, P + N);
        
        printf("Case #%d: %f\n", test, solve(tot + U));
    }
}
