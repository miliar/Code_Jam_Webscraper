#include<bits/stdc++.h>
using namespace std;
#define ll long long
set<ll> st;
set<ll>::iterator itr;
map<ll,ll> mp;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ll t,ti=0;
    cin>>t;
    while(t--)
    {
        st.clear();
        mp.clear();
        ti++;
        ll n,k,ans;
        cin>>n>>k;
        st.insert(n);
        mp[n]=1;
            ll a,b;
        while(k>0)
        {
            itr=st.end();
            itr--;
            ll p=*itr;
            st.erase(p);
            k-=mp[p];
            if(p%2!=0)
            {
                a=b=p/2;
            }
            else
            {
                a=p/2;
                b=p-a-1;
            }
            st.insert(a);
            st.insert(b);
            mp[a]+=mp[p];
            mp[b]+=mp[p];
            mp.erase(p);
        }
        cout<<"Case #"<<ti<<": ";
        cout<<a<<" "<<b<<"\n";

    }
}
