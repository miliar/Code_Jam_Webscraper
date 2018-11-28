#include <cstdio>

int T;
char in[30][30];
int n, m;

int main() {
    scanf("%d", &T);
    for(int tt = 1; tt <= T; tt++){
        scanf("%d %d", &n, &m);
        for(int i = 0; i < n; i++){
            scanf("%s", in[i]);
        }

        for(int i = 0; i < n; i++){
            for(int j = 1; j < m; j++){
                if(in[i][j - 1] != '?' && in[i][j] == '?'){
                    in[i][j] = in[i][j - 1];
                }
            }
        }

        for(int i = 0; i < n; i++){
            for(int j = m - 2; j >= 0; j--){
                if(in[i][j + 1] != '?' && in[i][j] == '?'){
                    in[i][j] = in[i][j + 1];
                }
            }
        }

        for(int i = 1; i < n; i++){
            for(int j = 0; j < m; j++){
                if(in[i - 1][j] != '?' && in[i][j] == '?'){
                    in[i][j] = in[i - 1][j];
                }
            }
        }

        for(int i = n - 2; i >= 0; i--){
            for(int j = 0; j < m; j++){
                if(in[i + 1][j] != '?' && in[i][j] == '?'){
                    in[i][j] = in[i + 1][j];
                }
            }
        }

        printf("Case #%d:\n", tt);
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                printf("%c", in[i][j]);
            }
            printf("\n");
        }
    }
}
