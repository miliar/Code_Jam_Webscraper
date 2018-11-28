#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;

int T, n, m;
char cake[30][30];
int border[30][4];

int boraden(int v, int dir) {
    
    if (dir == 0) {
        if (border[v][1] == 0) return 0;
        
        for (int i = border[v][0]; i <= border[v][2]; i++) {
            if (cake[i][ border[v][1] - 1] != '?') {
                return 0;
            }
        }
        
        char tmp = 'A' + v;
        for (int i = border[v][0]; i <= border[v][2]; i++) {
            cake[i][ border[v][1] - 1] = tmp;
        }
        
        border[v][1]--;
        return border[v][2] - border[v][0] + 1;
    }
    
    if (dir == 1) {
        if (border[v][3] == m - 1) return 0;
        
        for (int i = border[v][0]; i <= border[v][2]; i++) {
            if (cake[i][ border[v][3] + 1] != '?') {
                return 0;
            }
        }
        char tmp = 'A' + v;
        for (int i = border[v][0]; i <= border[v][2]; i++) {
            cake[i][ border[v][3] + 1] = tmp;
        }
        
        border[v][3]++;
        return border[v][2] - border[v][0] + 1;
    }
    
    if (dir == 2) {
        if (border[v][0] == 0) return 0;
        
        for (int i = border[v][1]; i <= border[v][3]; i++) {
            if (cake[ border[v][0] - 1][i] != '?') {
                return 0;
            }
        }
        
        char tmp = 'A' + v;
        for (int i = border[v][1]; i <= border[v][3]; i++) {
            cake[ border[v][0] - 1][i] = tmp;
        }
        border[v][0]--;
        return border[v][3] - border[v][1] + 1;
    }
    
    if (dir == 3) {
        if (border[v][2] == n - 1) return 0;
        
        for (int i = border[v][1]; i <= border[v][3]; i++) {
            if (cake[ border[v][2] + 1][i] != '?') {
                return 0;
            }
        }
        
        char tmp = 'A' + v;
        for (int i = border[v][1]; i <= border[v][3]; i++) {
            cake[ border[v][2] + 1][i] = tmp;
        }
        border[v][2]++;
        return border[v][3] - border[v][1] + 1;
    }
    
    return 0;
}

int main() {
    scanf("%d", &T);
    bool used[30];
    
    for(int cas = 1; cas <= T; cas++) {
        scanf("%d%d", &n, &m);
        memset(used, 0, sizeof(used));
        
        for (int i = 0; i < n; i++) scanf("%s", cake[i]);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (cake[i][j] != '?' && !used[ cake[i][j] - 'A']) {
                    int lm = m, rm = -1, um = n, dm = -1;
                    for (int ii = 0; ii < n; ii++) {
                        for (int jj = 0; jj < m; jj++) {
                            if (cake[ii][jj] == cake[i][j]) {
                                lm = min(lm, jj), rm = max(rm, jj);
                                um = min(um, ii), dm = max(dm, ii);
                            }
                        }
                    }
                    border[ cake[i][j] - 'A'][0] = um, border[ cake[i][j] - 'A'][1] = lm;
                    border[ cake[i][j] - 'A'][2] = dm, border[ cake[i][j] - 'A'][3] = rm;
                    used[ cake[i][j] - 'A'] = true;
                    
                    char tmp = cake[i][j];
                    for (int ii = um; ii <= dm; ii++) {
                        for (int jj = lm; jj <= rm; jj++) cake[ii][jj] = tmp;
                    }
                }
            }
        }
        
        int left = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (cake[i][j] == '?') left++;
        
        while (left) {
            for (int i = 0; i < 26; i++) {
                if (used[i]) {
                    for (int dir = 0; dir < 4; dir++) {
                        int tmp = boraden(i, dir);
                        //if (tmp != 0) cerr << tmp << endl;
                        left -= tmp;
                    }
                }
            }
        }
        
        printf("Case #%d:\n", cas);
        for (int i = 0; i < n; i++) printf("%s\n", cake[i]);
            
    }
    return 0;
}