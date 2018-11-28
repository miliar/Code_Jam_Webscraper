#include <cstdio>
#include <iostream>
#include <map>
using namespace std;

typedef long long ll;

int main() {
    //freopen("in.txt", "r", stdin);
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int cases;
    cin >> cases;
    for(int caseno=1; caseno<=cases; caseno++) {
        ll N, K, done=0, half, len, ans;
        cin >> N >> K;

        map<ll, ll> m;
        m[N] = 1;

        while(!m.empty()) {
            map<ll, ll> mm;
            for(map<ll, ll>::reverse_iterator it = m.rbegin(); it != m.rend(); ++it) {
                if(!it->first) continue;

                done += it->second;
                if(done >= K) {
                    ans = it->first;
                    goto OUT;
                }

                len = it->first;
                len -= 1;
                half = len >> 1;
                mm[len-half] += it->second;
                mm[half] += it->second;
//                if((it->first)&1) {
//                    mm[(it->first)>>1] += (it->second)<<1;
//                }
//                else {
//                    half = (it->second)>>1;
//                    mm[half] += it->second;
//                    mm[half-1] += it->second;
//                }
            }

            m = mm;
        }

OUT:
        ans -= 1;
        half = ans >> 1;
        cout << "Case #" << caseno << ": " << (ans-half) << " " << half << "\n";
        cerr << "Case #" << caseno << ": " << (ans-half) << " " << half << "\n";
    }
    return 0;
}
