#include <iostream>
#include <stdio.h>
using namespace std;

int n,m;
int t;
char grid[111][111];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int test;
    int i,j;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        scanf("%d %d",&n,&m);

        for (i=1;i<=n;i++)
        {
            scanf("%s",grid[i]+1);
        }

        for (i=1;i<=n;i++)
        {
            for (j=2;j<=m;j++)
            {
                if (grid[i][j]=='?')
                {
                    if (grid[i][j-1]!='?')
                    {
                        grid[i][j]=grid[i][j-1];
                    }
                }
            }

            for (j=m-1;j>=1;j--)
            {
                if (grid[i][j]=='?')
                {
                    if (grid[i][j+1]!='?')
                    {
                        grid[i][j]=grid[i][j+1];
                    }
                }
            }
        }

        for (i=2;i<=n;i++)
        {
            for (j=1;j<=m;j++)
            {
                if (grid[i][j]=='?')
                {
                    if (grid[i-1][j]!='?')
                    {
                        grid[i][j]=grid[i-1][j];
                    }
                }
            }
        }

        for (i=n-1;i>=1;i--)
        {
            for (j=1;j<=m;j++)
            {
                if (grid[i][j]=='?')
                {
                    if (grid[i+1][j]!='?')
                    {
                        grid[i][j]=grid[i+1][j];
                    }
                }
            }
        }

        for (i=1;i<=n;i++)
        {
            for (j=1;j<=m;j++)
            {
                if (grid[i][j]=='?')
                {
                    fprintf(stderr,"ERROR\n");
                }
            }
        }

        printf("Case #%d:\n",test);

        for (i=1;i<=n;i++)
        {
            for (j=1;j<=m;j++)
            {
                printf("%c",grid[i][j]);
            }
            printf("\n");
        }
    }
}
