#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (ll (i)=(0);(i)<(ll)(n);++(i))
typedef pair<int, int> P;
typedef unsigned long long ll;

inline void output(ll i, string n) {
    cout << "Case #" << i+1 << ": " << n << endl;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n;
    cin >> n;

    rep(i, n) {
        ll d;
        cin >> d;

        string t = to_string(d);
        reverse(t.begin(), t.end());

        rep(j, t.size()-1) {
            if (t[j]-'0' < t[j+1]-'0') {
                t[j] = '9';
                t[j+1]--;
                for (int i=0; i<j; ++i) t[i]='9';
            }
        }

        reverse(t.begin(), t.end());

        if (t[0] == '0') {
            t.erase(t.begin());
            rep(j, t.size()) t[j] = '9';
        }

        output(i, t);

        // rep(j, t.size()-1) {
        //     if (t[j]-'0' > t[j+1]-'0') {
        //         if (j+1 == t.size()-1 && t[j] == '0') {
        //             t.pop_back();
        //             rep(k, t.size()) {
        //                 t[k] = '9';
        //             }
        //         }
        //         else {
        //             t[j]--;
        //             for (int k=j+1; k<t.size(); ++k) {
        //                 t[k]='9';
        //             }
        //         }
        //     }
        // }
    }
}
