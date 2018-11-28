#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

int main(){
    int T;
    cin >> T;

    for (int t = 1  ; t <= T; t++){
        int R,C;
        cin >> R;
        cin >> C;

        char G[30][30];

        string s;

        for (int i = 0 ; i < R;  i++){
            cin >> s;

            for (int j = 0 ; j < C; j++){

                G[i][j] = s[j];
            }
        }

        for (int i = 1; i < R; i++){

            for (int j = 0 ; j < C ; j++){

                if (G[i][j] == '?'){

                    G[i][j] = G[i-1][j];
                }
            }
        }

        for (int i = R-2; i >=0 ; i--){
            for (int j = 0 ; j < C ; j++){

                if (G[i][j] == '?'){

                    G[i][j] = G[i+1][j];
                }
            }
        }

        for (int j = 1 ; j < C; j++){
            for (int i = 0 ; i < R; i++){
                if (G[i][j] == '?'){

                    G[i][j] = G[i][j-1];
                }
            }

        }

        for (int j = C-2 ; j >= 0; j--){
            for (int i = 0 ; i < R; i++){
                if (G[i][j] == '?'){

                    G[i][j] = G[i][j+1];
                }
            }
        }
        printf("Case #%d:\n",t);
        for (int i = 0; i < R; i++){

            for (int j = 0 ; j< C; j++){

                printf("%c",G[i][j]);
            }
            printf("\n");
        }
    }

}
