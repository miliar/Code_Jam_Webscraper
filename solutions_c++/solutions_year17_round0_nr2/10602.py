#include <bits/stdc++.h>
using namespace std;
int isTidy(int input)
{
    int lastSeen = 10;
    int current;

    while (input > 0) 
    {
        current = input % 10;
        if (lastSeen < current)
            return 0;
        lastSeen = current;
        input /= 10;
    }
    return 1;
}
int main()
{
    int t,i,j,op;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        int n;
        scanf("%d",&n);
        if(n/10==0)
            printf("Case #%d: %d\n",j,n);
        else
        {
            for(i=n;i>=1;i--)
            {
                if(isTidy(i)==1)
                {
                    printf("Case #%d: %d\n",j,i);
                    break;
                }
            }
        }
    }
}