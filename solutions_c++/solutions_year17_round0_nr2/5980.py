#include<cstdio>
#include<string.h>
#include<algorithm>
using namespace std;

main()
{
    char s[2442];
    freopen("B-large.in","r",stdin);
    freopen("tn.txt","w",stdout);
    int t,ct;
    int n,m;
    int i,j;
    int x,y;
    scanf("%d",&t);
    for(ct=1;ct<=t;ct++)
    {
        scanf("%s",s);
        n=strlen(s);
        y=1;
        x=0;
        while(y!=0)
        {
            x=0;
            y=0;
            for(i=0;i<n-1;i++)
            {
                if(s[i]>s[i+1]&&x==0)
                {
                    s[i]--;
                    s[i+1]='9';
                    x=1;
                    y=1;
                }
                else if(s[i]>s[i+1]&&x==1)
                {
                    s[i+1]='9';
                    y=1;
                }
            }
        }
        printf("Case #%d: ",ct);
        i=0;
        if(s[i]=='0')
        {
            i=1;
        }
        for(;i<n;i++)
        {
            printf("%c",s[i]);
        }
        printf("\n");
    }
}

