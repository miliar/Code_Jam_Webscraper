#include <bits/stdc++.h>

using namespace std;

int t,tes,i,j,k;
int a[107];
int ans[107];
int mem[107][107][107];
long long n;

int DP(int pos, int last, int naik) {
    if (pos == -1) return 1;
    if (mem[pos][last][naik] != -1) return mem[pos][last][naik];
    
    int i;
    
    //printf("%d %d %d\n",pos,last,naik);
    
    if (naik == 1) {
        i = a[pos];
        if (i >= last && DP(pos-1,i,1) != -999) {
            ans[pos] = i;
            return mem[pos][last][naik] = i;
        }
        for (i=a[pos]-1 ; i>=last ; i--) if (DP(pos-1,i,0) != -999) {
            ans[pos] = i;
            return mem[pos][last][naik] = i;
        }
        return mem[pos][last][naik] = -999;
    } else {
        for (i=9 ; i>=last ; i--) if (DP(pos-1,i,0) != -999) {
            ans[pos] = i;
            return mem[pos][last][naik] = i;
        }
        return mem[pos][last][naik] = -999;
    }
}

int main() {
    scanf("%d",&t);
    for (tes=1 ; tes<=t ; tes++) {
        scanf("%lld",&n);
        
        k = 0;
        while (n != 0) {
            a[k++] = n % 10;
            n /= 10;
        }
        
        for (i=0 ; i<=k ; i++) {
            for (j=0 ; j<=9 ; j++) {
                mem[i][j][0] = -1;
                mem[i][j][1] = -1;
            }
            ans[i] = 0;
        }
        
        printf("Case #%d: ",tes);
        k--;
        int ans = DP(k,0,1);
        bool yes = false;
        bool masi = true;
        
        while (k >= 0) {
            if (ans != 0) yes = true;
            if (ans != a[k]) masi = false;
            if (yes) printf("%d",ans);
            k--;
            ans = DP(k,ans,masi ? 1 : 0);
        }
        printf("\n");
    }   
}
