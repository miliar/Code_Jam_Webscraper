#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<utility>
#include<set>
#include <queue>
#define ull unsigned long long
#define ll long long
#define pii pair<int,int>
#define pb(x) push_back(x)
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define FD(i,a,n) for(int i=(a);i>=(n);--i)
using namespace std;
map<ll,ll> mp;
int main()
{
    freopen("inp.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    cin>>t;
    F(p,1,t+1){
        ll n,k;
        cin>>n>>k;

        ll curr = 0;
        ll ans = 0;
        mp[n] = 1;
        while(1){

            map<ll,ll>::reverse_iterator it = mp.rbegin();

            ll x = (*it).first;
            ll val = (*it).second;
            ll nxt = curr + val;

            mp.erase(x);


            //cout<<"x= "<<x<<" val= "<<val<<" curr= "<<curr<<" nxt= "<<nxt<<endl;
            if(k>curr && k<= nxt){
                ans = x;
                break;
            }

            ll y,z;
            if(x&1){
                y = x/2;
                z = x/2;
            } else {
                y = x/2;
                z = x-(1+y);
            }

            //cout<<"x= "<<x<<" val= "<<val<<" curr= "<<curr<<" nxt= "<<nxt<<" y= "<<y<<" z= "<<z<<endl;int tmp;cin>>tmp;
            mp[y]+=val;
            mp[z]+=val;
            curr = nxt;
        }

        if(ans&1){
            cout<<"Case #"<<p<<": "<<ans/2<<" "<<ans/2<<endl;
        } else{
            cout<<"Case #"<<p<<": "<<ans/2<<" "<<ans-(1+ans/2)<<endl;
        }
        mp.clear();
    }
}

