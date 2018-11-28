#include <bits/stdc++.h>
using namespace std;
const int inf = 1e9 + 7;

int _hd, _ad, _hk, _ak, _b, _d;
int hd, ad, hk, ak, b, d;

int simulate(int debuff, int buff) {
    hd = _hd;
    ad = _ad;
    hk = _hk;
    ak = _ak;
    b = _b;
    d = _d;

    int moves = 0;
    int timeout = 1000;

    while (debuff > 0 && timeout > 0) {
        ++moves;
        --timeout;

        if (hd - (ak - d) <= 0) {
            hd = _hd;
        } else {
            --debuff;
            ak -= d;
            if (ak < 0) {
                ak = 0;
            }
        }

        hd -= ak;
        if (hd <= 0) {
            return inf;
        }
    }
    if (timeout <= 0) {
        return inf;
    }

    timeout = 1000;
    while (buff > 0 && timeout > 0) {
        ++moves;
        --timeout;

        if (hd - ak <= 0) {
            hd = _hd;
        } else {
            --buff;
            ad += b;
        }

        hd -= ak;
        if (hd <= 0) {
            return inf;
        }
    }
    if (timeout <= 0) {
        return inf;
    }

    timeout = 1000;
    while (hk > 0 && timeout > 0) {
        ++moves;
        --timeout;

        if (hd - ak <= 0 && hk - ad > 0) {
            hd = _hd;
        } else {
            hk -= ad;
            if (hk <= 0) {
                return moves;
            }
        }

        hd -= ak;
        if (hd <= 0) {
            return inf;
        }
    }
    if (timeout <= 0) {
        return inf;
    }

    return moves;
}

void solve() {
    cin >> _hd >> _ad >> _hk >> _ak >> _b >> _d;

    int moves = inf;
    for (int i = 0; i < 150; i++) {
        for (int j = 0; j < 150; j++) {
            moves = min(simulate(i, j), moves);
        }
    }

    if (moves == inf) {
        cout << "IMPOSSIBLE\n";
    } else {
        cout << moves << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int numCases;
    cin >> numCases;
    for (int i = 1; i <= numCases; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cerr << i << endl;
    }
    return 0;
}
