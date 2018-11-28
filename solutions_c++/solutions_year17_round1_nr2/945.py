#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
typedef long long ll;
int n, p;
ll a[55][55];
ll nd[55];
int check() {
    int res = 0;
    for(int i = 1; i <= p; ++i) {
        ll k = max(a[1][i]/nd[1]-5555,1ll);
        for(int j = 2; j <= n; ++j) {
            k = max(k, max(a[j][i]/nd[j]-5555, 1ll));
        }
        for(; k <= 1000000; ++k) {
            int flag = 1;
            for(int j = 1; j <= n; ++j) {
                if(nd[j]*k*11 < 10*a[j][i]) {
                    flag = 0;
                    break;
                }
                if(nd[j]*k*9 > 10*a[j][i]) {
                    goto l2;
                }
                
            }
            if(flag) {
                res++;
                break;
            }
        }
    l2:;
    }
    return res;
}
int main() {
    int T, ca = 1;
    scanf("%d", &T);
    while(T--) {
        scanf("%d %d", &n, &p);
        for(int i = 1; i <= n; ++i) {
            scanf("%lld", nd+i);
        }
        for(int i = 1; i <= n; ++i) {
            for(int j = 1; j <= p; ++j) {
                scanf("%lld", a[i]+j);
            }
        }
        for(int i = 1; i <= n; ++i) {
            sort(a[i]+1, a[i]+p+1);
        }
        int ans = 0;
        do {
            ans = max(ans, check());
        } while(next_permutation(a[1]+1, a[1]+p+1));
        printf("Case #%d: %d\n", ca++, ans);
    }
}
