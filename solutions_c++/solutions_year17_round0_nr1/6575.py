#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<string>
using namespace std;
typedef long long ll;

char str[1010];
int vis[1010];
int f[1010];
int solve(int n,int k)
{
    memset(f,0,sizeof(f));
    int res=0;
    int sum=0;
    for(int i=0;i+k<=n;i++)
    {
        if((vis[i]+sum)%2)
        {
            res++;
            f[i]=1;
        }
        sum+=f[i];
        if(i-k+1>=0)
            sum-=f[i-k+1];
    }
    for(int i=n-k+1;i<n;i++)
    {
        if((vis[i]+sum)%2)
        {
            return -1;
        }
        if(i-k+1>=0)
            sum-=f[i-k+1];
    }
    return res;
}

int main()
{
//    freopen("A-large.in-1.txt","r",stdin);
//    freopen("A-large.out-1.txt", "w", stdout);
    int t,k;
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++)
    {
        scanf("%s",str);
        int n=strlen(str);
        for(int i=0;i<n;i++)
            if(str[i]=='-')
                vis[i]=1;
            else
                vis[i]=0;
        scanf("%d",&k);
        int m=solve(n,k);
        if(m==-1)
            printf("Case #%d: IMPOSSIBLE\n",ca);
        else
        printf("Case #%d: %d\n",ca,m);
    }
    return 0;
}
