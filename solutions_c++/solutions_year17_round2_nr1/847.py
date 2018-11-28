#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <deque>
#include <vector>

using namespace std;


int main() {
    int TT, T;
    scanf("%d", &TT);
    
    
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        
        double d;
        int n;
        
        double maxTime = 0.0;
        
        scanf("%lf %d", &d, &n);
        
        int i;
        for (i = 0; i < n; i++) {
            double p, s;
            scanf("%lf %lf", &p, &s);
            if ((d-p)/s > maxTime)
                maxTime = (d-p)/s;
        }
        
        printf("%.8f\n", d/maxTime);
        

    }
}
        