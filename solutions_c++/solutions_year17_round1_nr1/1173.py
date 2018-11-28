#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

int R, C;
char G[30][30];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
	scanf("%d",&T);
    for(int cases=1; cases<=T; cases++){
    	printf("Case #%d:\n",cases);
    	scanf("%d %d",&R,&C);
    	for(int i=0; i<R; i++){
    		scanf("%s",G[i]);
    		for(int j=0; j<C; j++){
    			if(G[i][j]!='?'){
    				for(int k=j-1; k>=0; k--){
    					if(G[i][k]=='?') G[i][k] = G[i][j];
    					else break;
					}
					for(int k=j+1; k<C; k++){
    					if(G[i][k]=='?') G[i][k] = G[i][j];
    					else break;
					}
				}
			}
		}
		for(int i=0; i<C; i++){
			for(int j=0; j<R; j++){
				if(G[j][i]!='?'){
    				for(int k=j-1; k>=0; k--){
    					if(G[k][i]=='?') G[k][i] = G[j][i];
    					else break;
					}
					for(int k=j+1; k<R; k++){
    					if(G[k][i]=='?') G[k][i] = G[j][i];
    					else break;
					}
				}
			}
		}
		for(int i=0; i<R; i++) printf("%s\n",G[i]);
	}
    return 0;
}
