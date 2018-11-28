#include <bits/stdc++.h>
using namespace std;

#define ll unsigned long long

int main() {
    int test, kase = 0;
    ll n, k;
    scanf("%d", &test);
    while(test--) {
        scanf("%llu%llu", &n, &k);
        ll kk = k, x = n, y = n, op = 0;
        while(kk > 0) {
            if(n & 1) 
                x = n / 2, y = n / 2;
            else 
                x = n / 2 - 1, y = n / 2;

            kk--;
            op = kk & 1;
            if(op == 1) n = y;
            else n = x;

            kk = kk / 2;
            if(op) kk++;
        }


        printf("Case #%d: %llu %llu\n", ++kase, y, x);
    }
    return 0;
}