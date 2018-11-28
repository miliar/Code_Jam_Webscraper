#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int t;
char seq[100111];
int n,k;

void Flip(int l,int r)
{
    int i;

    for (i=l;i<=r;i++)
    {
        if (seq[i]=='-')
        seq[i]='+';
        else
        seq[i]='-';
    }

    return;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int i;
    int test;
    int ans=0;
    bool okay;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        okay=true;
        ans=0;

        scanf("%s",seq+1);
        n=strlen(seq+1);

        scanf("%d",&k);

        for (i=1;i<=n;i++)
        {
            if (seq[i]=='-')
            {
                if (i+k-1>n)
                {
                    okay=false;
                    break;
                }

                Flip(i,i+k-1);
                ans++;
            }
        }

        printf("Case #%d: ",test);
        if (okay)
        {
            printf("%d\n",ans);
        }
        else
        {
            printf("IMPOSSIBLE\n");
        }
    }

    return 0;
}
