#include <cstdio>
#include <algorithm>

using namespace std;

char sir[30][30];

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n;i++) scanf("\n%s",sir[i]+1);
        for(int j=1;j<=m;j++)
        {
            int last=0;
            for(int i=1;i<=n;i++)
                if(sir[i][j]!='?')
                {
                    for(int k=last+1;k<=i;k++) sir[k][j]=sir[i][j];
                    last=i;
                }
            if(last>0)
                for(int k=last+1;k<=n;k++) sir[k][j]=sir[last][j];
        }
        for(int i=1;i<=n;i++)
        {
            int last=0;
            for(int j=1;j<=m;j++)
                if(sir[i][j]!='?')
                {
                    for(int k=last+1;k<=j;k++) sir[i][k]=sir[i][j];
                    last=j;
                }
            for(int k=last+1;k<=m;k++) sir[i][k]=sir[i][last];
        }
        printf("Case #%d:\n",t);
        for(int i=1;i<=n;i++)
            printf("%s\n",sir[i]+1);
    }
    return 0;
}
