#include<stdio.h>
#include<string.h>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output-large.txt","w",stdout);
    long long i,j,a,b,c,n,m,t,caseno=0;
    char num[30],ch;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld",&n);
        printf("Case #%lld: ",++caseno);
        if(n<10)
        {
            printf("%lld\n",n);
            continue;
        }
        sprintf(num,"%lld",n);
        a=strlen(num);
        for(i=a-1;i>0;i--)
        {
            if(num[i]<num[i-1])
            {
                num[i]='a';
                num[i-1]=num[i-1]-1;
            }
        }
        for(i=0;i<a;i++)
        {
            if(num[i]=='a')
                break;
        }
        for(;i<a;i++)
            num[i]='9';
        for(i=0;i<a;i++)
        {
            if(num[i]!='0')
                break;
        }
        for(;i<a;i++)
            printf("%c",num[i]);
        printf("\n");
    }
    return 0;
}
