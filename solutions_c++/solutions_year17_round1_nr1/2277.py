#include <bits/stdc++.h>
using namespace std;

char s[30][30], re;
        int n, m;

int count(int lx, int ly, int rx, int ry) {
    int cnt = 0;
    for(int i = lx; i < ly; i ++) {
        for(int j = rx; j < ry; j ++) {
            if(s[i][j] != '?') {
                re = s[i][j];
                cnt ++;
            }
        }    
    }
    
    return cnt;
}

void solve(int lx, int ly, int rx, int ry) {
    if(lx == ly) return;
    if(rx == ry) return;
    if(count(lx, ly, rx, ry) == 1) {
        for(int i = lx; i < ly; i ++) {
            for(int j = rx; j < ry; j ++) {
                s[i][j] = re;
            }
        }
        return;
    }
    int x, y;
    for(int i = lx; i < ly; i ++) {
        int f = 0;
        for(int j = rx; j < ry; j ++) {
            if(s[i][j] != '?') {
                x = i, y = j;
                f = 1;
                break;
            }
        }
        if(f) break;
    }
    for(int j = y+1; j < ry; j ++) {
        int f = 1;
        for(int i = lx; i <= x; i ++) {
            if(s[i][j] != '?') f = 0;
        }
        if(f) y ++;
        else break;
    }
    for(int i = x+1; i < ly; i ++) {
        int f = 1; 
        for(int j = rx; j <= y; j ++) {
            if(s[i][j] != '?') f = 0;
        }
        if(f) x ++;
        else break;
    }
    solve(lx, x+1, rx, y+1);

    solve(lx, x+1, y+1, ry);
    solve(x+1, ly, rx, ry);
}

int main() {
  // freopen("A-large.in", "r", stdin);
  // freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    int cas = 0;
    while(t --) {
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; i ++) {
            scanf("%s", s[i]);
        }
        solve(0, n, 0, m);
        printf("Case #%d:\n", ++ cas);
        for(int i = 0; i < n; i ++) {
            printf("%s\n", s[i]);
        }
    }
}
