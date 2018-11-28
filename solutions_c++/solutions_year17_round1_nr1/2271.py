#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <queue>
#define MAXN 1010

using namespace std;

int n,m;
char G[101][101];


int main()
{
    int T,cas = 1;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&n,&m);
        for(int i = 0;i < n;++ i)
            scanf("%s",G[i]);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                if(G[i][j]=='?' && i>0)
                    G[i][j]=G[i-1][j];
            }
        
        
        for(int i=n-1;i>=0;i--)
            for(int j=0;j<m;j++)
            {
                if(G[i][j]=='?' && i<n-1)
                    G[i][j]=G[i+1][j];
            }
        
        for(int j=0;j<m;j++)
            for(int i=0;i<n;i++)
            {
                if(G[i][j]=='?' && j>0)
                    G[i][j]=G[i][j-1];
            }
        
        for(int j=m-1;j>=0;j--)
            for(int i=0;i<n;i++)
            {
                if(G[i][j]=='?' && j<m-1)
                    G[i][j]=G[i][j+1];
            }
        printf("Case #%d:\n",cas);
        cas++;
        for(int i = 0;i < n;++ i)
            printf("%s\n",G[i]);
    }
    return 0;
}
