#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#define MAXN 30
using namespace std;
int T,R,C;
char S[MAXN][MAXN];
int Front(int i,int j){
    if(j-1<0) return -1;
    if(S[i][j-1]!='?')
        return j-1;
    else
        return Front(i,j-1);
}
int Back(int i,int j){
    if(j+1>=C) return -1;
    if(S[i][j+1]!='?')
        return j+1;
    else return Back(i,j+1);
}
void solve(){
    for(int i=0;i<R;++i){
        for(int j=0;j<C;++j){
            if(S[i][j]=='?'){
                int x = Front(i,j);
                if(x!=-1){
                    for(int k=x;k<=j;++k){
                        S[i][k]=S[i][x];
                    }
                }
                else{
                    int y = Back(i,j);
                    if(y!=-1){
                        for(int k=j;k<=y;++k){
                            S[i][k] = S[i][y];
                        }
                    }
                }
            }
        }
    }
}
int Up(int i, int j){
    if(i-1<0) return -1;
    if(S[i-1][j]!='?')
        return i-1;
    else return Up(i-1,j);
}
int Down(int i,int j){
    if(i+1>=R) return -1;
    if(S[i+1][j]!='?')
        return i+1;
    else return Down(i+1,j);
}
void solve2(){
    for(int i=0;i<C;++i){
        for(int j=0;j<R;++j){
            if(S[j][i]=='?'){
                int x = Up(j,i);
                if(x!=-1){
                    for(int k=x;k<=j;++k){
                        S[k][i]=S[x][i];
                    }
                }
                else{
                    int y = Down(j,i);
                    if(y!=-1){
                        for(int k=j;k<=y;++k){
                            S[k][i] = S[y][i];
                        }
                    }
                }
            }
        }
    }
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for(int c=1;c<=T;++c){
        scanf("%d%d",&R,&C);
        memset(S,0,sizeof(S));
        for(int i=0;i<R;++i)
            scanf("%s",S[i]);
        solve();
        solve2();
        printf("Case #%d:\n",c);
        for(int i=0;i<R;++i)
            printf("%s\n",S[i]);
    }
    return 0;
}
