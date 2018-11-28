#include<stdio.h>
#include<stdlib.h>
int main()
{
    int T,R,C;
    scanf("%d",&T);
    for(int k = 1; k <= T; k++) {
        scanf("%d%d",&R,&C);
        char cake[R][C+1];
        for(int r = 0; r < R; r++) {
            scanf("%s",cake[r]);
        }
        /* scan each row for all ??*/
        bool no[R];
        for(int r = 0; r < R; r++ ) {
            bool all = true;
            for(int c = 0; c < C; c++){
                if(cake[r][c] != '?') {
                    all = false;
                    break;
                }
            }
            no[r] = all;
        }
        for(int ind = 0; ind < R; ind++) {
            if( no[ind] ) continue;
            int modi = ind-1;
            while(modi >= 0 && no[modi]) {
                for(int c = 0; c < C; c++)
                    cake[modi][c] = cake[ind][c];
                --modi;
            }
            modi = ind+1;
            while(modi < R && no[modi]) {
                for(int c = 0; c < C; c++)
                    cake[modi][c] = cake[ind][c];
                ++modi;
            }
        }
        /***************************/
        for(int r = 0; r < R; r++ ) {
            for(int c = 0; c < C; c++){
                if('?' == cake[r][c] ) continue;
                int index = c - 1;
                while(index >= 0 && '?' == cake[r][index]) {
                    cake[r][index] = cake[r][c];
                    --index;
                }
                index = c + 1;
                while(index < C && '?' == cake[r][index]) {
                    cake[r][index] = cake[r][c];
                    ++index;
                }
            }
        }
        printf("Case #%d:\n",k);
        for(int r = 0; r < R; r++) {
            printf("%s\n",cake[r]);
        }
    }
    return 0;
}
