#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

vector<short> ll2digs(ll x) {
    vector<short> digs;
    ll xcp = x;
    while (xcp) {
        digs.push_back(xcp % 10);
        xcp /= 10;
    }
    reverse(digs.begin(), digs.end());
    return digs;
}

ll digs2ll(const vector<short>& x) {
    ll ans = 0;
    for (auto entry : x) {
        ans *= 10;
        ans += entry;
    }
    return ans;
}

bool isgood(ll x) {
    auto d = ll2digs(x);
    for (size_t i = 0; i + 1 < d.size(); ++i) {
        if (d[i] > d[i + 1]) return false;
    }
    return true;
}

int brute(int x) {
    for (int v = x; v > 0; --v) {
        if (isgood(v)) {
            return v;
        }
    }
    assert(false);
}

ll smart(ll x) {
    auto digs = ll2digs(x);
    int bad = -1;
    int val = -1;
    for (size_t pl = 0; pl + 1 < digs.size(); ++pl) {
        if (digs[pl] > digs[pl + 1]) {
            bad = pl;
            val = digs[pl];
            break;
        }
    }
    if (bad >= 0) {
        if (val == 1) {
            digs.pop_back();
            for (auto& v: digs) v = 9;
        } else {
            for (int nxt = bad + 1; nxt < int(digs.size()); ++nxt) {
                digs[nxt] = 9;
            }
            for (int nxt = int(bad); nxt >= 0 && digs[nxt] == val; --nxt) {
                if (nxt != 0 && digs[nxt - 1] == val) digs[nxt] = 9;
                else --digs[nxt];
            }
        }
    }
    return digs2ll(digs);
}


int main() {
    int t; ll n; cin >> t;
    for (int _ = 1; _ <= t; ++_) {
        cout << "Case #" << _ << ": ";
        cin >> n;
        cout << smart(n) << endl;
    }
}
