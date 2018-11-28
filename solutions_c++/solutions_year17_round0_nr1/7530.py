#include <bits/stdc++.h>
using namespace std;

int main()
{   long long t,k,c,l,i,ii,j;
    scanf("%lld",&t);
    for(ii=1;ii<=t;ii++)
    {   char a[1007];
        scanf("%s %lld",a,&k);
        c=0;
        bool b=0;
        l=strlen(a);
        for(i=0;i<l;i++)
        {   if(a[i]=='-')
            {   c++;
                if((i+k)>=(l+1))
                {   b=1;
                    break;
                }
                for(j=i;j<(i+k);j++)
                {   if(a[j]=='-')
                        a[j]='+';
                    else
                        a[j]='-';
                }
            }
        }
        if(b)
            printf("Case #%lld: IMPOSSIBLE\n",ii);
        else
            printf("Case #%lld: %lld\n",ii,c);
    }
    return 0;
}
