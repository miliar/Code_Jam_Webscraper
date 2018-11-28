#include <cstdio>
#include <set>

using namespace std;

const int MAXN = 25 + 5;

int TC, tc;

int R, C;
char B[MAXN][MAXN];
set<char> bst;

int main() {
    freopen("i.in", "r", stdin);
    freopen("o.out", "w", stdout);
    scanf("%d", &TC);

    while(TC--) {
        scanf("%d%d", &R, &C);
        for(int i = 0; i < R; i++)
            scanf("%s", B[i]);
        bst.clear();
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                if(B[i][j] != '?' && !bst.count(B[i][j])) {
                    bst.insert(B[i][j]);
                    int r = i - 1;
                    while(r >= 0 && B[r][j] == '?')
                        B[r--][j] = B[i][j];
                    r++;
                    int c = j - 1;
                    while(c >= 0 && B[r][c] == '?') {
                        for(int k = r; k <= i; k++)
                            B[k][c] = B[i][j];
                        c--;
                    }
                    c++;
                    int c2 = j + 1;
                    while(c2 < C && B[i][c2] == '?') {
                        for(int k = r; k <= i; k++)
                            B[k][c2] = B[i][j];
                        c2++;
                    }
                    c2--;
                    bool cover = true;
                    r = i + 1;
                    while(r < R && cover) {
                        for(int k = c; k <= c2; k++)
                            if(B[r][k] != '?')
                                cover = false;
                        if(cover) {
                            for(int k = c; k <= c2; k++)
                                B[r][k] = B[i][j];
                            r++;
                        }
                    }
                }
            }
        }
        printf("Case #%d:\n", ++tc);
        for(int i = 0; i < R; i++)
            printf("%s\n", B[i]);
    }
}
