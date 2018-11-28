#include <bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define bp __builtin_popcount

#define mt(a,b,c) mp(a,mp(b,c))
#define min3(a,b,c) min(a,min(b,c))

const ll mo=1e9+7;
const ll INF=1e17;
const ld pi=acos(-1);
const int mxn=2e5+5;
const int cons=1;

using namespace std;

map<ll,ll> m1,m2;
map<ll,ll>::reverse_iterator it;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T,t;
    ll n,k,ct,ans;
    bool f;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        m1.clear();
        m2.clear();
        cin>>n>>k;
        m2[n]=1;
        ct=0;
        f=1;
        while(f)
        {
            m1.clear();
            for(it=m2.rbegin();it!=m2.rend();it++)
            {
                m1[ it->first ]=it->second;
                ct+=(it->second);
                if(ct>=k)
                {
                    ans=it->first;
                    f=0;
                    break;
                }
            }
            m2.clear();
            for(it=m1.rbegin();f&&it!=m1.rend();it++)
            {
                if((it->first)%2==0)
                {
                    m2[(it->first)/2]+=m1[(it->first)];
                    m2[(it->first)/2-1]+=m1[(it->first)];
                }
                else
                {
                    m2[(it->first)/2]+=(2*m1[(it->first)]);
                }
            }
        }
        if(ans%2==1)
        {
            cout<<(ans/2)<<" "<<(ans/2)<<"\n";
        }
        else
        {
            cout<<(ans/2)<<" "<<(ans/2-1)<<"\n";
        }
    }
    return 0;
}
