#include<stdio.h>
int store[20];
int ans[20];
int ok;
void get(int now,int flag,int last)
{
    if(now<0)
    {
        ok=1;
        return;
    }
    if(ok)return;
    int st;
    if(!flag)st=store[now];
    else st=9;
    for(int i=st;i>=0;i--)
    {
        if(i<last)return;
        ans[now]=i;
        if(i==st)get(now-1,flag,i);
        else get(now-1,1,i);
        if(ok)return;
    }
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b-b.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cases=1;cases<=t;cases++)
    {
        long long n;
        scanf("%lld",&n);
        int tot=0;
        while(n)
        {
            store[tot]=n%10;
            n=n/10;
            tot++;
        }
        ok=0;
        get(tot-1,0,0);
        printf("Case #%d: ",cases);
        int f=0;
        for(int i=tot-1;i>=0;i--)
        {
            if(!f&&!ans[i])continue;
            f=1;
            printf("%d",ans[i]);
        }
        printf("\n");
    }
    return 0;
}
