#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int,int> pii;
typedef long long ll;

void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}


void solve_small(ll N, ll K){
    set<pair<ll, ll> > s;
    s.insert(make_pair(-N, 0));
    for(int i = 0; i < K; i++){
        pair<ll, ll> p = *s.begin(); s.erase(p);
        ll cnt = abs(p.first);
        ll pos = p.second;

        ll ls = (cnt - 1) / 2;
        ll rs = cnt / 2;

        s.insert(make_pair(-ls, pos));
        s.insert(make_pair(-rs, pos + (cnt - 1 - ls)));

        if(i == K - 1){
            cout << max(ls, rs) << " " << min(ls, rs) << endl;
        }
    }
}

void solve_large(ll N, ll K){
    map<ll, ll> m;
    m[-N] = 1;
    while(K > 0){
        ll target = abs(m.begin()->first);
        ll cnt    = m.begin()->second;
        m.erase(m.begin());
        ll ls = (target - 1) / 2;
        ll rs =  target / 2;
        K -= cnt;
        m[-ls]+=cnt;
        m[-rs]+=cnt;
        if(K <= 0){
            cout << max(ls, rs) << " " << min(ls, rs) << endl;
        }
    }
}


int main(){
    fastStream();
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        ll K, N;
        cin >> N >> K;
        solve_large(N, K);
    }
    return 0;
}
