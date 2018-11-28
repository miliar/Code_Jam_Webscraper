#include <bits/stdc++.h>


using namespace std;
const int N = 30;
char a[N][N], b[N][N];
int n , m;
bool flag;

void gao(int x, int y) {
    if(flag) return;
    if(x >= n) {
        for(int i = 0 ; i < n ; i ++) {
            for(int j = 0 ; j < m ; j ++) {
                printf("%c", b[i][j]);
            }
            puts("");
        }
        flag = true;
        return ;
    }
    if(y >= m) {
        gao(x + 1, 0);
        return ;
    }
    if(b[x][y] != '?') {
        gao(x, y + 1);
        return ;
    }
    for(int i = x; i < n ; i ++) {
        for(int j = y ; j < m ; j ++) {
            int ok = 1;
            char p = '?';
            for (int xx = x ; xx <= i && ok ; xx ++) {
                for(int yy = y ; yy <= j && ok; yy ++) {
                    if(b[xx][yy] != '?') {
                        ok = 0;
                    }
                    if(a[xx][yy] != '?') {
                        if(p == '?') {
                            p = a[xx][yy];
                        }
                        else {
                            ok = 0;
                        }
                    }
                }
            }
            if(p == '?') ok = 0;
            if(ok) {
                for (int xx = x ; xx <= i && ok ; xx ++) {
                    for(int yy = y ; yy <= j && ok; yy ++) {
                        b[xx][yy] = p;
                    }
                }
                gao(x , y + 1);
                for (int xx = x ; xx <= i && ok ; xx ++) {
                    for(int yy = y ; yy <= j && ok; yy ++) {
                        b[xx][yy] = '?';
                    }
                }
            }
        }
    }
}

int main () {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t --) {
        printf("Case #%d:\n", ++ cas);
        scanf("%d %d" , &n, &m);
        for(int i = 0 ; i < n ; i ++) {
            scanf("%s", a[i]);
        }
        for(int i = 0 ; i < n ; i ++) {
            for(int j = 0 ; j < m ; j ++) {
                b[i][j] = '?';
            }
        }
        flag = false;
        gao(0, 0);

    }


    return 0;
}