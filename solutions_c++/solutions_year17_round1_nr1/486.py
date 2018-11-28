#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
int TC, R, C;
char str[36][36];
char ans[36][36];
bool isBlank[36];
void spread(char a[], char b[]){
    int prime = 0;
    while(b[prime] == '?') ++prime;
    for(int i = 0; i < prime; ++i) a[i] = b[prime];
    for(int i = prime; i < C; ++i){
        if(b[i] == '?') a[i] = a[i-1];
        else a[i] = b[i];
    }
}
int main(){
    scanf("%d", &TC);
    for(int tc = 1; tc <= TC; ++tc){
        scanf("%d %d", &R, &C);
        for(int i = 0; i < R; ++i){
            scanf("%s", str[i]);
            isBlank[i] = true;
            for(int j = 0; j < C; ++j) if(str[i][j] != '?') isBlank[i] = false;
            ans[i][C] = 0;
        }
        int prime = 0;
        while(isBlank[prime]) ++prime;
        spread(ans[prime], str[prime]);
        for(int i = 0; i < prime; ++i)
            for(int j = 0; j < C; ++j) 
                ans[i][j] = ans[prime][j];
        for(int i = prime+1; i < R; ++i){
            if(isBlank[i])
                for(int j = 0; j < C; ++j) ans[i][j] = ans[i-1][j];
            else spread(ans[i], str[i]);
        }
        printf("Case #%d:\n", tc);
        for(int i = 0; i < R; ++i) printf("%s\n", ans[i]);
    }
}
        
        
