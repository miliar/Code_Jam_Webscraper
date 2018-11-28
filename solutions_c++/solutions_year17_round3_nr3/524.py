#include<bits/stdc++.h>
typedef long long ll;
typedef long double ld;
using namespace std;
const int MX = 1e5+69;
int n;
ld p[55],U,k;
int main()
{
freopen("Code3ts.in","r",stdin);
    freopen("Codejamfuck.txt","w",stdout);
    int t;
    cin>>t;

    for(int TC=1; TC<=t; TC++)
    {
        cin>>n>>k;
        cin>>U;
        for(int i=0; i<n; i++)
            cin>>p[i];
        p[n]=1;
        sort(p,p+n+1);
        ld sum=0,nn=n,opts;
        int opt=n-1;
        for(int i=0; i<=n; i++)
        {
            ld ii = i;
            if(ii*p[i]-sum>U||i==n)
            {
                opt=i-1;
                opts=sum;
                break;
            }
            sum+=p[i];
        }
        for(int i=0; i<=opt; i++)
        {
            p[i]=(U+opts)/((ld)opt+1);
        }
        ld ans=1;
        for(int i=0; i<=n; i++)
            ans*=p[i];
        cout<<fixed;
        cout.precision(6);
        cout<<"Case #"<<TC<<": "<<ans<<"\n";
    }
    return 0;
}
