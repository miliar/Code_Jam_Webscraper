#include <stdio.h>
#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int n,m;
char brd[44][44];
bool mkr[44];

bool check(){
    for(int i = 1;i <= n; i++){
        if(!mkr[i]) return false;
    }
    return true;
}

int main(int argc, char *argv[]){

    int caseCnt;
    scanf(" %d",&caseCnt);
    for(int d = 1;d <= caseCnt;d++){
        printf("Case #%d:\n",d);
        scanf(" %d %d",&n,&m);
        for(int i = 1;i <= n; i++){
            for(int j = 1;j <= m; j++){
                scanf(" %c",&brd[i][j]);
            }
        }
        memset(mkr,0,sizeof(mkr));
        for(int i = 1;i <= n; i++){
            char fil = 0;
            for(int j = 1;j <= m; j++){
                if(brd[i][j] != '?') {
                    fil = brd[i][j];
                    break;
                }
            }
            if(fil != 0){
                mkr[i] = 1;
                for(int j = 1;j <= m; j++){
                    if(brd[i][j] == '?'){
                        brd[i][j] = fil;
                    }else{
                        fil = brd[i][j];
                    }
                }
            }
        }

        while(!check()){
            for(int i = 1;i < n; i++){
                if(mkr[i] ^ mkr[i+1]){
                    if(mkr[i]){
                        for(int j = 1;j <= m; j++){
                            brd[i+1][j] = brd[i][j];
                        }
                        mkr[i+1] = true;
                    }else{
                        for(int j = 1;j <= m; j++){
                            brd[i][j] = brd[i+1][j];
                        }
                        mkr[i] = true;
                    }
                }
            }
        }

        for(int i = 1;i<= n; i++){
            for(int j = 1;j <= m; j++){
                putchar(brd[i][j]);
            }puts("");
        }
    }

    return 0;
}
