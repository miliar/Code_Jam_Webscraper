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
        string pancakes;
        ll k;
        cin >> pancakes >> k;
        // dbg(pancakes);
        // dbg(k);

        ll ans = 0;
        const auto n = pancakes.size();

        ll loops = 0;
        const ll maxloops = 10000;
        while(loops < maxloops) {
            // dbg(loops);
            fori(i, 0, n-k+2) {
                // dbg(i);
                if(pancakes[i] == '-') {
                    if(i+k <= n) {
                        fori(j, 0, k) {
                            // dbg(pancakes[i+j]);
                            pancakes[i+j] = (pancakes[i+j] == '+' ? '-' : '+');
                            // dbg(pancakes[i+j]);
                        }
                        ++ans;
                    }
                    else {
                    }
                }

                if(count(begin(pancakes), end(pancakes), '-') == 0) {
                    goto end;
                }
                else {
                    ++loops;
                }
            }
        }

        end:
        cout << "Case #" << (tt+1) << ": ";
        if(count(begin(pancakes), end(pancakes), '-') != 0) {
            cout << "IMPOSSIBLE";
        }
        else {
            cout << ans;
        }
        cout << endl;
    }

    return 0;
}
