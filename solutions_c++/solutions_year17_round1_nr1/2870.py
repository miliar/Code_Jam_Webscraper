#include<bits/stdc++.h>
#define ll long long
#define elif else if
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define lim 1000010
#define sz(a) int(a.size())
#define sc(a) scanf("%lld",&a)
#define sc2(a,b) scanf("%lld %lld",&a,&b)
#define sc3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
#define sf(a) scanf("%f",&a)
#define pr(a) printf("%lld",a);
#define pf(a) printf("%f",a);
#define rep(n) for(long long i=0;i<n;i++)
#define forab(a,b) for(long long i=a;i<b;i++)
#define INF 1e18
#define Sort(a) sort(a.begin(),a.end())
using namespace std;
int main()
{
    ll t;
    cin>>t;
    for(ll m=1;m<=t;m++)
    {
        ll r,c;
        cin>>r>>c;
        char grid[r][c+1];
        for(ll i=0;i<r;i++)
            for(ll j=0;j<c;j++)
            cin>>grid[i][j];
        ll rowcount=0;
        ll j=0;
        if(grid[0][j]=='?')
        {
            while(grid[0][j]=='?' && j<c)
                j++;
            ll k=0;
            if(j!=c)
            k=j;
                while(k>0)
                {
                    grid[0][k-1]=grid[0][k];
                    k--;
                }
        }
        while(true)
        {
            if(grid[0][j]!='?' and j<c)
            {
                j++;
            }
            else
            {
                while(j<c && grid[0][j]=='?')
                {
                    grid[0][j]=grid[0][j-1];
                    j++;
                }
                if(j==c)
                    break;
            }

        }
        // for(ll i=0;i<r;i++)
        // {
        //     for(ll j=0;j<c;j++)
        //     cout<<grid[i][j];
        //     cout<<endl;
        // }
        for(ll i=1;i<r;i++)
        {
            ll j=1,left=0;
            ll arr[c];
            for(ll k=0;k<c;k++)
            arr[k]=0;
            bool check=true;
            while(j<c)
            {
                if(grid[i-1][j]!=grid[i-1][j-1])
                {
                    check=true;
                    for(ll k=left;k<j;k++)
                        if(grid[i][k]!='?')
                    {
                        check=false;
                        break;
                    }
                    if(check)
                        for(ll k=left;k<j;k++)
                        arr[k]=1;
                    left=j;
                }
                j++;
            }
            for(ll k=left;k<c;k++)
                if(grid[i][k]!='?')
                {
                    check=false;
                    break;
                }
            if(grid[i][left]=='?' && check)
            for(ll k=left;k<c;k++)
                arr[k]=1;
            j=0;
            while(grid[i][j]=='?' && j<c)
                j++;
            if(j!=c)
            for(ll k=j-1;k>=0 && arr[k]!=1;k--)
                grid[i][k]=grid[i][j];
            while(j<c)
            {
                if(grid[i][j]=='?')
                    grid[i][j]=grid[i][j-1];
                j++;
            }
            for(ll j=0;j<c;j++)
                if(arr[j]==1)
                    grid[i][j]=grid[i-1][j];
        }
        if(grid[0][0]=='?')
            {
                ll i=0;
                while(grid[i][0]=='?')
                    i++;
                for(;i>0;i--)
                {
                    for(ll j=0;j<c;j++)
                        grid[i-1][j]=grid[i][j];
                }
            }
        cout<<"Case #"<<m<<":\n";
        for(ll i=0;i<r;i++)
        {
            for(ll j=0;j<c;j++)
            cout<<grid[i][j];
            cout<<endl;
        }
    }
    return 0;
}
