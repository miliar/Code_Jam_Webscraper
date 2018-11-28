#include <bits/stdc++.h>

using namespace std;

int main () {
    int tt; 
    cin >> tt;
    for (int cases = 1; cases <= tt; ++cases) {
        cout << "Case #" << cases << ": ";
        double d, n;
        cin >> d >> n;

        double h, v, best = 0x7070707070707070L;
        for (int i = 0; i < n; ++i) {
            cin >> h >> v;
            if (h >= d)
                continue;
            best = min(best, v*d/(d - h));
        }

        cout << fixed << setprecision(6) << best << "\n";    
    }
}
