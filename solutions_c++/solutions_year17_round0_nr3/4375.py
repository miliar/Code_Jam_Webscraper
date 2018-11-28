#include <bits/stdc++.h>
#define ll long long int
#define mod 1000000007
using namespace std;

ll t,tt,n,k,l,h,m,mini,maxi;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    tt=t;
    while(t)
    {
        cin>>n>>k;
        set<pair<ll,ll> > s;
        s.insert(make_pair(-1-n,n+3));
        while(k)
        {
            l=(s.begin()->first+s.begin()->second)/2;
            h=(-s.begin()->first+s.begin()->second)/2;
            s.erase(s.begin());
            if(h-l==1)
                continue;

            m=l+(h-l)/2;
            mini=min(m-l-1,h-m-1);
            maxi=max(m-l-1,h-m-1);
            s.insert(make_pair(l-m,l+m));
            s.insert(make_pair(m-h,m+h));
            k--;

        }

        cout<<"Case #"<<tt-t+1<<": "<<maxi<<" "<<mini<<endl;

        t--;
    }

    return 0;
}
