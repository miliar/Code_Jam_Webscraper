#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int t;
int n,m,c;
int ctrplaces[1011];
int ctrclients[1011];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int test;
    int b,p;
    int i;
    int promotions=0;
    int sum;
    int rides=0,needrides;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        memset(ctrplaces,0,sizeof(ctrplaces));
        memset(ctrclients,0,sizeof(ctrclients));

        scanf("%d %d %d",&n,&c,&m);

        for (i=1;i<=m;i++)
        {
            scanf("%d %d",&p,&b);

            ctrplaces[p]++;
            ctrclients[b]++;
        }

        rides=0;
        for (i=1;i<=c;i++)
        {
            if (ctrclients[i]>rides)
            rides=ctrclients[i];
        }

        sum=0;
        for (i=1;i<=n;i++)
        {
            sum+=ctrplaces[i];
            needrides=sum/i;
            if (sum%i!=0)
            needrides++;

            if (needrides>rides)
            rides=needrides;
        }

        promotions=0;
        for (i=1;i<=n;i++)
        {
            if (ctrplaces[i]>rides)
            promotions+=ctrplaces[i]-rides;
        }

        printf("Case #%d: %d %d\n",test,rides,promotions);
    }

    return 0;
}
