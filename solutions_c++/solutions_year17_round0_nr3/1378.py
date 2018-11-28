#include<bits/stdc++.h>
using namespace std;
#define ll long long
map<ll, ll> mp[1005];
map<ll, ll> :: iterator it;
ll s, sc, f, fc, cnt, one, i, t, n, k, ans;

int main() {
    cin>>t;
    for(ll _t = 1; _t <= t; _t++) {
        cin>>n>>k;
        mp[0].clear();
        mp[0][n] = 1;
        cnt = 1;
        for(i = 1; i <= n; i++) {
            mp[i].clear();
            it = mp[i-1].begin();
            f = it->first;
            fc = it->second;
            mp[i][(f-1)/2] += fc;
            mp[i][f/2] += fc;
            s = -1;
            if(mp[i-1].size() > 1) {
                it++;
                s = it->first;
                sc = it->second;
                mp[i][(s-1)/2] += sc;
                mp[i][s/2] += sc;
            }
            one = 1;
            if(k > (one<<(i-1))) {
                k -= (one<<(i-1));
            }
            else {
                if(s != -1) {
                    if(k <= sc) ans = s;
                    else ans = f;
                }
                else ans = f;
                break;
            }
        }
        printf("Case #%lld: %lld %lld\n", _t, ans/2, (ans-1)/2);
    }

    return 0;
}
