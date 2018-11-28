#include <bits/stdc++.h>
using namespace std;
const int N = 100 + 5;
typedef long long LL;
int T, Case, n, p;
int a[N];
int p0, p1, p2, p3;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out0.out", "w", stdout);
    scanf("%d", &T);
    while(T--) {
        scanf("%d%d", &n, &p);
        for(int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
        }
        int ans = 0;
        p0 = p1 = p2 = p3 = 0;
        if(p == 2) {
            int flag = 1;
            for(int i = 0; i < n; i++) {
                if(a[i]%2 == 0) ans++;
                else {
                    ans += flag;
                    flag ^= 1;
                }
            }
        }else if(p == 3) {
            for(int i = 0; i < n; i++) {
                if(a[i]%3 == 0) p0++;
                else if(a[i]%3 == 1) p1++;
                else p2++;
            }
            ans = p0;
            int t = min(p1, p2);
            ans += t;
            p1 -= t;
            p2 -= t;
            ans += p1/3 + (p1%3 != 0) + p2/3 + (p2%3 != 0);
        }
        printf("Case #%d: %d\n", ++Case, ans);
    }
    return 0;
}
