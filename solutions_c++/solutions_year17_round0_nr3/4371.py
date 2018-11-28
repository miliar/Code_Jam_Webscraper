#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

struct chel {
    ll l, r, pos;
};

bool compare(chel a, chel b) {
    if (a.l == b.l) {
        if (a.r == b.r) return a.pos > b.pos;
        return a.r < b.r;
    }
    return a.l < b.l;
}

bool compareq(pair<ll, ll> a, pair<ll, ll> b) {
    if((a.second - a.first) == (b.second - b.first)) return a.first < b.first;
    return (a.second - a.first) > (b.second - b.first);
}

int main() {
#define TASK "C-small-2-attempt0"
    freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
    int t;
    cin >> t;
    for (int cs = 1; cs <= t; ++cs) {
        ll n, k;
        cin >> n >> k;
        set<chel, bool(*)(chel a, chel b)> chels(&compare);
        set<pair<ll, ll>, bool(*)(pair<ll, ll> a, pair<ll, ll> b)> q(&compareq);
        q.insert(make_pair((ll) 1, n));
        while (k > chels.size() && !q.empty()) {
            ll l = q.begin()->first, r = q.begin()->second;
            if (!chels.empty() && r - l < chels.begin()->r + chels.begin()->l)
                k -= chels.size(), chels.clear();
            q.erase(q.begin());
            chel last;
            last.pos = (l + r) / (ll) 2;
            last.l = last.pos - l;
            last.r = r - last.pos;
            chels.insert(last);
            if (last.l > 0) q.insert(make_pair(l, last.pos - 1));
            if (last.r > 0) q.insert(make_pair(last.pos + 1, r));
            //cout << k - chels.size() << "\n";
        }
        auto ans = chels.begin();
        for (int i = 1; i < chels.size() - k; ++ans, ++i);
        cout << "Case #" << cs << ": " << max(ans->l, ans->r) << " " << min(ans->l, ans->r) << "\n";
    }
    return 0;
}
