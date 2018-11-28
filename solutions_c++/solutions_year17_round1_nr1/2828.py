#include <bits/stdc++.h>

using namespace std;

char cake[50][50];
bool vis[50][50];
int r, c;

void paint(int x, int y) {
    char initial = cake[x][y];
    int left = max(y-1, 0), right = min(y+1, c-1);
    vis[x][y] = true;
    if (cake[x][left] == '?' || cake[x][right] == '?') {
        for(int j=right; j<c && cake[x][j] == '?'; j++) {
            cake[x][j] = initial;
            vis[x][j] = true;
        }
        for(int j=left; j>=0 && cake[x][j] == '?'; j--) {
            cake[x][j] = initial;
            vis[x][j] = true;
        }
        return;
    }
    int top = max(x-1, 0), bottom = min(x+1, r-1);
    if (cake[top][y] == '?' || cake[bottom][y] == '?') {
        for(int i=bottom; i<r && cake[i][y] == '?'; i++) {
            cake[i][y] = initial;
            vis[i][y] = true;
        }
        for(int i=top; i>=0 && cake[i][y] == '?'; i--) {
            cake[i][y] = initial;
            vis[i][y] = true;
        }
        return;
    }
}

int main() {
    int t;
    scanf("%d", &t);
    for(int tc=0; tc<t; tc++) {
        memset(vis, 0, sizeof vis);
        scanf("%d%d", &r, &c);
        for(int i=0; i<r; i++) {
            scanf("%s", cake[i]);
        }
        for(int i=0;i<r; i++) {
            for(int j=0; j<c; j++) {
                if (cake[i][j] != '?' && !vis[i][j]) {
                    paint(i, j);
                }
            }
        }
        for(int i=0;i<r-1; i++) {
            for(int j=0;j<c-1; j++) {
                char alp = '?';
                if(cake[i][j] != '?') {
                    if (alp!='?' && cake[i][j]!=alp) continue;
                    alp = cake[i][j];
                }
                if(cake[i][j+1] != '?') {
                    if (alp!='?' && cake[i][j+1]!=alp) continue;
                    alp = cake[i][j+1];
                }
                if(cake[i+1][j] != '?') {
                    if (alp!='?' && cake[i+1][j]!=alp) continue;
                    alp = cake[i+1][j];
                }
                if(cake[i+1][j+1] != '?') {
                    if (alp!='?' && cake[i+1][j+1]!=alp) continue;
                    alp = cake[i+1][j+1];
                }
                if (alp!='?') {
                    cake[i][j] = alp;
                    cake[i][j+1] = alp;
                    cake[i+1][j] = alp;
                    cake[i+1][j+1] = alp;
                }
            }
        }
        printf("Case #%d:\n", tc + 1);
        for(int i=0;i<r; i++) {
            for(int j=0; j<c; j++) {
                printf("%c", cake[i][j]);
            }
            puts("");
        }
    }
    return 0;
}