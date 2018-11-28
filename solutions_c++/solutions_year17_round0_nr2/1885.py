#include<stdio.h>

typedef unsigned long long LL;
LL d[25],s[25];

LL f(LL v, int x, int sx)
{
    if(x==0)return 0;
    LL i,t;
    for(i=9;i>=sx;i--){
        if(s[x]*i>v)continue;
        t=f(v-d[x]*i,x-1,i);
        return t+d[x]*i;
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    LL n,x;
    int len,i,T,lt;
    scanf("%d", &T);
    for(lt=1;lt<=T;lt++){
        scanf("%llu", &n);
        x=n;
        len=0;
        while(x){
            x/=10;
            len++;
        }
        d[1]=s[1]=1;
        for(i=2;i<=len;i++){
            d[i]=d[i-1]*10;
            s[i]=s[i-1]+d[i];
        }
        printf("Case #%d: %llu\n", lt, f(n,len,0));
    }
    return 0;
}
