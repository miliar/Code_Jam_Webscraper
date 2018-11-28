#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;

const int maxn = 1100;


char s[11][110];
int f[11][110];
char t[11][110];
//int g[11][110];
struct node {
    int x, y, z;
}w[11000];
void add0(int x, int y) {
    int dx = x, dy = y;
    s[x][y] = '-';
    while (s[dx][dy] != '#') {
        f[dx][dy]++;
        dy--;
    }
    dx = x, dy = y+1;
    while (s[dx][dy] != '#') {
        f[dx][dy]++;
        dy++;
    }
}
void del0(int x, int y) {
    int dx = x, dy = y;

    while (s[dx][dy] != '#') {
        f[dx][dy]--;
        dy--;
    }
    dx = x, dy = y+1;
    while (s[dx][dy] != '#') {
        f[dx][dy]--;
        dy++;
    }
}
void add1(int x, int y) {
    int dx = x, dy = y;
    s[x][y] = '|';
    while (s[dx][dy] != '#') {
        f[dx][dy]++;
        dx--;
    }
    dx = x+1, dy = y;
    while (s[dx][dy] != '#') {
        f[dx][dy]++;
        dx++;
    }
}
void calc(int i, int j) {
    int x = i, y = j;
    while (s[x][y] == '.') x--;
    if (s[x][y] == '-' || s[x][y] == '|') {
        del0(x, y);
        add1(x, y);
        return;
    }
    x = i, y = j;
    while (s[x][y] == '.') x++;
    if (s[x][y] == '-' || s[x][y] == '|') {
        del0(x, y);
        add1(x, y);
        return;
    }
    
}
int n, m;
int main() {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i <= n+1; i++)
            for (int j = 0; j <= m+1; j++) s[i][j] = '#';
        for (int i = 1; i <= n; i++)
            scanf("%s", s[i]+1);
        
        
        
        
        memset(f,0,sizeof(f));
        
        int tot = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                t[i][j] = s[i][j];
                if (s[i][j] == '|' || s[i][j] == '-') {
                    add0(i, j);
                    
                    tot++;
                    w[tot].x = i;
                    w[tot].y = j;
                //    g[i][j] = tot;
                }
            }
        }
        for (int i = 1; i <= tot; i++) w[i].z = f[w[i].x][w[i].y];
        
        for (int i = 1; i <= tot; i++) if (w[i].z > 1) {
            del0(w[i].x, w[i].y);
            add1(w[i].x, w[i].y);
        }
        
        
        int sum = 0;
        while (1) {
            bool ff = false;
            sum++;
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= m; j++) {
                    if (s[i][j] == '.' && f[i][j] == 0) {
                        calc(i, j);
                        ff = true;
                        break;
                    }
                    
                }
                if (ff) break;
            }
            
            if (!ff || sum > 300) break;
        }
        bool ans = 1;
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++) if (s[i][j] == '.' && f[i][j] == 0) {
                ans = 0;
            }
        for (int i = 1; i <= tot; i++) {
            w[i].z = f[w[i].x][w[i].y];
            if (w[i].z > 1) ans = 0;
        }
        printf("Case #%d: ", ++cas);
        if (ans) {
            printf("POSSIBLE\n");
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= m; j++) printf("%c", s[i][j]);
                printf("\n");
            }
        } else {
            printf("IMPOSSIBLE\n");
            /*
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= m; j++) printf("%c", t[i][j]);
                printf("\n");
            }*/
        }
        
    }
    
}
