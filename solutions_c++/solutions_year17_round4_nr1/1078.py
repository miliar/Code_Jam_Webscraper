#include <bits/stdc++.h>

using namespace std;

int t,tes,n,p,x,i,j,k;
int a[107];
int mem[5][107][107][107];

int DP(int sum, int satu, int dua, int tiga) {
    if (satu + dua + tiga == 0) return 0;
    if (mem[sum][satu][dua][tiga] != -1) return mem[sum][satu][dua][tiga];
    
    int ans = 0;
    
    if (p >= 2 && satu > 0) {
        ans = max(ans,DP((sum + 1) % p, satu - 1, dua, tiga));
    }
    if (p >= 3 && dua > 0) {
        ans = max(ans,DP((sum + 2) % p, satu, dua - 1, tiga));
    }
    if (p >= 4 && tiga > 0) {
        ans = max(ans,DP((sum + 3) % p, satu, dua, tiga - 1));
    }
    
    ans += (sum == 0 ? 1 : 0);
    
    return mem[sum][satu][dua][tiga] = ans;
}

int main() {
    scanf("%d",&t);
    
    for (tes=1 ; tes<=t ; tes++) {
        scanf("%d%d",&n,&p);
        for (i=0 ; i<=4 ; i++) a[i] = 0;
        for (i=0 ; i<n ; i++) {
            scanf("%d",&x);
            a[x%p]++;
        }
        
        for (i=0 ; i<=100 ; i++) {
            for (j=0 ; j<=100 ; j++) {
                for (k=0 ; k<=100 ; k++) {
                    mem[0][i][j][k] = -1;
                    mem[1][i][j][k] = -1;
                    mem[2][i][j][k] = -1;
                    mem[3][i][j][k] = -1;
                }
            }
        }
        
        printf("Case #%d: %d\n",tes,a[0] + DP(0,a[1],a[2],a[3]));
    }
}
