#include <stdio.h>
bool pancake[1001];
int main()
{
    freopen("output.txt","w",stdout);
    freopen("A-large.in","r",stdin);
    int T,i,len,K,current,co;
    bool f;
    char s[1001];
    scanf("%d",&T);
    for(int t=1;t<=T;++t)
    {
        co=0;
        f=true;
        scanf("%s",s);
        for(i=0;s[i]!='\0';++i)
        {
            switch(s[i])
            {
                case '+' : pancake[i]=true;break;
                case '-' : pancake[i]=false;
            }
        }
        len=i-1;
        scanf("%d",&K);
        for(current=0;current<=len-K+1;++current)
        {
            if(!pancake[current])
            {
                co++;
                for(int j=current,k=1;k<=K&&j<=len;++j,++k)
                {
                    pancake[j]=!pancake[j];
                }
            }
        }
        printf("Case #%d: ",t);
        for(int i=0;i<=len;++i)
        {
            if(!pancake[i])
            {
                printf("IMPOSSIBLE\n");
                f=false;
                break;
            }
        }
        if(f)printf("%d\n",co);
    }
}
