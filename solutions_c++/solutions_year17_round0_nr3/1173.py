#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
    int TT, T;
    scanf("%d", &TT);
    
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        
        long long n, k;
        scanf("%lld%lld", &n, &k);
        
        long long x=n, xspaces=1, xpspaces=0;
        
        while (xspaces + xpspaces < k) {
            k -= (xspaces+xpspaces);
            if (x%2 == 0) {
                x = x/2-1;
                xpspaces = 2*xpspaces + xspaces;
            } else {
                x = (x-1)/2;
                xspaces = 2*xspaces + xpspaces;
            }
        }
        long long finalspace;
        if (k <= xpspaces)
            finalspace = x+1;
        else 
            finalspace = x;
        
        if (finalspace%2 == 0)
            printf("%lld %lld\n", finalspace/2, finalspace/2-1);
        else
            printf("%lld %lld\n", finalspace/2, finalspace/2);


    }
}
        