#include <iostream>
#include <cassert>
#include <climits>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

const int BIG = 2100000000;

typedef long long ll;

// min # of turns without ever debuffing
int opt(ll ch, ll Hd, ll Ad, ll Hk, ll Ak, ll B) {
    assert(ch > 0);
    assert(Hd > 0);
    ll before_first_cure = Ak ? (ch-1) / Ak : BIG;
    //bool Hd_exact = Hd % Ak == 0;
    ll per_cure = Ak ? (Hd - 1) / Ak - 1 : BIG;
    int turns = 0;
    if (B == 0) {
        turns = (Hk + Ad - 1) / Ad;
    } else {
        ll n = floor((sqrt(double(Hk * B)) - Ad) / B);
        turns = min(
            n + (Hk + Ad + (B * n) - 1) / (Ad + B * n),
            n+1 + (Hk + Ad + (B * (n+1)) - 1) / (Ad + B * (n+1))
            );
    }
    if (turns <= before_first_cure + 1) {
        return turns;
    }
    if (per_cure <= 0) return BIG;
    ll extra = 1;
    ll remaining = turns - before_first_cure;
    extra += (remaining - 1) / per_cure;
    if (per_cure == 1 || remaining % per_cure == 1) {
        extra -= 1;
    }
    return turns + extra;
}

int main() {
    int T;
    cin >> T;
    int cas = 1;
    vector<int> res(T);
#pragma omp parallel for
    for (int z = 1; z <= T; ++z) {
        int Hd, Ad, Hk, Ak, B, D;
        int caseno;
        #pragma omp critical
        {
            cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
            caseno = cas++;
        }
        int ch = Hd;
        int r = BIG;
        if (Ad >= Hk) {
            // Kill him in one hit
            r = 1;
            goto done;
        }
        if (D == 0) {
            r = opt(Hd, Hd, Ad, Hk, Ak, B);
        } else {
            int n = 0;
            while (r > n) {
                r = min(r, opt(ch, Hd, Ad, Hk, Ak, B) + n);
                if (Ak == 0) break;
                int nAk = max(0, Ak - D);
                if (ch <= nAk) {
                    // Also cure (then tank)
                    ch = Hd - Ak;
                    n += 1;
                }
                if (ch <= nAk) {
                    // Can't actually proceed
                    break;
                }
                Ak = nAk;
                ch -= Ak;
                n += 1;
            }
        }

    done:
        res[caseno-1] = r;
    }
    for (int caseno = 1; caseno <= T; ++caseno) {
        cout << "Case #" << caseno << ": ";
        int r=  res[caseno-1];
        if (r >= BIG) {
            cout << "IMPOSSIBLE";
        } else {
            cout << r;
        }
        cout << endl;
    }
}
