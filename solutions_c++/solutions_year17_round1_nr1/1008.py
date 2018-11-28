#include <bits/stdc++.h>

using namespace std;

int main(int argc, const char * argv[]) {
    
    freopen("/Inputs/GC2017/in.txt", "r", stdin);
    freopen("/Inputs/GC2017/out.txt", "w", stdout);
    
    int t;
    
    scanf("%d", &t);
    
    for (int cn = 1; cn <= t; cn++) {
        int r, c;
        scanf("%d%d", &r, &c);
        char grid[r][c];
        for (int i = 0; i < r; i++) {
            scanf("\n");
            for (int j = 0; j < c; j++) {
                scanf("%c", &grid[i][j]);
            }
        }
        int fr;
        char cc;
        for (fr = 0;; fr++) {
            for (int j = 0; j < c; j++) {
                cc = grid[fr][j];
                if (cc != '?') {
                    goto out;
                }
            }
        }
    out:
        char res[r][c];
        for (int i = 0; i < c; i++) {
            if (grid[fr][i] != '?' && cc != grid[fr][i]) {
                cc = grid[fr][i];
            }
            res[fr][i] = cc;
        }
        for (int i = fr-1; i >= 0; i--) {
            for (int j = 0; j < c; j++) {
                res[i][j] = res[fr][j];
            }
        }
        
        for (int i = fr+1; i < r; i++) {
            char currc = '?';
            for (int j = 0; j < c; j++) {
                currc = grid[i][j];
                if (currc != '?') {
                    break;
                }
            }
            if (currc == '?') {
                for (int j = 0; j < c; j++) {
                    res[i][j] = res[i-1][j];
                }
            } else {
                for (int j = 0; j < c; j++) {
                    if (grid[i][j] != '?' && currc != grid[i][j]) {
                        currc = grid[i][j];
                    }
                    res[i][j] = currc;
                }
            }
        }
        printf("Case #%d:\n", cn);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                printf("%c", res[i][j]);
            }
            printf("\n");
        }
    }
    
    return 0;
}
