#include <bits/stdc++.h>
using namespace std;
int g[27][27];
int t, r, c;

int isvalid(char x) {
    if ((isalpha(x) && isupper(x))) {
        return x-'A';
    } else if (x=='?') {
        return 30;
    } else {
        return -1;
    }
}

int v(int i, int j) {
    if (i < 0 || j < 0 || i >= r || j >= c) return 0;
    return 1;
}

int check() {
           for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (g[i][j] == 30) {
                    return false;
                } 
            }
           }
           return true;
}

void prant() {
            for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (g[i][j] == 30) {
                    printf(".");
                    assert(0);
                } else{
                    printf("%c", g[i][j]+'A');
                }
            }
            printf("\n");
        }
}

int expand(int i, int j) {
    int length = 1;
    int wow = i+1;
    for (int k = i-1; k >= 0; k --) {
        if (g[k][j] == 30 || g[k][j] == g[i][j]) {
            g[k][j] = g[i][j];
            i--;
            length++;
        } else {
            break;
        }
    }
    for (int k = wow; k < r; k++) {
        if (g[k][j] == 30 || g[k][j] == g[i][j]) {
            g[k][j] = g[i][j];
            length ++;
        } else {
            break;
        }
    }
    for (int k = j+1; k < c; k++) {
        bool okay = true;
        for (int l = 0; l < length; l++) {
            if (g[i+l][k] != 30) {
                okay = false;
                break;
            }
        }
        if (okay) {
            for (int l = 0; l < length; l++) {
                g[i+l][k] = g[i][j];
            }
        } else {
            break;
        }
    }
    for (int k = j-1; k >= 0; k--) {
        bool okay = true;
        for (int l = 0; l < length; l++) {
            if (g[i+l][k] != 30) {
                okay = false;
                break;
            }
        }
        if (okay) {
            for (int l = 0; l < length; l++) {
                g[i+l][k] = g[i][j];
            }
        } else {
            break;
        }
    }
}

int main() {
    cin >> t;
    char ch, d;
    int tc = 1;
    while (t--) {
        cin >> r >> c;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> ch;
                d= isvalid(ch);
                if (ch==-1){
                    j--;
                } else {
                    g[i][j]=d;
                }
            }
        }

        int copy[27][27];
        memcpy(copy, g, sizeof g);
        
        bool tried[500] = {0};
        for (int i = 0; i < c; i++) {
            for (int j = 0; j < r; j++) {
                if (g[j][i]!=30 && !tried[g[j][i]]) {
                    expand(j, i);
                    tried[g[j][i]] = true;
                }
            }
        }
        printf("Case #%d:\n", tc++);

        if (check()) {
            prant();
        } else {
            memcpy(g, copy, sizeof g);
            bool tried[500] = {0};
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    if (g[i][j]!=30 && !tried[g[i][j]]) {
                        expand(i, j);
                        tried[g[i][j]] = true;
                    }
                }
            }
            prant();
        }
    }

}