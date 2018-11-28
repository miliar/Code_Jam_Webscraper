#include <cstdio>
#include <algorithm>

using namespace std;

char base[100005];
int mark[100005];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int itr=1; itr<=tc; itr++)
    {
        scanf("%s",base+1);
        int k;
        scanf("%d",&k);
        int n=1;
        while (base[n+1])
        {
            n++;
        }
        for (int i=1; i<=n; i++)
            mark[i]=0;
        int cflip=0;
        int failed=0;
        int total=0;
        for (int i=1; i<=n; i++)
        {
            int cur=base[i]=='+'?1:0;
            cflip^=mark[i];
            cur^=cflip;
            if (cur==0)
            {
                total++;
                if (i+k-1>n)
                {
                    failed=1;
                }
                cflip^=1;
                mark[i+k]^=1;
            }
        }
        printf("Case #%d: ",itr);
        if (failed)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",total);
    }
}
