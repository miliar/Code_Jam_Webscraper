#include <cstdio>

using namespace std;

char sir[30][30];

int main()
{
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    int t,n,m;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        scanf("%d%d\n",&n,&m);
        for(int i=1;i<=n;i++) gets(sir[i]+1);
        for(int i=1;i<=m;i++)
        {
            int poz=1;
            while(sir[poz][i]=='?' && poz<=n) poz++;
            if(poz==n+1)
            {
                if(i>1)
                {
                    for(int j=1;j<=n;j++)
                        sir[j][i]=sir[j][i-1];
                }
                continue;
            }
            char c=sir[poz][i];
            for(int k=poz-1;k>=1;k--) sir[k][i]=c;
            poz++;
            while(poz<=n)
            {
                while(sir[poz][i]=='?' && poz<=n) {sir[poz][i]=c;poz++;}
                c=sir[poz][i];
                poz++;
            }
        }
        for(int i=1;i<=n;i++)
            for(int j=m;j>=1;j--)
                if(sir[i][j]=='?') sir[i][j]=sir[i][j+1];
        printf("Case #%d:\n",test);
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
                printf("%c",sir[i][j]);
            printf("\n");
        }
    }
    return 0;
}
