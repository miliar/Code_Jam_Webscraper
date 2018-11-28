#include <cstdio>
#include <iostream>


int main(){
    char table[200*200];
    int T,R,C;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        printf("Case #%d:\n", t);
        scanf("%d %d", &R, &C);

        for(int r = 0; r < R; r++)
            for(int c = 0; c < C; c++){
                scanf(" %c", &table[r*C +c]);
            }
        for(int r = 0; r < R; r++){
            for(int c = 0; c < C; c++){
                if(table[r*C +c] == '?' && c-1 >= 0)
                    table[r*C +c] = table[r*C +c-1];
                 if(table[r*C +c] == '?' && c+1 < C)
                    table[r*C +c] = table[r*C +c+1];
                
            }
            for(int c = C-1; c >= 0; c--){
                if(table[r*C +c] == '?' && c+1 < C)
                    table[r*C +c] = table[r*C +c+1];
                if(table[r*C +c] == '?' && c-1 >= 0)
                    table[r*C +c] = table[r*C +c-1];
            }
        }
    
        for(int c = 0; c < C; c++){
            for(int r = 0; r < R; r++){
                if(table[r*C +c] == '?' && r-1 >= 0)
                    table[r*C +c] = table[(r-1)*C +c];
                 if(table[r*C +c] == '?' && r+1 < R)
                    table[r*C +c] = table[(r+1)*C +c];
                
            }
            for(int r = R-1; r >= 0; r--){
               if(table[r*C +c] == '?' && r-1 >= 0)
                    table[r*C +c] = table[(r-1)*C +c];
                 if(table[r*C +c] == '?' && r+1 < R)
                    table[r*C +c] = table[(r+1)*C +c];
            }
        }
        for(int r = 0; r < R; r++){
            for(int c = 0; c < C; c++)
                printf("%c",table[r*C +c]);
            printf("\n");
        }
    }
    return 0;
}
