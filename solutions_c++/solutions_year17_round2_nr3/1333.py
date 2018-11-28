#include<bits/stdc++.h>
#include <stdio.h>

using namespace std;

#define mod 1000000007LL
#define pi 3.141592653589793238462643383279;
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define f first
#define s second
#define pic pair<char,long long >

void preprocess()
{
    int n,q;
    cin>>n>>q;
    vector<pii> v(n);
    for(int i=0;i<n;i++)
        cin>>v[i].f>>v[i].s;
    int el;
    vector<double> dist(n);
    dist[0]=0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
            {
                cin>>el;
                if(j==i+1)
                    dist[j]=el;
            }
    }
    cin>>el>>el;
    for(int i=1;i<n;i++)
        dist[i]+=dist[i-1];
    //for(int i=0;i<n;i++)
       // cout<<dist[i]<<" ";
    vector<double> dp(n,1e18);
    dp[n-1]=0;
    for(int i=n-2;i>=0;i--){
        for(int j=i+1;j<=n-1&&dist[j]<=dist[i]+v[i].f;j++)
        {
            if(dp[j]!=1e18)
            {
                double temp=((double)(dist[j]-dist[i])/(double)(v[i].s))+dp[j];
                dp[i]=min(dp[i],temp);
            }
        }
    }
    cout<<fixed<<setprecision(18)<<dp[0];
}
int main()
{
    freopen("E:\\input.txt", "r", stdin);
    freopen("E:\\output.txt", "w", stdout);
      int t=1;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        preprocess();
        cout<<endl;
    }
    int acc;cin>>acc;
    return 0;
}
