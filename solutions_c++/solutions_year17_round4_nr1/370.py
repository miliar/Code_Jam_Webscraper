//created by missever

#include<bits/stdc++.h>
#define MAX 1000000007
using namespace std;
typedef long long LL;

int a[5];
int f[101][101][101];
int g[101][101][101];

void update(int &x,int y) {
    if(x < y) x = y;
}

int main() {
//    freopen("A-large.in","r",stdin);
//    freopen("A.out","w",stdout);
    int t,n,p,i,j,k,l,x,ans;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas++) {
        scanf("%d%d",&n,&p);
        memset(a,0,sizeof(a));
        for(i = 0; i < n; i++) {
            scanf("%d",&x);
            a[x % p]++;
        }
        if(p == 2) ans = a[0] + (a[1] + 1)/ 2;
        else if(p == 3) {
            for(i = 0; i <= a[1]; i++) {
                for(j = 0; j <= a[2]; j++){
                        f[0][i][j] = -1;
                        g[0][i][j] = (i + j * 2) % p;
                }
            }
            f[0][0][0] = 0;
            for(l = 0; l < a[1] + a[2]; l++) {
                for(i = max(0,l - a[2]); i <= a[1] && i <= l; i++) {
                    j = l - i;
                    if(f[0][i][j] == -1) continue;
                    if(i < a[1]) update(f[0][i + 1][j],f[0][i][j] + (g[0][i][j] == 0));
                    if(j < a[2]) update(f[0][i][j + 1],f[0][i][j] + (g[0][i][j] == 0));
                }
            }
            ans = f[0][a[1]][a[2]] + a[0];
        } else {
            for(i = 0; i <= a[1]; i++) {
                for(j = 0; j <= a[2]; j++) {
                    for(k = 0; k <= a[3]; k++){
                            f[i][j][k] = -1;
                            g[i][j][k] = (i + j * 2 + k * 3) % p;
                    }
                }
            }
            f[0][0][0] = 0;
            for(l = 0; l < a[1] + a[2] + a[3]; l++) {
                for(i = max(0,l - a[2] - a[3]); i <= a[1] && i <= l; i++) {
                    for(j = max(0,l - i - a[3]); j <= a[2] && i + j <= l; j++) {
                        k = l - i - j;
                        if(f[i][j][k] == -1) continue;
                        if(i < a[1]) update(f[i + 1][j][k],f[i][j][k] + (g[i][j][k] == 0));
                        if(j < a[2]) update(f[i][j + 1][k],f[i][j][k] + (g[i][j][k] == 0));
                        if(k < a[3]) update(f[i][j][k + 1],f[i][j][k] + (g[i][j][k] == 0));
                    }
                }
            }
            ans = f[a[1]][a[2]][a[3]] + a[0];
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
