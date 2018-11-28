#include "bits/stdc++.h"
#define puba push_back
#define ff first
#define ss second
#define bend(_x) begin(_x), end(_x)
#define szof(_x) ((int) (_x).size())
#define cmpby(_x) [](const auto& a, const auto& b) {return (a _x) < (b _x);}
#define TASK_NAME ""

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9 + 7;
const ll INFL = 1e18 + 7;
const double PI = atan2(0, -1);

int solve() {
    int hd, ad, hk, ak, b, d;
    scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);

    ll ans = INFL;
    for (int i = 0; i < 200; ++i) {
        for (int j = 0; j < 200; ++j) {
            //cerr << i << " " << j << endl;
            int c = 0;
            ll chd = hd, cad = ad, chk = hk, cak = ak;
            int rest = i;
            bool flag = false;
            while (rest) {
                if (chd <= max(cak - d, 0ll)) {
                    if (flag) {
                        chd = -1;
                        break;
                    }
                    flag = true;
                    chd = hd;
                    ++c;
                    chd -= cak;
                } else {
                    flag = false;
                    cak = max(cak - d, 0ll);
                    --rest;
                    ++c;
                    chd -= cak;
                }
                if (chd <= 0) {
                    break;
                }
            }

            if (chd <= 0) {
                continue;
            }

            rest = j;
            flag = false;
            while (rest) {
                if (chd <= cak) {
                    if (flag) {
                        chd = -1;
                        break;
                    }
                    flag = true;
                    chd = hd;
                    ++c;
                    chd -= cak;
                } else {
                    flag = false;
                    cad += b;
                    --rest;
                    ++c;
                    chd -= cak;
                }
                if (chd <= 0) {
                    break;
                }
            }

            if (chd <= 0) {
                continue;
            }

            /*
            if (i == 0 && j == 1) {
                cerr << chd << " " << cad << " " << chk << " " << cak << endl;
            }*/
            //cerr << hd << " " << cak << endl;
            
            flag = false;
            while (chk > 0) {
                //cerr << chd << " " << cak << endl;
                if (chk > cad && chd <= cak) {
                    if (flag) {
                        chd = -1;
                        break;
                    }
                    flag = true;
                    chd = hd;
                    ++c;
                    chd -= cak;
                } else {
                    flag = false;
                    chk -= cad;
                    ++c;
                    if (chk > 0) {
                        chd -= cak;
                    }
                }
                if (chd <= 0) {
                    break;
                }
            }
            if (chd <= 0) {
                continue;
            }

            ans = min(ans, (ll) c);
        }
    }

    if (ans == INFL) {
        cout << "IMPOSSIBLE\n";
    } else {
        cout << ans << "\n";
    }
 
    return 0;
}

int main() {
    //freopen(TASK_NAME ".in", "r", stdin);
    //freopen(TASK_NAME ".out", "w", stdout);

    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }

    #ifdef LOCAL
        cerr << "time: " << clock() << endl;
    #endif
    return 0;
}