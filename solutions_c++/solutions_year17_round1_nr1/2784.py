#include <cstdio>

int R, C;
char cake[30][30];

int main(){
    int totalCases;
    scanf("%d", &totalCases);
    for(int T = 1; T <= totalCases; ++T){
        scanf("%d%d", &R, &C);
        for(int i = 0; i < R; ++i){
            scanf("%s", cake[i]);
        }
        for(int i = 0; i < R; ++i){
            for(int j = 0; j < C; ++j){
                if(cake[i][j] != '?'){
                    int trav = i;
                    while(trav-1 >= 0 && cake[trav-1][j] == '?')
                        cake[--trav][j] = cake[i][j];
                    trav = i;
                    while(trav+1 < R && cake[trav+1][j] == '?')
                        cake[++trav][j] = cake[i][j];
                }
            }
        }
        for(int j = 0; j < C; ++j){
            if(cake[0][j] == '?'){
                if(j == 0)
                    continue;
                if(cake[0][j-1] != '?'){
                    for(int i = 0; i < R; ++i){
                        cake[i][j] = cake[i][j-1];
                    }
                }
            }
        }
        for(int j = C-1; j >= 0; --j){
            if(cake[0][j] == '?'){
                if(j == C-1)
                    continue;
                if(cake[0][j+1] != '?'){
                    for(int i = 0; i < R; ++i){
                        cake[i][j] = cake[i][j+1];
                    }
                }
            }
        }
        printf("Case #%d:\n", T);
        for(int i = 0; i < R; ++i)
            printf("%s\n", cake[i]);
    }
    return 0;
}
/*
#include <cstdio>

int R, C, cnt, left;
int chk[30], chk2[30], chk3[30][30];
char inp[30];
char cake[30][30];

bool go(int now){
    if(now == left){
        bool pass = true;
        for(int i = 0; i < R && pass; ++i){
            for(int j = 0; j < C && pass; ++j){
                if(chk3[i][j])
                    continue;
                if(!chk2[cake[i][j]-'A']){
                    chk2[cake[i][j]-'A'] = true;
                    int k = j;
                    while(k < C && cake[i][k] == cake[i][j])
                        k++;
                    int l = i;
                    while(l < R && cake[l][j] == cake[i][j])
                        l++;
                    for(int m = i; m < l && pass; ++m){
                        for(int n = j; n < k && pass; ++n){
                            chk3[m][n] = true;
                            if(cake[m][n] != cake[i][j])
                                pass = false;
                        }
                    }
                }
                else
                    pass = false;
            }
        }
        for(int i = 0; i < 30; ++i){
            chk2[i] = 0;
            for(int j = 0; j < 30; ++j){
                chk3[i][j] = 0;
            }
        }
        return pass;
    }
    else{
        for(int i = 0; i < R; ++i){
            for(int j = 0; j < C; ++j){
                if(cake[i][j] == '?'){
                    for(int k = 0; k < cnt; ++k){
                        cake[i][j] = inp[k];
                        if(go(now+1))
                            return true;
                        cake[i][j] = '?';
                    }
                }
            }
        }
    }
    return false;
}

int main(){
    int totalCases;
    scanf("%d", &totalCases);
    for(int T = 1; T <= totalCases; ++T){
        scanf("%d%d", &R, &C);
        cnt = 0;
        left = 0;
        for(int i = 0; i < 30; ++i)
            chk[i] = chk2[i] = 0;
        for(int i = 0; i < R; ++i){
            scanf("%s", cake[i]);
            for(int j = 0; j < C; ++j){
                if(cake[i][j] != '?'){
                    if(chk[cake[i][j]-'A'] == 0){
                        chk[cake[i][j]-'A'] = 1;
                        inp[cnt++] = cake[i][j];
                    }
                }
                else
                    left++;
            }
        }
        go(0);
        printf("Case #%d:\n", T);
        for(int i = 0; i < R; ++i){
            printf("%s\n", cake[i]);
        }
    }
    return 0;
}
*/
