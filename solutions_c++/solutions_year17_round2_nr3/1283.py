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


void scan(vector<int> & v)
{
    for(int i=0;i<v.size();i++)
        cin>>v[i];
}
void print(vector<int> & v)
{
    for(int i=0;i<v.size();i++)
        cout<<v[i];
}
void fun()
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
    for(int i=n-2;i>=0;i--)
    {
        //int fi=max(i+v[i].f,n-1);
        //double dis=dist[i];
        for(int j=i+1;j<=n-1&&dist[j]<=dist[i]+v[i].f;j++)
        {
            if(dp[j]!=1e18)
            {
                double temp=((double)(dist[j]-dist[i])/(double)(v[i].s))+dp[j];
                dp[i]=min(dp[i],temp);
            }
           // dis=dist[j];
        }

    }
    cout<<fixed<<setprecision(18)<<dp[0];
}
int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);cout.tie(0);
    bool test=1;
    if(test==1)
    {
        freopen("input_file_name.txt","r",stdin);
        freopen("output_file_name.txt","w",stdout);
    }
    int t=1;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        fun();
        cout<<endl;
    }
    int acc;cin>>acc;
    return 0;
}
