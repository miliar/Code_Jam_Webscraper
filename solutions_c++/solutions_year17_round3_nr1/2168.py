#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
# define M_PIl 3.141592653589793238462643383279502884L
#define fi first
#define se second
#define pu          push_back
#define mp          make_pair
priority_queue<pll> q;
vector<pll> h,r,v;
int main(){
    ll cse; 
	scanf("%lld",&cse);
    for(ll i=1;i<=cse;i++){
        printf("Case #%lld: ", i);
        r.clear();
        v.clear();
        h.clear();
        ll N,K;
        scanf("%lld%lld",&N,&K);
        for(ll j=1;j<=N;j+=1){
            ll R,H;
            scanf("%lld%lld",&R,&H);
            r.pu(pll(R,j));
            ll e0 = 2*R*H;
            h.pu(pll(e0,j));
            v.pu(pll(R,H));
        }
        sort(h.rbegin(),h.rend());
        sort(r.rbegin(),r.rend());
        ll res=0;
        for(ll j=0;j<=r.size()-1;j+=1){
            ll e1=0,z=K-1,p1=r[j].se;
            ll e2=v[p1-1].se,e3=v[p1-1].fi;
            e1+=e3*2*e2;
            ll e5=0;
            while(e5<N && z>0){
                ll p2=h[e5].se;
                if(p2==p1)e5+=1;
                else {
                    ll e0= h[e5].fi;
                    e1+=e0;
                    z-=1;e5+=1;
                }
            }
            if(z == 0)res = max(res, r[j].fi*r[j].fi + e1);
        }
        double st1=res;
        st1 = st1*M_PIl;
         cout.setf(ios::showpoint);
        cout.precision(9);
        cout.setf(ios::fixed);
        cout<<st1<<endl;
    }
}