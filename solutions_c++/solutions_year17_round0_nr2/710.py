#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
using namespace std;
typedef long long ll;

char str[105];

bool isinc(){
    for(int i=1;str[i];i++){
        if(!isdigit(str[i]))return false;
        if(str[i]<str[i-1])return false;
    }
    return true;
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,Case=1;
    
    for(scanf("%d",&T);Case<=T;Case++){
        scanf("%s",str);
        int len=strlen(str);
        for(int i=len-1;i>=0;i--){
            if(isinc())break;
            
            str[i-1]--;
            str[i]='9';
        }
        printf("Case #%d: ",Case);
        ll ans=0;
        sscanf(str,"%I64d",&ans);
        printf("%I64d\n",ans);
    }
    return 0;
}

