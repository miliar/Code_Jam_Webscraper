#include <bits/stdc++.h>

#define ll long long
using namespace std;
ifstream f("d.in");
ofstream g("d.out");

struct statuss{
    ll lo,hi,ramas;
};

const ll INF = 1000000000000000003;

ll t,n,k,ans1,ans2,ramas;


int main()
{
    f >> t;
    for(ll co = 1; co <= t; ++co){
        f >> n >> k;

        //set<pair<ll,ll> > H;///heap in care tin -dimensiunea segmentului si inceputul lui
        set<pair<ll,ll> > H;

        ans1 = 0;
        ans2 = INF;

        H.insert(make_pair(-n,1));

        while(!H.empty()){
            ll dim = -(*H.begin()).first;
            ll lo = (*H.begin()).second;

            ll hi = lo + dim - 1;

            ll mid = (lo + hi) / 2;

            H.erase(H.begin());

            k--;

            if(k == 0){
                ans1 = max(mid - lo, hi - mid);
                ans2 = min(mid - lo, hi - mid);
                break;
            }
            if(hi - mid > mid - lo){
                if(mid + 1 <= hi)
                    H.insert(make_pair(-(hi - mid),mid + 1));
                if(lo <= mid - 1)
                    H.insert(make_pair(-(mid - lo),lo));
            }else{
                if(lo <= mid - 1)
                    H.insert(make_pair(-(mid - lo),lo));
                if(mid + 1<= hi)
                    H.insert(make_pair(-(hi - mid),mid + 1));
            }
        }
        g << "Case #" << co << ": ";
        g << ans1 << ' ' << ans2 << '\n';
    }
    return 0;
}
