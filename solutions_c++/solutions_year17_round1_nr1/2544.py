#include <bits/stdc++.h>

#define LL long long

using namespace std;

const int maxn = 30;

char cake[maxn][maxn];

int R, C;

char Get(int r, int c){
    for (int j = c + 1; j < C; j++)
        if (cake[r][j] != '?') return cake[r][j];
    for (int j = c - 1; j >= 0; j--)
        if (cake[r][j] != '?') return cake[r][j];
}

int main(){
    freopen("A-large (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++){
        scanf("%d%d", &R, &C);
        for (int i = 0; i < R; i++)
            scanf("%s", cake[i]);
        for (int j = 0; j < C; j++){
            int i = 0;
            while(i < R){
                if (cake[i][j] != '?'){
                    char ch = cake[i][j];
                    while(i < R && (ch == cake[i][j] || cake[i][j] == '?')){
                        cake[i][j] = ch;
                        i++;
                    }
                }
                else
                    i++;
            }
            i = R - 2;
            while(i >= 0){
                if (cake[i][j] == '?') cake[i][j] = cake[i + 1][j];
                i--;
            }
        }
        for (int i = 0; i < R; i++){
            for (int j = 0; j < C; j++){
                if (cake[i][j] == '?')
                    cake[i][j] = Get(i, j);
            }
        }
        printf("Case #%d:\n", cas);
        for (int i = 0; i < R; i++){
            printf("%s\n", cake[i]);
        }
    }
    return 0;
}
