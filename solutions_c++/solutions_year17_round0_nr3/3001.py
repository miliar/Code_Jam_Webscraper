#include <bits/stdc++.h>

using namespace std;

using ll = long long;

inline pair<ll, ll> get_val(ll n) {
    return make_pair(max(max(n - n/2 - 1, n/2), 0ll), max(min(n - n/2 - 1, n/2), 0ll));
}

int main(int argc, char **argv) {
    ios::sync_with_stdio(false);
    srand(time(0));

#ifdef HOME
    freopen("/home/acarus/input.txt", "r", stdin);
    freopen("/home/acarus/output.txt", "w", stdout);
#endif

    int t;
    cin >> t;

    for (int test_case = 1; test_case <= t; ++test_case) {
        ll n, k;
        cin >> n >> k;

        set<ll> ss;
        ss.insert(-n);

        unordered_map<ll, ll> cnt;
        cnt[n] = 1;

        ll i = 0;
        while (i < k) {
            auto cc = -*ss.begin();
            auto rr = get_val(cc);
            ll ccnt = cnt[cc];

            i += ccnt;
            if (i > k - 1) {
                cout << "Case #" << test_case << ": ";
                cout << rr.first << " " << rr.second;
                cout << endl;
                break;
            }

            cnt[rr.first] += ccnt;
            cnt[rr.second] += ccnt;
            cnt.erase(cc);
            ss.erase(-cc);
            ss.insert(-rr.first);
            ss.insert(-rr.second);
        }
    }
    return 0;
}