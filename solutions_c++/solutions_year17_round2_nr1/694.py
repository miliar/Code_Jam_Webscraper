#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

#define For(i, n) for(int i = 0; i < (n); i++)
typedef pair<int, int> pii;

double solve(int d, vector<pii> horses) {
    double res = -1;

    for (auto h : horses) {
        int s0 = d - h.first;
        double t0 = (double)s0 / (double)h.second;

        double v = (double)d / t0;
        if (res < 0 || v < res)
            res = v; 
    }

    return res;
}

int main () {
    int t;
    scanf("%d", &t);

    For (i, t) {
        int d, n;
        scanf("%d %d", &d, &n);
        
        vector<pii> hs(n);
        For (i, n) 
            scanf("%d %d", &hs[i].first, &hs[i].second);

        printf("Case #%i: %.6lf\n", i + 1, solve(d, hs));
    }
}