#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll k[1005],s[1005];
int main()
{
    freopen("test1.txt","r",stdin);
    freopen("file1.txt","w",stdout);
    ll t,d,n;
    cin>>t;
    int cnt=0;
    while(t--)
    {
        cnt++;
        cout<<"Case #"<<cnt<<": ";
        cin>>d>>n;
        long double maxi=0;
        for(ll i=1;i<=n;i++){
            cin>>k[i]>>s[i];
            long double p= (d- k[i])/(s[i]*(1.0));
            maxi=max(maxi,p);
        }
        long double ans= d/(maxi*(1.0));
        printf("%0.6Lf\n",ans);
    }
}
