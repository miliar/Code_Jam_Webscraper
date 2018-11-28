#include <bits/stdc++.h>
using namespace std;
int t, n, k;
int main() {
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    scanf("%d", &t);
    for (int z=0;z<t;z++) {
        scanf("%d %d", &n, &k);
        bool a[1005];
        memset (a, 0, sizeof a);
        a[0] = 1, a[n+1] = 1;
        for (int i=0;i<k;i++) {
            int ma=0, mi=0, s;
            for (int j=1;j<=n;j++) {
                if (a[j]==1) continue;
                int x, y;
                for (int k=j-1;k>=0;k--) {
                    if (a[k]==1) {
                        x = j-k-1;
                        break;
                    }
                }   
                for (int k=j+1;k<=n+1;k++) {
                    if (a[k]==1) {
                        y = k-j-1;
                        break;
                    }
                }   
                if (x<y) swap (x, y);
                //printf("x=%d y=%d\n", x, y);
                if (y>mi||(y==mi&&x>ma)) {
                    mi = y, ma = x, s = j;
                }
            }
            a[s] = 1;
            if (i==k-1) printf("Case #%d: %d %d\n", z+1, ma, mi);
        }
    }
}
