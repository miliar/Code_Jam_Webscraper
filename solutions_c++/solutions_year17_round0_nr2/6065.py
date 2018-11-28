#include<bits/stdc++.h>

int k;
char s[1003];
int a[1003];

void sol(){
    int i, j, len = strlen(s);
    for(i=0;i<len;i++){
        a[i] = s[i] - '0';
        if(!a[i]) break;
    }
    for(i=len-1;i>0;i--){
        if(a[i-1] > a[i]){
            a[i-1]--;
            j = i;
        }
    }for(i=j;i<len;i++) a[i] = 9;
    i = 0;
    if(!a[0]) ++i;
    for(;i<len;i++) printf("%d",a[i]);
    puts("");
}

int main(){
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%s",s);
        printf("Case #%d: ",t);
        sol();
    }

    return 0;
}
/*
 3
---+-++- 3
+++++ 4
-+-+- 4
*/
