#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <deque>
#include <vector>

using namespace std;

int n, k;
double extra;
double p[50];

int main() {
    int TT, T;
    scanf("%d", &TT);
    
    
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        
        scanf("%d%d", &n, &k);
        scanf("%lf", &extra);
        int i, j;
        double total = 0.0;
        for (i = 0; i < n; i++) {
            scanf("%lf", &p[i]);
            total += p[i];
        }
        total+=extra;
        sort(p, p + n);
        reverse(p, p+n);
        for (i = 0; i < n; i++) {
            double average = total / (n-i);
            if (p[i] < average) {
                for (j = i; j < n; j++)
                    p[j] = average;
                break;
            } else {
                total -= p[i];
            }
        }
        double ans = 1.0;
        for (i = 0; i < n; i++) {
            //fprintf(stderr, "%lf\n", p[i]);
            ans *= p[i];
        }
        printf("%.8lf\n", ans);
        


    }
}
        