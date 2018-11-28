#include <bits/stdc++.h>
using namespace std;
#define forsn(i, s, n) for (tint i = (tint)(s); i < (tint)(n); i++)
#define forn(i, n) forsn(i, 0, n)
#define dforsn(i, s, n) for (tint i = (tint)(n) - 1; i >= (tint)(s); i--)
#define dforn(i, n) dforsn(i, 0, n)
#define pb push_back
#define fst first
#define snd second
#define tint long long
#define uint unsigned tint
#define debug(v) cerr << #v << " = " << v << '\n';

int main() {
    tint t;

    cin >> t;

    forn(tt,t) {
        cout << "Case #" << tt+1 << ": ";

        tint n,p;
        cin >> n >> p;

        vector<tint> mods(p,0);

        forn(i,n) {
            tint gr;
            cin >> gr;
            mods[gr % p] += 1;
        }

        tint res = mods[0];
        mods[0] = 0;

        forsn(i, 1, p) {
            if(i > p-i) break;

            tint m;
            if(i == p-i) {
                m = mods[i]/2;
            } else {
                m = min(mods[i], mods[p-i]);
            }

            mods[i] -= m;
            mods[p-i] -= m;
            res += m;
        }

        //debug(mods[0]);
        //debug(mods[1]);
        //debug(mods[2]);

        if(p == 2){
            res += ((mods[1]+2-1) / 2);
        } else if (p==3) {
            res += ((mods[1]+3-1) / 3);
            res += ((mods[2]+3-1) / 3);
        } else if (p==4) {
            tint m = min(mods[1]/2, mods[2]);
            res += m;
            mods[1] -= m*2;
            mods[2] -= m;

            m = min(mods[3]/2, mods[2]);
            res += m;
            mods[3] -= m*2;
            mods[2] -= m;

            m = mods[1] / 4;
            res += m;
            mods[1] -= m*4;

            m = mods[3] / 4;
            res += m;
            mods[3] -= m*4;

            if(mods[1] + mods[2] + mods[3] > 0)
                res += 1;
        }

        cout << res << endl;
    }

    return 0;
}
