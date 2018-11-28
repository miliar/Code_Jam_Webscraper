#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
string s;
vector<ll>v,vv,vvv;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,tt=0;
    ll i,x=1,y=1;
    cin>>t;
    for(i=0;i<=18;i++)
    {
        vv.push_back(x);x=x*10+1;
        vvv.push_back(y);y*=10;
    }
    while(tt<t)
    {
        ll k,n=0;
        cin>>k;x=k;v.clear();

        while(x){v.push_back(x%10);x/=10;}
        printf("Case #%d: ",++tt);
        for(i=v.size()-1;i>=0;i--)
        {
            if(x)cout<<9;
            else
                if(v[i]*vv[i]<=k)
                {
                    k%=vvv[i];cout<<v[i];
                }
                else
                {
                    x=1;
                    if(v[i]>1)cout<<v[i]-1;
                }
        }
        printf("\n");
    }
    return 0;
}
