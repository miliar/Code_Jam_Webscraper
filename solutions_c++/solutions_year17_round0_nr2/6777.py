#include<stdio.h>
#include<string.h>

unsigned long long res;

char s[33];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    int i,j,k,len,flag,co=1,t;
    scanf("%d",&t);
    while(t--)
    {
        res=0;
        scanf("%s",s);
        len=strlen(s);
        for(i=0;i<len;i++)
        {
            flag=0;
            if(s[i]-48>s[i+1]-48 && i+1<len)
            {
                flag=1;
                s[i]=s[i]-1;
                for(j=i+1;j<len;j++)
                    s[j]=57;
            }
            if(flag)
                i=-1;
        }
        for(i=0;i<len;i++)
            res=res*10+(s[i]-48);
        printf("Case #%d: %llu\n",co++,res);
    }
    return 0;
}
