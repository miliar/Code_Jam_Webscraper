#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

const ll oo = ll(1e17);

pair<ll,ll> brute(ll n, ll k) {

    vector<ll> L(n), R(n);
    vector<bool> S(n, false);
    pair<ll,ll> ans;
//    for(auto xd : S) cout << xd << " "; cout << endl;

    while(k--) {
        for(int i = 0; i < n; ++i) {
            if(S[i]) {
                L[i] = R[i] = -1;
                continue;
            }

            int l = -1, r = -1;
            for(int j = i; j >= 0 && !S[j]; j--)
                l++;

            for(int j = i; j < n && !S[j]; j++)
                r++;

            L[i] = l;
            R[i] = r;
        }

        int idx = 0;
        for(int i = 0; i < n; ++i) {

            ll currentMax = max(L[idx], R[idx]);
            ll currentMin = min(L[idx], R[idx]);

            ll maxm = max(L[i], R[i]);
            ll minm = min(L[i], R[i]);

            if( (currentMin < minm) || (currentMin == minm && currentMax < maxm) ) {
                idx = i;
            }
        }

        S[idx] = true;
        ans = {max(L[idx], R[idx]), min(L[idx], R[idx])};
//        cout << L[idx] << " " << R[idx] << endl;
//        for(auto xd : S) cout << xd << " "; cout << endl;
    }

    return ans;
}

struct CMP {
    bool operator()(const ll& a, const ll& b) const {
        return a > b;
    }
};

pair<ll,ll> greedy(ll n, ll k) {
    map<ll, ll, CMP> pq = { {n, 1} };
    pair<ll,ll> ans;
    for(int i = 0; i < k; ++i) {
        auto it = pq.begin();
        ll maxm = it->first, ctr = it->second;
        assert(ctr >= 1);

        if(ctr == 1) pq.erase(it);
        else pq[maxm]--;

        ll x = maxm / 2;
        ll y = max(0LL, maxm - x - 1);
        pq[x]++;
        pq[y]++;
        ans = {max(x,y), min(x,y)};
    }

    return ans;
}




int main() {

    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-small-2-attempt0.out", "w", stdout);
    int T;
    ll n, k;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cin >> n >> k;
//        auto ans = brute(n, k);
        auto ans2 = greedy(n , k);
//        cout << "Case #" << t << " : " << ans.first << " " << ans.second << '\n';
        cout << "Case #" << t << ": " << ans2.first << " " << ans2.second << '\n';
//        assert(ans == ans2);
    }
}
