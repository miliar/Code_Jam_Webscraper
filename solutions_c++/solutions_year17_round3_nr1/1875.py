#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
# define M_PIl 3.141592653589793238462643383279502884L

#define jbmr_kkd

priority_queue<pll> q;
vector<pll> h;
vector<pll> r;
vector<pll> v;
int main()
{
    ll test; 
	scanf("%lld", &test);
    for(ll i=1;i<=test;i++){
        printf("Case #%lld: ",i);
        r.clear();h.clear();
        v.clear();
        ll nn;
		ll kk;
        scanf("%lld%lld", &nn, &kk);
        for(ll j =1;j<=nn;j++){
            ll R,H;
            scanf("%lld%lld", &R, &H);
            r.push_back(pll(R, j));
            ll area = 2*R*H;
            h.push_back(pll(area , j));
            v.push_back(pll(R, H));
        }
        sort(r.rbegin(), r.rend());
        sort(h.rbegin(), h.rend());
        ll ans=0;
        for(ll j=0;j<r.size();j++){
            ll areachoos = 0;ll z=kk-1;ll p1 = r[j].second;ll hh=v[p1-1].second;ll rr=v[p1-1].first;
            areachoos+=2*rr*hh;
            ll pos=0;
            while(z>0&&pos<nn){
                ll p2=h[pos].second;
                if(p2==p1) pos++;
                else {
                    ll area= h[pos].first;
                    areachoos+=area;
                    z--;pos++;
                }
            }
            if(z==0)ans=max(ans, r[j].first*r[j].first+areachoos);
        }
        double print=ans;
        print=print*M_PIl;
        cout.setf(ios::showpoint);

        cout.precision(9);       
        cout.setf(ios::fixed);
        cout<<print<<"\n";
    }
}

