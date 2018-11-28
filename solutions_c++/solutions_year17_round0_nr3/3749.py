#include<bits/stdc++.h>
#define ll long long
#define elif else if
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define lim 1000010
#define sz(a) int(a.size())
#define sc(a) scanf("%lld",&a)
#define sc2(a,b) scanf("%lld %lld",&a,&b)
#define sc3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
#define sf(a) scanf("%f",&a)
#define pr(a) printf("%lld",a);
#define pf(a) printf("%f",a);
#define rep(n) for(long long i=0;i<n;i++)
#define forab(a,b) for(long long i=a;i<b;i++)
#define INF 1e18
#define Sort(a) sort(a.begin(),a.end())
using namespace std;
bool wayToSort(ll i,ll j){return i>j;}
int main()
{
    ll t,n,k;
    cin>>t;
    rep(t)
    {

        cin>>n>>k;
        map<ll,ll> m;
        vector<ll> v;
        m[n]=1;
        v.pb(n);
        while(k>0)
        {
            ll ele,siz=sz(v);
            //cout<<"k="<<k<<" size="<<siz<<endl;
            for(ll j=0;j<siz;j++)
            {
                ele=v[j];
                //cout<<k<<" "<<m[ele]<<endl;
                if(k>m[ele])
                    k-=m[ele];
                else
                {
                    k=0;
                    cout<<"Case #"<<i+1<<": ";
                    if(ele%2!=0)
                        cout<<ele/2<<" "<<ele/2<<endl;
                    else
                        cout<<ele-ele/2<<" "<<ele/2-1<<endl;
                    break;
                }
                if(ele%2==0)
                {
                    if(m.find(ele/2)!=m.end())
                        m[ele/2-1]+=m[ele];
                    else
                        m[ele/2-1]=m[ele];
                    if(m.find(ele/2)!=m.end())
                        m[ele-ele/2]+=m[ele];
                    else
                        m[ele-ele/2]=m[ele];
                    if(ele-ele/2>0)
                        v.pb(ele-ele/2);
                    if(ele/2>0)
                        v.pb(ele/2-1);

                }
                else
                {
                    if(m.find(ele/2)!=m.end())
                        m[ele/2]+=m[ele]*2;
                    else
                        m[ele/2]=m[ele]*2;
                    if(ele/2>0)
                        v.pb(ele/2);
                }
                m.erase(ele);
            }
            v.erase(v.begin(),v.begin()+siz);
        }
    }
    return 0;
}
