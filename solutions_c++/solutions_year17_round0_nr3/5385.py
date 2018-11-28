#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    set<ll> s;
    map<ll,ll> m;
    ll t,n,T,i,j,k,val,x,y,sum;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>n>>k;
        s.clear();
        m.clear();
        m[n]=1;
        s.insert(n);
        while(!s.empty())
        {

            val = *s.rbegin();
            x=y=(val)/2;
            if(val%2==0)x--;
            if(x>0)
            {
                m[x]+=m[val];s.insert(x);
            }
            if(y>0)
            {
                m[y]+=m[val];s.insert(y);
            }

            s.erase(val);
        }
        sum=0;
        for(auto it=m.rbegin();it!=m.rend();it++)
        {
            j=it->second;
            sum+=j;
            if(sum>=k)
            {
                val=it->first;
                x=(val-1)/2;
                y=val-x-1;
                break;
            }

        }

        cout<<"Case #"<<t<<": "<<max(x,y)<<" "<<min(x,y)<<endl;

    }
    return 0;
}
