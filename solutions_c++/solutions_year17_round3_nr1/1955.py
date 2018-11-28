#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <string.h>
#include <queue>
#include <stdlib.h>
using namespace std;

int r[1024], h[1024];

#define M_PI           3.14159265358979323846264338327950288

struct par {
    double r, h;
    par(double _r, double _h) {
        r = _r, h = _h;
    }
};

bool operator <(const par &A, const par &B) {
    return A.r * A.h < B.r * B.h;
}

void solve2(int t) {
    
    int n, k;
    scanf("%d %d", &n, &k);
    
    vector <par> v;
    
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &r[i], &h[i]);
        v.push_back(par(r[i], h[i]));
    }
    
    sort(v.rbegin(), v.rend());
    
    double ret = 0.0;
    
    for (int i = 0; i < n; i++) {
        double tmp = 0.0;
        tmp += (double)v[i].r * (double)v[i].r;
        tmp += (double)v[i].r * (double)v[i].h * 2.0;
        
        if (i < k) {
            for (int j = 0; j < k; j++) {
                if (j != i) {
                    tmp += (double)v[j].r * (double)v[j].h * 2.0;
                }
            }
        } else {
            for (int j = 0; j < k - 1; j++) {
                if (j != i) {
                    tmp += (double)v[j].r * (double)v[j].h * 2.0;
                }
            }
        }
        
        if (tmp > ret) {
            ret = tmp;
        }
    }
    
    printf("Case #%d: %lf\n", t, ret * M_PI);
}

int main() {
    
    int t;
    scanf("%d", &t);
    
    for (int i = 1; i <= t; i++) {
        solve2(i);
    }
    
    return 0;
}
