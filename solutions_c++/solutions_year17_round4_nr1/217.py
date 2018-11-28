#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;


bool cmp2(int a, int b) {
    return (a%2) < (b%2);
}
const int maxn = 110;
int f[maxn][maxn][maxn][5];
int g[maxn][maxn][5];
int a[maxn];
int w[5];
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T, cas = 0;
    int n, k;
    scanf("%d", &T);
    memset(f,0,sizeof(f));
    f[0][0][0][0] = 1;
    for (int i = 0; i <= 100; i++)
        for (int j = 0; j <= 100; j++)
            for (int k = 0; k <= 100; k++)
                for (int z = 0; z < 4; z++) {
                    // las  f[i][j][k][z]  f[i+1][j][k][z+1]
                    
                    f[i+1][j][k][(z+1)%4] = max(f[i+1][j][k][(z+1)%4], f[i][j][k][z] + ((z+1)%4 == 0));
                    
                    f[i][j+1][k][(z+2)%4] = max(f[i][j+1][k][(z+2)%4], f[i][j][k][z] + ((z+2)%4 == 0));
                    
                    f[i][j][k+1][(z+3)%4] = max(f[i][j][k+1][(z+3)%4], f[i][j][k][z] + ((z+3)%4 == 0));
                    
                }
    
    memset(g,0,sizeof(g));
    g[0][0][0] = 1;
    for (int i = 0; i <= 100; i++)
        for (int j = 0; j <= 100; j++)
            for (int z = 0; z < 3; z++) {
                g[i+1][j][(z+1)%3] = max(g[i+1][j][(z+1)%3], g[i][j][z] + ((z+1)%3 == 0));
                
                g[i][j+1][(z+2)%3] = max(g[i][j+1][(z+2)%3], g[i][j][z] + ((z+2)%3 == 0));
            }
    
    while (T--) {
        scanf("%d%d", &n, &k);
        for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
        
        printf("Case #%d: ", ++cas);
        if (k == 2) {
            sort(a+1, a+n+1, cmp2);
            int ss = 0;
            int ans = 0;
            for (int i = 1; i <= n; i++) {
                if (ss == 0) ans++;
                ss = (ss+a[i])%2;
            }
            printf("%d\n", ans);
            continue;
        }
        if (k == 3) {
            memset(w,0,sizeof(w));
            for (int i = 1; i <= n; i++) w[a[i]%3]++;
            
            int x = w[1], y = w[2];
            int ans = g[x][y][0];
            ans = max(ans, g[x][y][1]);
            ans = max(ans, g[x][y][2]);
            
            ans += w[0];
            if ((x+2*y)%3 == 0) ans--;
            printf("%d\n", ans);
            
            continue;
        }
        if (k == 4) {
            memset(w,0,sizeof(w));
            for (int i = 1; i <= n; i++) w[a[i]%4]++;
            
            int x = w[1], y = w[2], z = w[3];
            
            int ans = f[x][y][z][0];
            ans = max(ans, f[x][y][z][1]);
            ans = max(ans, f[x][y][z][2]);
            ans = max(ans, f[x][y][z][3]);
            
            ans += w[0];
            if ((x+2*y+3*z)%4==0) ans--;
            printf("%d\n", ans);
                
            
            continue;
        }
        
    }
    
}