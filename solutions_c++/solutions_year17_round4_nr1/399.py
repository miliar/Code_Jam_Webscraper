#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>
#include<assert.h>
using namespace std;using namespace std;
const int maxn = 205;
int A[maxn];
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt","w", stdout);
    int T; scanf("%d",&T);
    for(int cas = 1; cas <= T; cas ++) {
        int n, p, ans = 1; scanf("%d%d", &n, &p);
        int M = 0;
        for(int i = 0; i < n; i ++) {
            scanf("%d", &A[i]);
            A[i] %= p;
            M += A[i];
        }
        sort(A, A + n);
        if (p == 2) {
            int res = 0;
            for(int i = 0; i < n; i ++) {
                if (A[i] == 0) ans ++;
                else res ++;
            }
            ans += res / 2;
        }
        else if(p == 3) {
            int x = 0, y = 0; ans = 1;
            for(int i = 0; i < n; i ++) {
                if (A[i] == 0) {
                    ans ++;
                }
                else if(A[i] == 1) {
                    x ++;
                }
                else{
                    y ++;
                }
            }
            int t = min(x, y);

            x -= t, y -= t;
                ans += t;
                ans += x / 3;
                ans += y / 3;
        }
        else{
            int x = 0, y = 0, z = 0; ans = 1;
            for(int i = 0; i < n; i ++) {
                if (A[i] == 0) {
                    ans ++;
                }
                else if(A[i] == 1) {
                    x ++;
                }
                else if(A[i] == 2){
                    z ++;
                }
                else{
                    y ++;
                }
            }
            int t = min(x, y);
            x -= t, y -= t;
            ans += t;
            ans += z / 2;
            ans += x / 4;
            ans += y / 4;
            x = x%4 + y%4;
            if( z%2 == 1 && x >= 2 )
                ans++;
        }
        if( M % p == 0 ) ans--;
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
