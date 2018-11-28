#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int T,n,i,j,k,m,count1,c;
    string ar;
    scanf("%d",&T);
    for(j=1;j<=T;j++)
    {
        c=1;
        count1=0;
        cin>>ar;
        cin>>k;

        n=ar.length();
        for(i=0;i<=n-k;i++)
        {
            if(ar[i]=='+')
                continue;
            else
            {   count1++;
                for(m=i;m<i+k;m++)
                {
                    if(ar[m]=='-')
                        ar[m]='+';
                    else
                        ar[m]='-';
                }
            }
        }

        for(;i<n;i++)
        {
            if(ar[i]=='-')
                {
                    printf("Case #%d: IMPOSSIBLE\n",j);
                    c=0;
                    break;

                }
        }
        if(c==1)
            printf("Case #%d: %d\n",j,count1);


}
}
