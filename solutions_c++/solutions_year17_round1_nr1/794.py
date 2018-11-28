#include <iostream>
#include <cstdio>

using namespace std;

char ch[30][30];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, cnt = 0;
    scanf("%d", &T);
    while(T--) {
        printf("Case #%d:\n", ++cnt);
        int R, C;
        scanf("%d%d", &R, &C);
        int k;
        for(int i = 1; i <= R; i++) {
            scanf("%s", ch[i]+1);
            for(int j = 1; j <= C; j++)
                if(ch[i][j] != '?') k = i;
        }
        /*for(int j = 1; j <= C; j++) if(ch[k][j] == '?') {
            char c;
            for(int l = 1; l <= C; l++)
                if(ch[k][l] != '?') c = ch[k][l];
            for(int l = j; l <= C; l++)
                if(ch[k][l] == '?') ch[k][l] = c;
                else break;
        }*/
        char c = 0;
        for(int l = 1; l <= C; l++)
            if(ch[k][l] == '?') {
                if(c) ch[k][l] = c;
                else {
                    for(int p = l+1; p <= C; p++)
                        if(ch[k][p] != '?') {c = ch[k][p]; break;}
                        ch[k][l] = c;
                    }
                } else {
                    c = ch[k][l];
                }
        for(int i = k-1; i; i--) {
            bool flag = false;
            for(int l = 1; l <= C; l++)
                if(ch[i][l] != '?') flag = true;
            if(!flag) {
                for(int l = 1; l <= C; l++) ch[i][l] = ch[i+1][l];
            } else {
                c = 0;
                for(int l = 1; l <= C; l++)
                    if(ch[i][l] == '?') {
                        if(c) ch[i][l] = c;
                        else {
                            for(int p = l+1; p <= C; p++)
                                if(ch[i][p] != '?') {c = ch[i][p]; break;}
                            ch[i][l] = c;
                        }
                    } else {
                        c = ch[i][l];
                    }
            }
        }
        for(int i = k+1; i <= R; i++) {
            bool flag = false;
            for(int l = 1; l <= C; l++)
                if(ch[i][l] != '?') flag = true;
            if(!flag) {
                for(int l = 1; l <= C; l++) ch[i][l] = ch[i-1][l];
            } else {
                char c = 0;
                for(int l = 1; l <= C; l++)
                    if(ch[i][l] == '?') {
                        if(c) ch[i][l] = c;
                        else {
                            for(int p = l+1; p <= C; p++)
                                if(ch[i][p] != '?') {c = ch[i][p]; break;}
                            ch[i][l] = c;
                        }
                    } else {
                        c = ch[i][l];
                    }
            }
        }
        for(int i = 1; i <= R; i++) {
            for(int j = 1; j <= C; j++)
                printf("%c", ch[i][j]);
            printf("\n");
        }
    }
}
