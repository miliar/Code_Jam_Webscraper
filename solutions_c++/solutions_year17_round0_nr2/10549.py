#include <bits/stdc++.h>
#define ll long long
#define whl(t) while(t--)
using namespace std;
//akashravi.tk
int sortchk(ll int n)
{
    ll int nd = n%10;
    n = n/10;
    while (n)
    {
        ll int d = n%10;
        if (d > nd)
            return 0;
        nd = d;
        n = n/10;
    }

    return 1;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll int t,i,j,n,m;
    cin>>t;
    m=t;
    whl(t)
    {
        cin>>n;
        for(i=n; i>0; i--)
        {
            if(sortchk(i))
            {
                j=i;
                break;
            }
        }
        cout<<"Case #"<<m-t<<": "<<j<<"\n";
    }

   // cout<<"\n";

    return 0;
}
