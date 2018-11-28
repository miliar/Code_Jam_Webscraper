#include<stdio.h>
#include<iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#define ll long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define tr(v,it) for(auto it=v.begin();it!=v.end();it++)
#define int long long
#define f first
#define s second
#define pi 3.14159265358979323846264338327950288419716939937510582097494
using namespace std;
pii rh[1002];
double dp[1002][1002];
double area(int i)
{
    return 2.0*pi*rh[i].f*rh[i].s;
}
main()
{

    //freopen("data.txt","r",stdin);
    //freopen("data1.in","r",stdin);
    //freopen("out2.txt","w",stdout);
    cout<<fixed;
    int t,l1=0;
    cin>>t;
    while(t--)
    {
        l1++;
        int n,m,i,j,k,l;
        cin>>n>>k;
        for(i=0;i<n;i++)
        {
            cin>>rh[i].f>>rh[i].s;
        }
        sort(rh,rh+n);
        reverse(rh,rh+n);
        for(int st=0;st<1;st++)
        {
            for(i=0;i<=n;i++)
            {
                for(j=0;j<=k;j++)
                {
                    if(i==0||j==0||j>i)
                    {
                        dp[i][j]=0.0;
                        continue;
                    }
                    dp[i][j]=dp[i-1][j];
                    if(j==1)
                    {
                        dp[i][j]=max(dp[i][j],dp[i-1][j-1]+area(i-1)+pi*rh[i-1].f*rh[i-1].f);
                        continue;
                    }
                    dp[i][j]=max(dp[i][j],dp[i-1][j-1]+area(i-1));
                }
            }
        }
        cout<<"Case #"<<l1<<": "<<setprecision(12)<<dp[n][k]<<"\n";
    }
    return 0;
}
