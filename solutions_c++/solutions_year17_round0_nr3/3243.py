#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
priority_queue<ll>q;
map<ll,ll>mp;

ll m,n;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;
    cin>>T;
    for(int it=1;it<=T;it++)
    {
        cin>>m>>n;
        mp.clear();
        while(!q.empty())
            q.pop();
        q.push(m);
        mp[m]=1;
        while(n)
        {
            ll t = q.top();
            q.pop();
            //cout<<"top="<<t<<" mp="<<mp[t]<<" n="<<n<<endl;
            if(mp[t]>=n)
            {
                cout<<"Case #"<<it<<": ";
                if(t%2==0)
                {
                    cout<<t/2<<" "<<t/2-1<<endl;
                }
                else
                {
                    cout<<t/2<<" "<<t/2<<endl;
                }
                break;
            }
            else
            {
                ll l,r;
                if(t%2==0)
                {
                    l = t/2;
                    r = t/2-1;
                }
                else
                {
                    l=r=t/2;
                }

                if(mp.find(l)==mp.end())
                {
                    mp[l]=mp[t];
                    q.push(l);
                    //cout<<"push l "<<l<<endl;
                }
                else
                    mp[l]+=mp[t];

                if(mp.find(r)==mp.end())
                {
                    mp[r]=mp[t];
                    q.push(r);
                    //cout<<"push r "<<r<<endl;
                }
                else
                    mp[r]+=mp[t];

                n-=mp[t];
                mp[t]=0;
            }
        }
    }
    return 0;
}
