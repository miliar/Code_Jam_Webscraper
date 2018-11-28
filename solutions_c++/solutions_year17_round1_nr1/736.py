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
    uint t;

    cin >> t;

    forn(tt,t) {
        cout << "Case #" << tt+1 << ":" << endl;

        uint r,c;

        cin >> r >> c;

        vector<string> v;
        v.resize(r);
        forn(i,r) {
            cin >> v[i];
        }

        tint firstNE = -1;

        string empty = string(c, '?');

        forn(i,r) {
            if(v[i] == empty) {
                if(firstNE != -1) {
                    v[i] = v[i-1];
                } else {
                    continue;
                }
            } else {
                if(firstNE == -1) {
                    firstNE = i;
                }

                char f = 0;
                char l = 0;
                tint pf = -1;

                forn(j,c) {
                    if(v[i][j] != '?') {
                        l = v[i][j];
                        if(f == 0) {
                            f = v[i][j];
                            pf = j;
                        }
                    } else {
                        if(l != 0) {
                            v[i][j] = l;
                        }
                    }
                }

                forn(j,pf) {
                    v[i][j] = f;
                }
            }
        }
        forn(i,firstNE) {
            v[i] = v[firstNE];
        }

        for(auto ss : v) {
            cout << ss << endl;
        }
    }

    return 0;
}
