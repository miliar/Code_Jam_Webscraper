#include<bits/stdc++.h>

int k;
char s[1003];
int a[1003];

void sol(){
    int i, j, len = strlen(s);
    for(i=0;i<len;i++){
        if(s[i] == '+') a[i] = 1;
        else a[i] = -1;
    }
    int cnt = 0;
    for(i=0;i<=len-k;i++){
        if(a[i]!=1){
            ++cnt;
            for(j=i;j<i+k;j++) a[j] *= -1;
        }
    }
    for(i;i<len;i++){
        if(a[i] != 1){
            puts("IMPOSSIBLE");
            return;
        }
    }
    printf("%d\n",cnt);
    return;
}

int main(){
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%s %d",s,&k);
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
