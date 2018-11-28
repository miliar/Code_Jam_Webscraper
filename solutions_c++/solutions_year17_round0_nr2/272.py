#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;
typedef long long Int;

int num[21];
int L;
int t;
Int n;

int mynum[21];

bool Okay(int x)
{
    int i;
    Int thenum=0;

    for (i=1;i<=L;i++)
    {
        thenum*=10;

        if (mynum[i]==-1)
        thenum+=x;
        else
        thenum+=mynum[i];
    }

    return (thenum<=n);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int test;
    int i,j;
    bool good;
    Int rem;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        scanf("%lld",&n);
        rem=n;

        L=0;
        while(n>0)
        {
            L++;
            num[L]=n%10;
            n/=10;
        }

        n=rem;

        reverse(num+1,num+1+L);

        memset(mynum,-1,sizeof(mynum));

        good=false;
        for (i=num[1];i>=1;i--)
        {
            mynum[1]=i;

            if (Okay(i))
            {
                good=true;
                break;
            }
        }

        printf("Case #%d: ",test);
        if (good)
        {
            printf("%d",mynum[1]);

            for (i=2;i<=L;i++)
            {
                for (j=9;j>=mynum[i-1];j--)
                {
                    mynum[i]=j;

                    if (Okay(j))
                    break;
                }

                printf("%d",mynum[i]);
            }
            printf("\n");
        }
        else
        {
            for (i=1;i<=L-1;i++)
            {
                printf("9");
            }
            printf("\n");
        }
    }

    return 0;
}
