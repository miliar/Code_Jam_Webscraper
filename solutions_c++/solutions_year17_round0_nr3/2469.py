#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;


ll t,n,k;
map<ll,ll> ac;

map<ll,ll>::iterator mx;

int main()
{
   freopen("C-large.in","rt",stdin);
   freopen("out.txt","wt",stdout);



    cin>>t;
    for(int c=1; c<=t; c++)
    {
        cin>>n>>k;
        ac[n]=1;
ll m,M;
        while(k>0)
        {
            mx=ac.end();
            mx--;
            // cout<<mx->first<<" "<<mx->second<<endl;
            ll f=mx->first, s=mx->second;
            f--;
            if(k > s)
            {
                ac[f/2LL+f%2LL]+=s;
                ac[f/2LL]+=s;
                ac.erase(mx);
                k-=s;

            }
            else
            {
                M=f/2LL+f%2LL;
                m=f/2LL;

                ac[f]-=k;
                ac[M]+=k;
                ac[m]+=k;
                k=0;
            }

        }

        cout<<"Case #"<<c<<": "<<M<<" "<<m<<endl;
        ac.clear();


    }

    return 0;
}
