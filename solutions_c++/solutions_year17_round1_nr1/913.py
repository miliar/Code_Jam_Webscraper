#include <bits/stdc++.h>

using namespace std;



int n, m;
char s[100][100];


int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase = 1; kase <= T; kase ++) {
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; i ++) {
            scanf("%s", s[i]);
        }

        for(int i = 0; i < n; i ++) {
            char ps = 0;
            for(int j = 0; j < m; j ++) {
                if(s[i][j] != '?') ps = s[i][j];
                if(s[i][j] == '?' && ps != 0) s[i][j] = ps;
            }
            ps = 0;
            for(int j = m - 1; j >= 0; j --) {
                if(s[i][j] != '?') ps = s[i][j];
                if(s[i][j] == '?' && ps) s[i][j] = ps;
            }
        }

        for(int j = 0; j < m; j ++) {
            char ps = 0;
            for(int i = 0; i < n; i ++) {
                if(s[i][j] != '?') ps = s[i][j];
                if(s[i][j] == '?' && ps != 0) s[i][j] = ps;
            }
            ps = 0;
            for(int i = n - 1; i >= 0; i --) {
                if(s[i][j] != '?') ps = s[i][j];
                if(s[i][j] == '?' && ps) s[i][j] = ps;
            }
        }

        printf("Case #%d:\n", kase);
        for(int i = 0; i < n; i ++) {
            for(int j = 0; j <m; j ++) {
                printf("%c", s[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
