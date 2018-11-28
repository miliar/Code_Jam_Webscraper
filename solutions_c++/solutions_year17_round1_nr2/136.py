#include <cstdio>
#include <algorithm>

using namespace std;

int req[105];
int amt[105][105];
int pos[105];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int itr=1; itr<=tc; itr++)
    {
        int n,p;
        scanf("%d%d",&n,&p);
        for (int i=1; i<=n; i++)
            scanf("%d",&req[i]);
        for (int i=1; i<=n; i++)
            for (int j=1; j<=p; j++)
                scanf("%d",&amt[i][j]);
        for (int i=1; i<=n; i++)
            sort(amt[i]+1,amt[i]+1+p);
        for (int i=1; i<=n; i++)
            pos[i]=1;
        int ended=0;
        int ret=0;
        while (!ended)
        {
            int top=10000000;
            int bot=1;
            for (int i=1; i<=n; i++)
            {
                if (pos[i]>p)
                {
                    ended=1;
                    break;
                }
                int mx=((amt[i][pos[i]]*10)/(req[i]*9));
                int mn=((amt[i][pos[i]]*10+req[i]*11-1)/(req[i]*11));
                bot=max(bot,mn);
                top=min(top,mx);
            }
            if (ended)
                break;
            if (bot<=top)
            {
                ret++;
                for (int i=1; i<=n; i++)
                    pos[i]++;
            }
            else
            {
                for (int i=1; i<=n; i++)
                {
                    int mx=((amt[i][pos[i]]*10)/(req[i]*9));
                    int mn=((amt[i][pos[i]]*10+req[i]*11-1)/(req[i]*11));
                    if (mx<mn || mx<bot)
                        pos[i]++;
                }
            }
        }
        printf("Case #%d: %d\n",itr,ret);
    }
}
