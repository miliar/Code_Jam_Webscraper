#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
    freopen("clarge.in","r",stdin);
    freopen("clarge.out","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll tt;
    cin>>tt;
    ll n,k,lo,hi,top,freq,mini,maxi;
    for(ll t=1; t<=tt; t++)
    {
        cin>>n;
        cin>>k;
        map<ll,ll,greater<ll>> m;
        m[n]=1;
        while(1)
        {
            top=m.begin()->first;
            freq=m.begin()->second;
            lo=(top-1)/2;
            hi=top-lo-1;
            m[hi]+=freq;
            m[lo]+=freq;
            m.erase(m.begin());
            k=k-freq;
            if(k<=0)
            {
                mini=min(lo,hi);
                maxi=max(lo,hi);
                break;
            }
        }

        cout<<"Case #"<<t<<": "<<maxi<<" "<<mini<<endl;
        cerr<<"Test Case "<<t<<" Solved"<<endl;
    }
    return 0;
}
