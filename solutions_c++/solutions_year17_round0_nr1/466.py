#include<bits/stdc++.h>

char a[1010];
void flip(int x,int y){
    for(int k=x;k<=y;k++){
        if(a[k]=='+') a[k]='-';
        else a[k]='+';
    }
    return;
}
int main(){
    int s,m,T,t=0;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%s%d",a,&m);
        s=strlen(a);
        bool flag=true;
        int cnt=0;
        for(int k=0;k<=s-m;k++){
            if(a[k]=='-') flip(k,k+m-1),cnt++;
        }
        for(int k=0;k<s;k++) if(a[k]=='-') flag=false;
        t++;
        printf("Case #%d: ",t);
        if(flag) printf("%d\n",cnt);
        else puts("IMPOSSIBLE");
    }
}
