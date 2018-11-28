#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

pair<ll, ll> splitSpace(ll space) {
    if (space & 1) {
        return make_pair(space / 2, space / 2);
    }
    return make_pair(space / 2, (space - 1)  /2);
}

pair<ll, ll> solve(ll n, ll k) {
    map<ll, ll, greater<ll> > leftNum;
    leftNum[n] = 1;
    while (true) {
        auto i = leftNum.begin();
        ll left = i->first;
        ll num = i->second;
        leftNum.erase(i);
        if (num >= k) {
            return splitSpace(left);
        } else {
            k -= num;
            pair<ll, ll> s = splitSpace(left);
            if (s.first > 0) {
                leftNum[s.first] += num;
            }
            if (s.second > 0) {
                leftNum[s.second] += num;
            }
        }
    }
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        ll n, k;
        cin >> n >> k;
        pair<ll, ll> ans = solve(n, k);
        cout << "Case #" << (i + 1) << ": " << ans.first << " " << ans.second;
        if (i + 1 < t) {
            cout << endl;
        }
    }
    return 0;
}