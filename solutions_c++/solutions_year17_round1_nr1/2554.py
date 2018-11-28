#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

int t,r,c;
char mapp[30][30];

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    scanf("%d",&t);
    int z=1;
    while(t--)
    {
        scanf("%d %d",&r,&c);
        for(int i=0;i<r;++i)
            scanf("%s",mapp[i]);
        for(int i=0;i<r;++i)
        {
            for(int j=0;j<c;++j)
            {
                if(mapp[i][j]=='?')
                {
                    if(j!=0)
                    {
                        if(mapp[i][j-1]!='?')
                            mapp[i][j]=mapp[i][j-1];
                    }
                }
            }
        }

        for(int i=0;i<r;++i)
        {
            for(int j=c-1;j>=0;--j)
            {
                if(mapp[i][j]=='?')
                {
                    if(j!=c-1)
                    {
                        if(mapp[i][j+1]!='?')
                            mapp[i][j]=mapp[i][j+1];
                    }
                }
            }
        }

        for(int j=0;j<c;++j)
        {
            for(int i=0;i<r;++i)
            {
                if(mapp[i][j]=='?')
                {
                    if(i!=0)
                    {
                        if(mapp[i-1][j]!='?')
                            mapp[i][j]=mapp[i-1][j];
                    }
                }
            }
        }

        for(int j=0;j<c;++j)
        {
            for(int i=r-1;i>=0;--i)
            {
                if(mapp[i][j]=='?')
                {
                    if(i!=r-1)
                    {
                        if(mapp[i+1][j]!='?')
                            mapp[i][j]=mapp[i+1][j];
                    }
                }
            }
        }
        printf("Case #%d:\n",z++);
        for(int i=0;i<r;++i)
            printf("%s\n",mapp[i]);
    }
}
