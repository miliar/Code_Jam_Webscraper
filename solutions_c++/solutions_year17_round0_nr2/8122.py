#include <bits/stdc++.h>

#define dbg(x) cout << "* "#x << " = " << (x) << endl
#define fori(idx, ini, lim) for(int idx = int(ini); idx < int(lim); ++idx)
#define ford(idx, ini, lim) for(int idx = int(ini); idx >= int(lim); --idx)

using namespace std;
using ll = long long;
using ull = unsigned ll;
using pii = pair<int, int>;

int main() {
    ios_base::sync_with_stdio(false);

    ll t;
    cin >> t;
    // dbg(t);
    fori(tt, 0, t) {
        string num;
        cin >> num;
        // dbg(num);

        const auto sz = num.size();

        for(ll i = sz-1; i > 0; --i) {
            if(num[i-1] > num[i]) {
                for(ll j = i; j < sz && num[j] != '9'; ++j) {
                    num[j] = '9';
                }

                num[i-1] = num[i-1] - 1;
            }
        }

        // dbg(num);
        ll leading_zeroes = 0;
        fori(i, 0, sz) {
            if(num[i] == '0') {
                ++leading_zeroes;
            }
            else {
                break;
            }
        }

        cout << "Case #" << (tt+1) << ": " << num.substr(leading_zeroes, sz) << endl;
    }

    return 0;
}
