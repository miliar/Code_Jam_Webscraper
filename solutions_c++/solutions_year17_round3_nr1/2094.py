#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
# define M_PIl 3.141592653589793238462643383279502884L
#define fi first
#define se second
priority_queue<pll> q;
vector<pll> h;
vector<pll> r;
vector<pll> v;
int main(){
    ll testcase; scanf("%lld", &testcase);
    for(ll i = 1; i <= testcase; i++){
        printf("Case #%lld: ", i);
        r.clear();
        h.clear();
        v.clear();
        ll N; ll K;
        scanf("%lld%lld", &N, &K);
        for(ll j = 1; j <= N; j++){
            ll R, H;
            scanf("%lld%lld", &R, &H);
            r.push_back(pll(R, j));
            ll area = 2*R*H;
            h.push_back(pll(area , j));
            v.push_back(pll(R, H));
        }
        sort(r.rbegin(), r.rend());
        sort(h.rbegin(), h.rend());
        ll ans = 0;
        for(ll j = 0; j < r.size(); j++){
            ll areachoose = 0;
            ll z = K-1;
            ll p1 = r[j].se;
            ll hh = v[p1-1].se;
            ll rr = v[p1-1].fi;
            areachoose += 2*rr*hh;
            ll pos = 0;
            while(z > 0 && pos < N){
                ll p2 = h[pos].se;
                if(p2 == p1) pos++;
                else {
                    ll area = h[pos].fi;
                    areachoose += area;
                    z--; pos++;
                }
            }
            if(z == 0)ans = max(ans, r[j].fi*r[j].fi + areachoose);
        }
        double print = ans;
        print = print*M_PIl;
         cout.setf(ios::showpoint);

        cout.precision(9);        // 固定出现多少个小数位

        cout.setf(ios::fixed);
        cout << print << endl;
    }
}
