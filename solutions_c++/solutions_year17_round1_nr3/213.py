#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int INF = 2147483647;
ll DINF = 1000000000000000000;

int main() {
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        ll hd, ad, hk, ak, b, d;
        cin >> hd >> ad >> hk >> ak >> b >> d;
        // cout << "Case #" << (t+1) << ": ";
        // if (ad >= hk) {
        //     cout << 1 << endl;
        //     continue;
        // }

        int C = 420;
        ll mn = DINF;
        rep(debuffs,0,C) {
            // if (debuffs != 0) continue;
            ll h = hd,
               a = ak;
            bool ok = true;
            rep(i,0,debuffs) {
                ll na = max(0LL,a-d);
                if (h - na <= 0) {
                    h = hd;
                } else {
                    a = na;
                }
                h -= a;
                if (h <= 0) {
                    ok = false;
                    break;
                }
            }
            if (!ok) {
// cout << "mewo" << endl;
                continue; // TODO: probably break
            }

            rep(buffs,0,C) {
                // if (buffs != 0) continue;
                // if (buffs != 1) continue;
                ll mya = ad,
                   h2 = h;
                bool ok2 = true;
                rep(i,0,buffs) {
                    if (h2 - a <= 0) {
                        h2 = hd;
                    } else {
                        mya += b;
                    }
                    h2 -= a;
                    if (h2 <= 0) {
                        ok2 = false;
                        break;
                    }
                }
                if (!ok2) {
// cout << "moo" << endl;
                    continue; // TODO: probably break
                }

                // cout << mya << " " << h2 << " " << hk << endl;

                ll hish = hk;
                rep(kill,0,C) {
                    // cout << h2 << " " << hish << endl;
                    if (h2 - a <= 0 && hish - mya > 0) {
                        h2 = hd;
                    } else {
                        hish -= mya;
                    }
                    if (hish <= 0) {
                        mn = min(mn, debuffs + buffs + kill + 1LL);
                        break;
                    }
                    h2 -= a;
                    if (h2 <= 0) {
                        break;
                    }
                }
            }
        }

        cout << "Case #" << (t+1) << ": ";
        if (mn == DINF)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << mn << endl;
    }
    return 0;
}

