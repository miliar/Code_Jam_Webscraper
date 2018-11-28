#include<stdio.h>
#include<string.h>
char s[1050];
void tsf(int i,int x){
    while(x--){
        if(s[i]=='-')s[i++]='+';
        else s[i++]='-';
    }
}
int pan(int x){
    int z=0;
    int n=strlen(s);
    for(int i=0;i<=n-x;i++){
        if(s[i]=='-') {tsf(i,x);z++;}
    }
    for(int i=0;i<n;i++){
        if(s[i]=='-') return -1;
    }
    return z;
}
int main(){
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int t;scanf("%d",&t);
    for(int T=1;T<=t;T++){
        int x;
        scanf("%s %d",s,&x);
       // printf("-----------%s\n",s);
        x=pan(x);
        if(x==-1) printf("Case #%d: IMPOSSIBLE\n",T);
        else printf("Case #%d: %d\n",T,x);
    }
    return 0;
}
