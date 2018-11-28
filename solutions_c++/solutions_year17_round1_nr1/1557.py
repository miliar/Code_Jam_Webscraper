#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int r,c;
char str[30][30];

int main()
{
    int T;
    int ca = 1;
    freopen("A-large.in","r",stdin);
    freopen("A-large-out.txt","w",stdout);
    scanf("%d",&T);
    while (T--)
    {
        memset(str,0,sizeof(str));
        scanf("%d%d",&r,&c);
        for (int i = 1 ; i <= r ; i ++)
        {
            scanf("%s",str[i]+1);
            for (int j = 1 ; j <= c ; j ++)
            {
                if (str[i][j]=='?')
                {
                    if (str[i][j-1]!=0&&str[i][j-1]!='?')
                        str[i][j]=str[i][j-1];
                    else if (str[i][j+1]!=0&&str[i][j+1]!='?')
                        str[i][j]=str[i][j+1];
                }
            }
            for (int j = c ; j >= 1 ; --j)
            {
                if (str[i][j]=='?')
                {
                    if (str[i][j-1]!=0&&str[i][j-1]!='?')
                        str[i][j]=str[i][j-1];
                    else if (str[i][j+1]!=0&&str[i][j+1]!='?')
                        str[i][j]=str[i][j+1];
                }
            }
        }
        for (int i =1 ; i <= r ; i ++)
        {
            for (int j = 1 ; j <= c ; j ++)
            {
                if (str[i][j]=='?')
                {
                    if (str[i-1][j]!=0&&str[i-1][j]!='?')
                        str[i][j]=str[i-1][j];
                    else if (str[i+1][j]!=0&&str[i+1][j]!='?')
                        str[i][j]=str[i+1][j];
                }
            }
        }
        for (int i =r ; i >= 1 ; --i)
        {
            for (int j = 1 ; j <= c ; j ++)
            {
                if (str[i][j]=='?')
                {
                    if (str[i-1][j]!=0&&str[i-1][j]!='?')
                        str[i][j]=str[i-1][j];
                    else if (str[i+1][j]!=0&&str[i+1][j]!='?')
                        str[i][j]=str[i+1][j];
                }
            }
        }
        printf("Case #%d: \n",ca++);
        for (int i =1 ; i <= r ; i ++)
            printf("%s\n",str[i]+1);

    }
}
