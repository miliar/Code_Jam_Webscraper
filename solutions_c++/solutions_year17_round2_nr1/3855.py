#include<bits/stdc++.h>
#define ULL unsigned long long
using namespace std;
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("output.txt","w",stdout);
    long double i,j,n,x,t;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>x>>n;
        long double mx=0.00;
        for(j=0;j<n;j++)
        {
            long double p,q;
            cin>>p>>q;
            long double y;
            y=(x-p)/q;
            mx=max(mx,y);
        }
        long double ans;
        ans=x/mx;
        cout<<"Case #"<<(int)i<<": ";
        cout<<fixed<<setprecision(6)<<(long double)ans<<"\n";
    }
}
