#include <stdio.h>
#include <string.h>

int main(){
	int T;
	scanf("%d",&T);
	for(int t=0; t<T; t++){
        int R,C;
        scanf("%d%d",&R,&C);
        char c[R][C];
        for(int i=0; i<R; i++){
            scanf(" %s",c[i]);
        }
        int emptyrow = 0;
        for(int i=0; i<R; i++){
            char first='?';
            for(int j=0; j<C; j++)
                if(c[i][j]!='?'){
                    first = c[i][j];
                    break;
                }
            if(first=='?'){
                if(i==emptyrow)
                    emptyrow++;
                else
                    for(int j=0; j<C; j++)
                        c[i][j] = c[i-1][j];
            }
            char now=first;
            for(int j=0; j<C; j++)
                if(c[i][j]=='?')
                    c[i][j] = now;
                else
                    now = c[i][j];
        }
        if(emptyrow)
            for(int i=0; i<emptyrow; i++)
                for(int j=0; j<C; j++)
                    c[i][j] = c[emptyrow][j];
		printf("Case #%d:\n",t+1);
        for(int i=0; i<R; i++){
            for(int j=0; j<C; j++)
                printf("%c",c[i][j]);
            printf("\n");
        }
	}
	return 0;
}
