#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll long long
#define fi first
#define se second
using namespace std;
ll r[100];
ll a[100][100];
vector<ll> valid[100];
int main()
{
    freopen("txtin.txt","r",stdin);
    freopen("txtout.txt","w",stdout);
    int t,n,i,j,k,l,m,r1,r2;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        cout<<"Case #"<<test<<": ";
        cin>>n>>m;
        bool vis[100][100];
        for(i=1;i<=n;i++)
        {
            cin>>r[i];
        }
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                vis[i][j]=0;
                cin>>a[i][j];
            }
            sort(a[i]+1,a[i]+m+1);
        }
        ll ans=0;
        vector<int> sum[54];
        for(i=1000000;i>=1;i--)
        {
          int mini=100;
            for(j=1;j<=n;j++)
            {
                sum[j].clear();
                for(k=m;k>0;k--)
                {
                    if(vis[j][k])
                        continue;

                    if((i*r[j])*(ll)90<=a[j][k]*(ll)100&&a[j][k]*(ll)100<=(ll)110*(i*r[j]))
                    {
                        sum[j].pb(k);
                    }

                }
                mini=min(mini,(int)sum[j].size());

            }
            if(mini>0&&mini!=100)
            {
                ans+=mini;
                int temp=mini;
                for(j=1;j<=n;j++)
                    for(k=sum[j].size()-1;temp-->0;--k)
                    vis[j][sum[j][k]]=1;

            }
        }
        cout<<ans<<"\n";
    }
    return 0;
}
