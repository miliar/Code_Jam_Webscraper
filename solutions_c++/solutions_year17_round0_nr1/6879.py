#include<cstdio>
#include<cstring>
#include<iostream>
#define N 1000

using namespace std;

int t,n,k;
char s[N+10];

int main(void){
    int i,j,x,y,dap;

    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);


    scanf("%d",&t);

    for(i=1;i<=t;i++){
        scanf("%s %d",s,&k);

        x=strlen(s);
        dap=0;

        for(j=0;j<=x-k;j++){
            if(s[j]=='-'){
                dap++;
                for(y=j;y<j+k;y++) s[y]=s[y]=='-'?'+':'-';
            }
        }
        for(;j<x;j++){
            if(s[j]=='-'){
                dap=-1;
                break;
            }
        }
        if(dap<0){
            printf("Case #%d: IMPOSSIBLE\n",i);
        }else{
            printf("Case #%d: %d\n",i,dap);
        }

    }


    return 0;
}
