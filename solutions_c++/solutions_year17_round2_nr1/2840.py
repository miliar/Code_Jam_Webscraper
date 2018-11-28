#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll tt;
    cin>>tt;
    for(ll t=1; t<=tt; t++)
    {
        int d,n,k,s;
        cin>>d;
        cin>>n;
        double ans=-1e12;
        for(int i=0;i<n;i++)
        {
            cin>>k>>s;
            ans=max(ans,(d-k)*1.0/(s*1.0));
        }
        ans=d/ans;
        cout<<setprecision(16);
        cout<<"Case #"<<t<<": "<<ans<<endl;
        cerr<<"Test Case "<<t<<" Solved"<<endl;
    }
    return 0;
}
