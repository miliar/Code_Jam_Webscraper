#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long long t,n,i,x=1,l;
    char ch[100004];
    while(scanf("%lld",&t)==1)
    {
        getchar();
        while(t--)
        {
            scanf("%s",ch);
            l=strlen(ch);
            for(;;)
            {
                int flag=0;
                for(i=0;i<l;i++)
                {
                    if(ch[i]>ch[i+1] && flag==0 && ch[i+1]!='\0')
                    {
                        ch[i] = ch[i]-1;
                        flag=1;
                    }
                    else if(flag==1)
                        ch[i] = '9';
                }
                if(flag==0)
                    break;
            }
            int flag=0;
            printf("Case #%lld: ",x++);
            for(i=0;i<l;i++)
            {
                if(ch[i]!='0' && flag==0)
                    flag=1;
                if(flag==1)
                    printf("%c",ch[i]);
            }
            printf("\n");
        }
    }
    return 0;
}
