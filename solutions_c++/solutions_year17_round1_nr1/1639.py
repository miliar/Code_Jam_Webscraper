#include <stdio.h>

char cake[100][100];
int y,x;

void solve(){
	for(int i=0;i<y;++i){
		char prev = 0;
		for(int j=0;j<x;++j){
			if(cake[i][j] == '?'){
				if(prev != 0) cake[i][j] = prev;
			}else{
				prev = cake[i][j];
			}
		}
		prev = 0;
        for(int j=x-1;j>=0;--j){
            if(cake[i][j] == '?'){
                if(prev != 0) cake[i][j] = prev;
            }else{
                prev = cake[i][j];
            }
        }
	}

    for(int i=0;i<x;++i){
        char prev = 0;
        for(int j=0;j<y;++j){
            if(cake[j][i] == '?'){
                if(prev != 0) cake[j][i] = prev;
            }else{
                prev = cake[j][i];
            }
        }
        prev = 0;
        for(int j=y-1;j>=0;--j){
            if(cake[j][i] == '?'){
                if(prev != 0) cake[j][i] = prev;
            }else{
                prev = cake[j][i];
            }
        }
    }
}

int main(){
	int test; scanf("%d\n", &test);
	for(int t=1;t<=test;++t){
		scanf("%d %d\n", &y, &x);
		for(int i=0;i<y;++i){
			for(int j=0;j<x;++j){
				scanf("%c", &cake[i][j]);
			}
			scanf("\n");
		}
		solve();
		printf("Case #%d:\n", t);
        for(int i=0;i<y;++i){
            for(int j=0;j<x;++j){
                printf("%c",cake[i][j]);
            }
			printf("\n");
        }
	}
	return 0;
}
