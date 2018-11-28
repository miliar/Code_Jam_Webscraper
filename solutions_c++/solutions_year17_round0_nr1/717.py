#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
using namespace std;
typedef long long ll;

char str[1005];
int k;

void flip(int x){
    for(int i=x;i<x+k&&str[i];i++){
        if(str[i]=='+')str[i]='-';
        else if(str[i]=='-')str[i]='+';
    }
}

bool check(){
    for(int i=0;str[i];i++)
        if(str[i]=='-')return false;
    return true;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,Case=1;
    
    for(scanf("%d",&T);Case<=T;Case++){
        scanf("%s%d",str,&k);
        int len=strlen(str),ans=0;
        for(int i=0;i+k<=len;i++){
            if(str[i]=='-'){
                ++ans;
                flip(i);
            }
        }
        printf("Case #%d: ",Case);
        if(!check())puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    return 0;
}

