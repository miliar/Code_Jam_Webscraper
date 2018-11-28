#include <iostream>
#include <cstdlib>
#include <algorithm>
#define MAX 110

using namespace std;

long long hd,ad,hk,ak,b,d;
long long h,ak2,ad2;

void init() {
    h = hd;
    ak2 = ak;
    ad2 = ad;
}

int debuffs(int num) {
    if (num == 0) return 0;
    int t = 0;
    for (int i = 0; i < num; i++) {
        if (h <= ak2-d) {
            h = hd - ak2;
            t++;
        }
        ak2 -= d;
        ak2 = max(ak2, 0ll);
        h -= ak2;
        if (h <= 0) {
            h = 0;
            return -1;
        }
        t++;
    }
    return t;
}

int buffs(int num) {
    if (num == 0) return 0;
    int t = 0;
    for (int i = 0; i < num; i++) {
        if (h <= ak2) {
            h = hd - ak2;
            t++;
        }
        ad2 += b;
        h -= ak2;
        if (h <= 0) {
            h = 0;
            return -1;
        }
        t++;
    }
    return t;
}

int kill() {
    int t = 0;
    int sum = 0;
    while (sum < hk) {
        if (h <= ak2 && sum + ad2 < hk) {
            h = hd - ak2;
            t++;
        }
        sum += ad2;
        t++;
        if (sum >= hk) break;
        h -= ak2;
        if (h <= 0) {
            h = 0;
            return -1;
        }
    }
    return t;
}

int main() {
    int T;
    cin >> T;
    for (int TC = 1; TC <= T; TC++) {
        cin >> hd >> ad >> hk >> ak >> b >> d;

        long long ans = 1e18;
        for (int i = 0; i < MAX; i++) {
            for (int j = 0; j < MAX; j++) {
                init();
                long long td = debuffs(i);
                if (td == -1) continue;
                long long tb = buffs(j);
                if (tb == -1) continue;
                long long tk = kill();
                if (tk == -1) continue;
                ans = min(ans, td + tb + tk);
                //if (TC == 1 && td + tb + tk == 6) { cerr << i << ' ' << j << " : " << td << ' ' << tb << ' ' << tk << endl; }
            }
        }

        cout << "Case #" << TC << ": ";
        if (ans == 1e18) cout << "IMPOSSIBLE\n";
        else cout << ans << '\n';
    }
}
