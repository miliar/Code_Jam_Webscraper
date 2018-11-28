#include<bits/stdc++.h>
using namespace std;
#define ll long long
double dp[1000],adj[1000][1000],e[1000],s[1000],dis[1000],INT=100000000000.0;
int main()
{
    // ios::sync_with_stdio(0);
     freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
     ll t,tt=0;
     cin>>t;
     while(t--)
     {
         tt++;
         ll n,q;
         cin>>n>>q;
         for(int i=0;i<n;i++)
         {
              cin>>e[i]>>s[i];
         }
         for(int i=0;i<n;i++)
         {
              for(int j=0;j<n;j++)
              {
                   cin>>adj[i][j];
              }
         }
         for(int i=0;i<q;i++)
         {
              ll a,b;
              cin>>a>>b;
         }
         for(int i=0;i<n;i++)
         {
              dp[i]=INT;
              dis[i+1]=adj[i][i+1];
         }
         dis[0]=0;
         for(int i=1;i<n;i++)
         {
              dis[i]+=dis[i-1];
         }
         dp[n-1]=0;
         for(int i=n-2;i>=0;i--)
         {
              for(int j=i+1;j<n;j++)
              {
                   if(dis[j]-dis[i]<=e[i])
                   {
                        dp[i]=min(dp[i],dp[j]+(dis[j]-dis[i])/s[i]);
                   }
              }
         }
         cout<<"Case #"<<tt<<": ";
         printf("%.10lf\n",dp[0]);
     }
}
