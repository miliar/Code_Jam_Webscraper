#include<cstdio>
#include<cstring>
#include<iostream>
#define N 1000

using namespace std;

int t,n,k;

int is_ok(int x){
    int a,b;

    a=x%10;
    x /=10;

    while(x){
        b=x%10;
        if(b>a) return 0;
        x/=10;
        a=b;
    }

    return 1;
}

int main(void){
    int i,j,x,y,dap;

    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);

    scanf("%d",&t);

    for(i=1;i<=t;i++){
        scanf("%d",&n);
        for(j=n;j>=1;j--){
            if(is_ok(j)==1) break;
        }
        printf("Case #%d: %d\n",i,j);
    }


    return 0;
}
