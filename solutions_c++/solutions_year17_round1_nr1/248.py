#include <cstdio>

int main(){
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int T, R, C;
    char cake[26][26];
    scanf("%d", &T);

    for(int t = 1; t <= T; t++){
        scanf("%d%d ", &R, &C);

        for(int i = 0; i < R; i++)
            scanf(" %s", cake[i]);

        for(int i = 0; i < R; i++){
            char ins = '?';
            for(int j = 0; j < C; j++){
                if(cake[i][j] != '?') ins = cake[i][j];
                else cake[i][j] = ins;
            }

            ins = '?';
            for(int j = C-1; j >= 0; j--){
                if(cake[i][j] != '?') ins = cake[i][j];
                else cake[i][j] = ins;
            }
        }

        for(int j = 0; j < C; j++){
            char ins = '?';
            for(int i = 0; i < R; i++){
                if(cake[i][j] != '?') ins = cake[i][j];
                else cake[i][j] = ins;
            }

            ins = '?';
            for(int i = R-1; i >= 0; i--){
                if(cake[i][j] != '?') ins = cake[i][j];
                else cake[i][j] = ins;
            }
        }

        for(int i = 0; i < R; i++){
            char ins = '?';
            for(int j = 0; j < C; j++){
                if(cake[i][j] != '?') ins = cake[i][j];
                else cake[i][j] = ins;
            }

            ins = '?';
            for(int j = C-1; j >= 0; j--){
                if(cake[i][j] != '?') ins = cake[i][j];
                else cake[i][j] = ins;
            }
        }

        printf("Case #%d:\n", t);
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++)
                printf("%c", cake[i][j]);
            printf("\n");
        }
    }
}
