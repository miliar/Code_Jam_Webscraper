#include <cstdio>
#include <algorithm>

using namespace std;

char base[105][105];


int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int itr=1; itr<=tc; itr++)
    {
        int r,c;
        scanf("%d%d",&r,&c);
        for (int i=1; i<=r; i++)
            scanf("%s",base[i]+1);
        for (int i=1; i<=r; i++)
        {
            int emp=1;
            for (int j=1; j<=c; j++)
                if (base[i][j]!='?')
                    emp=0;
            if (emp)
            {
                if (i>1)
                {
                    for (int j=1; j<=c; j++)
                        base[i][j]=base[i-1][j];
                }
            }
            else
            {
                char cur;
                for (int j=c; j>=1; j--)
                    if (base[i][j]!='?')
                        cur=base[i][j];
                for (int j=1; j<=c; j++)
                {
                    if (base[i][j]=='?')
                        base[i][j]=cur;
                    else
                        cur=base[i][j];
                }
            }
        }
        for (int i=r; i>=1; i--)
        {
            int emp=1;
            for (int j=1; j<=c; j++)
                if (base[i][j]!='?')
                    emp=0;
            if (emp)
            {
                if (i<r)
                {
                    for (int j=1; j<=c; j++)
                        base[i][j]=base[i+1][j];
                }
            }
            else
            {
                char cur;
                for (int j=c; j>=1; j--)
                    if (base[i][j]!='?')
                        cur=base[i][j];
                for (int j=1; j<=c; j++)
                {
                    if (base[i][j]=='?')
                        base[i][j]=cur;
                    else
                        cur=base[i][j];
                }
            }
        }
        printf("Case #%d:\n",itr);
        for (int i=1; i<=r; i++)
            printf("%s\n",base[i]+1);
    }

}
