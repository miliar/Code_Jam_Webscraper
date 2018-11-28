#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <string.h>
#include <queue>
#include <stdlib.h>
#include <cmath>
using namespace std;

void solve(int t) {

    int cilj, konji;
    scanf("%d %d", &cilj, &konji);
    
    int poz[1024], brzina[1024];
    
    for (int i = 0; i < konji; i++) {
        scanf("%d %d", &poz[i], &brzina[i]);
    }
    
    int k = 0;
    double lo = 0.0, hi = 1000000000000000000.0;
    while (abs(lo - hi) > 1e-9 && k < 1000) {
        k++;
        double mid = (lo + hi) / 2.0;
        double t = double(cilj) / mid;
        int prevelika = 0;
        for (int i = 0; i < konji; i++) {
            double udaljenost = poz[i] + brzina[i] * t;
            if (udaljenost < cilj) {
                prevelika = 1;
                break;
            }
        }
        if (prevelika) {
            hi = mid;
        } else {
            lo = mid;
        }
    }
    
    printf("Case #%d: %.9f\n", t, hi);
}

int main() {
    
    int t;
    scanf("%d", &t);
    
    for (int i = 1; i <= t; i++) {
        solve(i);
    }
    
    return 0;
}
