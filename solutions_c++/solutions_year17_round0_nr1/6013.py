#include<cstdio>
#include<string.h>
#include<algorithm>
using namespace std;

main()
{
    freopen("A-large(1).txt","r",stdin);
    freopen("opf.txt","w",stdout);
    char s[1005];
    int t,ct;
    int n,m,k;
    int i,j;
    int x,y;
    scanf("%d",&t);
    for(ct=1;ct<=t;ct++)
    {
        //printf("%d\n",ct);
        scanf("%s",s);
        scanf("%d",&k);
        n=strlen(s);
        x=0;
        for(i=0;i<=n-k;i++)
        {
            if(s[i]=='-')
            {
                x++;
                for(j=0;j<k;j++)
                {
                    if(s[i+j]=='-')
                    {
                        s[i+j]='+';
                    }
                    else
                    {
                        s[i+j]='-';
                    }
                }
            }
        }
        y=0;
        //printf("%s\n",s);
        for(i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
                y=1;
            }
        }
        if(y==0)
        {
            printf("Case #%d: %d\n",ct,x);
        }
        else
        {
            printf("Case #%d: IMPOSSIBLE\n",ct);
        }
    }
}
