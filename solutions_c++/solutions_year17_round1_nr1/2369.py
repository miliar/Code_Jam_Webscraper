#include <bits/stdc++.h>
using namespace std;

#define F0(i,n) for(int i=0;i<n;i++)

void solve(){
    int R,C;
    scanf("%d %d\n",&R,&C);
    char M[R][C+1];
    int empty = 0;
    F0(i,R)scanf("%s\n",M[i]);
    F0(i,R){
        int j=0;
        for(;M[i][j]=='?';j++){}
        if(M[i][j] == '\0'){ // it is an empty row
            empty++;
        }else{
            int k = 0;
            while(M[i][j] != '\0') {
                for (; k <= j; k++)M[i][k] = M[i][j];
                for (; k < C && M[i][k] == '?'; k++)M[i][k] = M[i][j];
                j++;
                for (; M[i][j] == '?'; j++) {}
            }
            for(;empty>0;empty--) { // first non-empty row
                F0(k,C)M[i-empty][k] = M[i][k];
            }
        }
    }
    int last = R-empty-1;
    for(;empty>0;empty--) { // first non-empty row
        F0(k,C)M[R-empty][k] = M[last][k];
    }
    F0(i,R){F0(j,C)printf("%c",M[i][j]);printf("\n");}
}

int main() {
    int T;
    scanf("%d\n",&T);
    F0(i,T){
        printf("Case #%d:\n",i+1);
        solve();
    }
}