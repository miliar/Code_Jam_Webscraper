#include <bits/stdc++.h>
using namespace std;

int main(int argc, char** argv) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int64_t N, K;
        cin >> N >> K;
        uint64_t mx = 0, mn = 0;
        bool found = false;
        map<uint64_t, uint64_t> mp, tmp;
        mp[N] = 1;
        for (uint64_t i = 0, sh = 0, pos = 0; i <= K; i += 1ULL << sh, ++sh) {
            tmp.clear();
            for (auto it = mp.rbegin(); it != mp.rend(); ++it) {
                uint64_t v = it->first - 1, c = it->second;
                uint64_t mx_v = (v + 1) >> 1, mn_v = v >> 1;
                //cout << i << ":: " << v << " " << c << ": " << mx_v << " " << mn_v << endl;
                tmp[mx_v] += c, tmp[mn_v] += c;
                pos += c;
                if (pos >= K && !found) {
                    mx = mx_v, mn = mn_v;
                    found = true;
                    break;
                }
            }
            mp.clear();
            mp = tmp;
            if (found) break;
        }
        cout << "Case #" << t << ": " << mx << " " << mn << "\n";
    }
    return 0;
}
