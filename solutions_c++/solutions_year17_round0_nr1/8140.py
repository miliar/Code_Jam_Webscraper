#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("prog1.out","w",stdout);
    int t,i,l,k,c,f,j,m;
    string s;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        cin>>s;
        scanf("%d",&k);
        l=s.length();
        c=0;
        f=1;
        for(j=0;j<l;j++)
        {
            if(s[j]=='-')
            {
                for(m=0;m<k;m++)
                {
                    if(j+m>=l)
                    {
                        f=0;
                        goto outer;
                    }
                    if(s[j+m]=='-')
                        s[j+m]='+';
                    else
                        s[j+m]='-';
                }
                c++;
            }

        }
        outer:
        if(f==0)
            printf("Case #%d: IMPOSSIBLE\n",i);
        else
            printf("Case #%d: %d\n",i,c);
    }

    return 0;
}
