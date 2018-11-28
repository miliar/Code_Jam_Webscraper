#include<stdio.h>
#include<string.h>
char s[1005];
char ss[1055];
int get()
{
    scanf("%s",ss);
    printf("ss:%s",ss);
    int num=0;
    for(int i=0;ss[i];i++)
    {
        num=num*10+ss[i]-'0';
    }
    return num;
}
int main()
{
    //freopen("A-small-attempt2","r",stdin);
    freopen("a-s.out","w",stdout);
    int t;
    scanf("%s",ss);
    t=0;
    int f;
    for(f=0;ss[f]>='0'&&ss[f]<='9';f++)
    {
        t=t*10+ss[f]-'0';
    }
    memset(s,0,sizeof(s));
    for(int i=0;ss[f];i++)
    {
        s[i]=ss[f];
        f++;
    }
    for(int cases=1;cases<=t;cases++)
    {
        int k=0;
        scanf("%s",ss);
        for(f=0;ss[f]>='0'&&ss[f]<='9';f++)
    {
        k=k*10+ss[f]-'0';
    }
        //printf("%s %d",s,k);
        int len=strlen(s);
        int ans=0;
        for(int i=0;i<=len-k;i++)
        {
            if(s[i]=='-')
            {
                ans++;
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
            }
        }
        printf("Case #%d: ",cases);
        for(int i=0;i<len;i++)
        {
            if(s[i]=='-')
            {
                ans=-1;
                break;
            }
        }
        if(ans==-1)printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
        memset(s,0,sizeof(s));
    for(int i=0;ss[f];i++)
    {
        s[i]=ss[f];
        f++;
    }
    }
    return 0;
}
