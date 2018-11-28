#include <bits/stdc++.h>

using namespace std;

long long T, n, k, l, r, tf, ts;

map<long long, int> g;

int main() {
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("output.out", "w", stdout);
    cin >> T;
    for(int TT = 1; TT <= T; ++TT){
        g.clear();
        cout << "Case #" << TT << ": ";
        cin >> n >> k;
        g[n] = 1;
        while(g.size() != 0){
            auto it = g.end();
            --it;
            tf = it -> first;
            ts = it -> second;
            r = tf / 2;
            if(tf & 1){
                l = tf / 2;
            } else {
                l = (tf - 1) / 2;
            }
            swap(l, r);
            if(tf == 0){
                cout << 0 << " " << 0  << "\n";
                break;
            }
            if(k <= ts){
                cout << l << " " << r  << "\n";
                break;
            } else {
                k -= ts;
                g[l] += ts;
                g[r] += ts;
                g.erase(it);
            }
        }
    }
    return 0;
}