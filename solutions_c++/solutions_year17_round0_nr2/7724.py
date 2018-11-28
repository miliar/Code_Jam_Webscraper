#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

ll tidynumber(ll a)
{
    int i=0,j,b,c=9;
    char str[30];
    while(a)
    {
        str[i++]=a%10+'0';
        a/=10;
    }
    str[i]=0;

    int strlen=i;
    reverse(str,str+strlen);
    //printf("%s %d\n",str,strlen);
    for(i--;i>=0;i--)
    {
        b=str[i]-'0';
        //printf("%d %c b %d c %d\n",i, str[i],b,c);
        if(b>c)
        {
            c=b-1;
            str[i]--;
            if(str[i]=='0'&&i>0)
            {
                str[i]='9';
            }
            for(j=i+1;j<strlen;j++)
            {
                //printf("J loop %d",j);
                str[j]='9';
            }
        }
        else
            c=b;
    }
    i=0;
    while(str[i]=='0')
    {
        i++;
    }
    j=0;
    for(;i<strlen;i++)
        str[j++]=str[i];
    str[j]=0;
    printf("%s\n",str);
}
/*
ll tidynumber(ll a)
{
    ll d=a;
    int c,b=9;
    bool flag=1;
    while(d&&flag)
    {
        c=d%10;
        if(b>=c)
            b=c;
        else
            flag=0;
        d/=10;
        //printf("%d %d %lld\n",b,c,d);
    }
    //printf("%d %lld\n",flag,a);
    return !flag;
}*/

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b_large_out.txt","w",stdout);
    int C=1,t;
    ll a;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld",&a);
        printf("Case #%d: ",C++);
        tidynumber(a);
    }
    return 0;
}


