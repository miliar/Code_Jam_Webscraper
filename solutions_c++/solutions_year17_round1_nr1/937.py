#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
char s[55][55];
bool vis[55][55];
int n, m;
void left(int i, int j, char x) {
    while(j >= 1 && s[i][j] == '?') {
        s[i][j--] = x;
    }
}
void right(int i, int j, char x) {
    while(j <= m && s[i][j] == '?') {
        s[i][j++] = x;
    }
}
void a() {
    for(int i = 1; i <= n; ++i) {
        if(s[i][1] == '?') {
            for(int j = 1; j <= m; ++j) {
                if(i != n) s[i][j] = s[i+1][j];
            }
        }
    }
}
void b() {
    for(int i = n; i >= 1; --i) {
        if(s[i][1] == '?') {
            for(int j = 1; j <= m; ++j) {
                if(i != 1) s[i][j] = s[i-1][j];
            }
        }
    }
}
int main() {
    int T, ca = 1;
    scanf("%d", &T);
    while(T--) {
        memset(vis, 0, sizeof(vis));
        scanf("%d %d", &n, &m);
        for(int i = 1; i <= n; ++i) {
            scanf("%s", s[i]+1);
        }
        for(int i = 1; i <= n; ++i) {
            for(int j = 1; j <= m; ++j) {
                if(s[i][j] != '?') vis[i][j] = true;
            }
        }
        for(int i = 1; i <= n; ++i) {
            for(int j = 1; j <= m; ++j) {
                if(vis[i][j]) {
                    left(i, j-1, s[i][j]);
                    right(i, j+1, s[i][j]);
                }
            }
        }
        for(int i = 1; i <= 10000; ++i) {
            a();
            b();
        }
        printf("Case #%d:\n", ca++);
        for(int i = 1; i <= n; ++i) {
            puts(s[i]+1);
        }
    }
}
