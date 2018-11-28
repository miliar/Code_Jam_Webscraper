#include <bits/stdc++.h>
using namespace std;
int t,d,n,k,s;
double xam;
int main(){
    scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        scanf("%d %d", &d, &n);
        xam = 0;
        for (int j = 0; j < n; j++){
            scanf("%d %d", &k, &s);
            xam = max(xam,(double)(d-k)/s);
        }
        printf("Case #%d: %.6f\n", i, (double)d/xam);
    }
}
