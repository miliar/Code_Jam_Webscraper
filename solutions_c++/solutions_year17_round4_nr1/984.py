
/*
Contest: Google Code Jam 2017 [Round 2]
*/


#include<stdio.h>
#include<algorithm>
using namespace std;

int n,p;
int bank[5];

int easyCase()
{
    int ret = bank[0];
    ret+= (bank[1]/2);
    ret+= (bank[1]%2);
    return ret;
}

int dp3[111][111];
int dp3s[111][111];

void dynamicPreparation()
{
    for(int i=0;i<=100;i++) for(int j=0;j<=100;j++) dp3[i][j] = 0;
    for(int i=0;i<=100;i++) for(int j=0;j<=100;j++)
    {
        if(i-3>=0) dp3[i][j] = max(dp3[i][j],dp3[i-3][j-0]+1);
        if(j-3>=0) dp3[i][j] = max(dp3[i][j],dp3[i-0][j-3]+1);
        if(i>0&&j>0) dp3[i][j] = max(dp3[i][j],dp3[i-1][j-1]+1);

        dp3s[i][j] = dp3[i][j];

        if(i>0) dp3s[i][j] = max(dp3s[i][j],dp3[i-1][j]+1);
        if(j>0) dp3s[i][j] = max(dp3s[i][j],dp3[i][j-1]+1);
    }
}

int dp4[111][111][111];
int dp4s[111][111][111];

void dynamic4Preparation()
{
    for(int i=0;i<=100;i++) for(int j=0;j<=100;j++) for(int k=0;k<=100;k++)
    {
        dp4[i][j][k] = 0;
        if(i-4>=0) dp4[i][j][k] = max(dp4[i][j][k],dp4[i-4][j][k]+1);
        if(k-4>=0) dp4[i][j][k] = max(dp4[i][j][k],dp4[i][j][k-4]+1);
        if(j-2>=0) dp4[i][j][k] = max(dp4[i][j][k],dp4[i][j-2][k]+1);
        if(i-1>=0&&k-1>=0) dp4[i][j][k] = max(dp4[i][j][k],dp4[i-1][j][k-1]+1);
        if(i-2>=0&&j-1>=0) dp4[i][j][k] = max(dp4[i][j][k],dp4[i-2][j-1][k]+1);
        if(j-1>=0&&k-2>=0) dp4[i][j][k] = max(dp4[i][j][k],dp4[i][j-1][k-2]+1);

        dp4s[i][j][k] = dp4[i][j][k];

        if(i>0) dp4s[i][j][k] = max(dp4s[i][j][k],dp4[i-1][j][k]+1);
        if(j>0) dp4s[i][j][k] = max(dp4s[i][j][k],dp4[i][j-1][k]+1);
        if(k>0) dp4s[i][j][k] = max(dp4s[i][j][k],dp4[i][j][k-1]+1);
    }
}

int solve()
{
    scanf("%d%d",&n,&p);
    for(int i=0;i<p;i++) bank[i] = 0;
    for(int i=0;i<n;i++)
    {
        int tmp; scanf("%d",&tmp);
        bank[tmp%p]++;
    }
    //Get Answer
    if(p==2) return easyCase();
    if(p==3) return dp3s[bank[1]][bank[2]]+bank[0];
    return dp4s[bank[1]][bank[2]][bank[3]] + bank[0];
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-Large.txt","w",stdout);
    dynamicPreparation();
    dynamic4Preparation();
    int tc; scanf("%d",&tc);
    for(int t=1;t<=tc;t++)
    {
        printf("Case #%d: ",t);
        int ans = solve();
        printf("%d\n",ans);
    }
    return 0;
}

