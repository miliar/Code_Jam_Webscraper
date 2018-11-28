#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <vector>
#include <string>
#include <map>

using namespace std;

typedef long long ll;

char board[33][33];


int main()
{
    freopen("/Users/qianjay/Documents/apac/in", "r", stdin);
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        printf("Case #%d: \n",test);
        int r,c;
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++)
            scanf("%s",board[i]);
        for(int i=0;i<r;i++)
        {
            int pre=-1;
            for(int j=0;j<c;j++)
            {
                if(board[i][j]!='?')
                {
                    for(int k=pre+1;k<=j;k++)
                        board[i][k]=board[i][j];
                    pre=j;
                }
                if(j==c-1&&pre!=-1)
                {
                    for(int k=pre+1;k<c;k++)
                        board[i][k]=board[i][pre];
                }
            }
        }
        int flag;
        int pre=-1;
        for(int i=0;i<r;i++)
        {
            flag=0;
            for(int j=0;j<c;j++)
                if(board[i][j]!='?')
                    flag=1;
            
            if(flag)
            {
                for(int j=pre+1;j<i;j++)
                    memcpy(board[j],board[i],sizeof(board[j]));
                pre=i;
            }
            if(i==r-1&&!flag)
            {
                for(int j=pre+1;j<=i;j++)
                    memcpy(board[j],board[pre],sizeof(board[j]));
            }
        }
        for(int i=0;i<r;i++)
            printf("%s\n",board[i]);
    }
    return 0;
}
