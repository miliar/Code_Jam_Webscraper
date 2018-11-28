#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
using namespace std;


const int MAXN=25+5;
const int INF=0x3f3f3f3f;
#define ll long long
char s[MAXN][MAXN];
int r,c;

void solve2(int x){
    char tmp;
    int i;
    bool flag=false;
    for(i=0;i<c;i++){
        if(s[x][i]!='?'){
            flag=true;
            tmp=s[x][i];
            break;
        }
    }
    if(!flag){
        for(int j=0;j<c;j++){
            s[x][j]=s[x-1][j];
        }
    }else{
        for(int j=0;j<i;j++){
            s[x][j]=tmp;
        }
    }
    i+=1;
    while(i<c){
        if(s[x][i]=='?') s[x][i]=tmp;
        else tmp=s[x][i];
        i++;
    }
}


void solve1(){
    int i,j;
    char tmp;
    bool flag=false;
    for(i=0;i<r;i++){
        for(j=0;j<c;j++){
            if(s[i][j]!='?'){
                tmp=s[i][j];
                flag=true;
                break;
            }
        }
        if(flag) break;
    }
    for(int l=0;l<j;l++){
        s[i][l]=s[i][j];
    }
    j+=1;
    //printf("debug:i:%d j:%d\n",i,j);
    while(j<c){
        //printf("i:%d j:%d\n",i,j);
        if(s[i][j]=='?') s[i][j]=tmp;
        else tmp=s[i][j];
        j++;
    }
    for(int l=0;l<i;l++){
        for(int k=0;k<c;k++){
            s[l][k]=s[i][k];
        }
    }
    //printf("ok\n");
    for(int l=i+1;l<r;l++){
        solve2(l);
    }
}



int main()
{

    //freopen("in.txt","r",stdin);
    int T;
    int time=0;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++){
            scanf("%s",s[i]);
        }
        solve1();
        printf("Case #%d:\n",++time);
        for(int i=0;i<r;i++){
            printf("%s\n",s[i]);
        }
    }
    return 0;
}
