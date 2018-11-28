#include <cstdio>

using namespace std;

char s[26][26];

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int r, c, j, k, l;
        
        scanf("%d %d", &r, &c);
        
        for (j = 0; j < r; j++) scanf("%s", s[j]);
        
        for (j = 0; j < r; j++) {
            int x = -1;
            
            for (k = 0; k < c; k++) {
                if (s[j][k] == '?') continue;
                
                for (l = x + 1; l < k; l++) s[j][l] = s[j][k];
                
                x = k;
            }
            
            if (x >= 0) {
                for (l = x + 1; l < c; l++) s[j][l] = s[j][x];
            }
        }
        
        for (j = 0; j < c; j++) {
            int x = -1;
            
            for (k = 0; k < r; k++) {
                if (s[k][j] == '?') continue;
                
                for (l = x + 1; l < k; l++) s[l][j] = s[k][j];
                
                x = k;
            }
            
            if (x >= 0) {
                for (l = x + 1; l < r; l++) s[l][j] = s[x][j];
            }
        }
        
        printf("Case #%d:\n", i + 1);
        for (j = 0; j < r; j++) {
            for (k = 0; k < c; k++) {
                putchar(s[j][k]);
            }
            puts("");
        }
    }
    
    return 0;
}
