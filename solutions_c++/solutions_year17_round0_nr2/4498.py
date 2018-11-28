#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("D:\B-large.in","r",stdin);
    freopen("D:\B-large.out","w",stdout);
    long long n,t,case1=0;
    char s[100];
    scanf("%lld",&t);
    while(case1++<t)
    {
        int i;
        bool ok=false;
        scanf("%lld",&n);
        if(n==1)
        {
            printf("Case #%lld: 1\n",case1);
            continue;
        }
        sprintf(s,"%lld",n);
        //puts(s);
        int l=strlen(s);
        bool others=false;
        for(int i=0;s[i];i++)
        {
            if(s[i]!='0'&&s[i]!='1')
            {
                others=true;
                break;
            }
        }
        printf("Case #%lld: ",case1);
        if(!others)
        {
            for(i=1;i<=l-1;i++)
                printf("9");
            printf("\n");
        }
        else{
        for(i=0;i<l;i++)
        {
            if(ok) s[i]='9';
            if(s[i]>s[i+1]&&!ok&&i+1<l)
            {
                int lpos=i,rpos,pos=i;
                ok=true;
                //printf("Pos %d\n",pos);
                while(s[pos]==s[pos-1]&&pos-1>=0)
                {
                    pos--;
                }
                rpos=pos;
                //printf("%d %d\n",lpos,rpos);
                if(rpos==0)
                {
                    s[0]-=1;
                    for(int f=1;f<l;f++)
                    {
                        s[f]='9';
                    }
                    break;
                }
                else {s[rpos]-=1;for(int f=rpos+1;f<=lpos;f++) s[f]='9';}
                //printf("Lpos %d \n",pos);
            }
        }
        for(i=0;i<l;i++)
        {
            if(s[i]!='0')
                break;
        }
        for(int j=i;j<l;j++)
        {
            printf("%c",s[j]);
        }
        printf("\n");}
    }
    return 0;
}
